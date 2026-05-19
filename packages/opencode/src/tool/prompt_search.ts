import { Effect, Schema } from "effect"
import * as Tool from "./tool"
import * as fs from "node:fs/promises"
import * as path from "node:path"
import * as os from "node:os"
import DESCRIPTION from "./prompt_search.txt"

const DEFAULT_LIBRARY_PATH = path.join(
  os.homedir(),
  "python-learn/SII/AIdesign/awesome-gpt-image-2-API-and-Prompts-main",
)

type PromptEntry = {
  number: number
  title: string
  description: string
  promptBody: string
  searchableText: string
}

const cache = new Map<string, PromptEntry[]>()

function optionString(value: unknown) {
  return typeof value === "string" && value.trim() ? value.trim() : undefined
}

function parseCaseFile(content: string, category: string): PromptEntry[] {
  const blocks = content.split(/\n(?=### Case\s+\d+:)/g)
  const entries: PromptEntry[] = []

  for (const block of blocks) {
    const headerMatch = block.match(/^### Case\s+(\d+):\s*\[([^\]]+)\]/)
    if (!headerMatch) continue

    const number = Number.parseInt(headerMatch[1], 10)
    const title = headerMatch[2].trim()

    const promptMatch = block.match(/\*\*Prompt:\*\*\s*\n+```[a-zA-Z]*\n([\s\S]*?)\n```/)
    const promptBody = promptMatch ? promptMatch[1].trim() : ""

    if (!promptBody) continue

    entries.push({
      number,
      title,
      description: category,
      promptBody,
      searchableText: `${title}\n${category}\n${promptBody}`.toLowerCase(),
    })
  }

  return entries
}

function parseReadme(content: string): PromptEntry[] {
  // Legacy format: ### No. N: Title with #### Description/Prompt sections
  const blocks = content.split(/\n(?=### No\.\s+\d+:)/g)
  const entries: PromptEntry[] = []

  for (const block of blocks) {
    const headerMatch = block.match(/^### No\.\s+(\d+):\s*(.+?)\s*$/m)
    if (!headerMatch) continue

    const number = Number.parseInt(headerMatch[1], 10)
    const title = headerMatch[2].trim()

    const descMatch = block.match(/####\s+(?:📖\s+)?Description\s*\n+([^\n][\s\S]*?)(?=\n####|\n---|$)/)
    const description = descMatch ? descMatch[1].trim().split(/\n\s*\n/)[0].trim() : ""

    const promptMatch = block.match(/####\s+(?:📝\s+)?Prompt\s*\n+```[a-zA-Z]*\n([\s\S]*?)\n```/)
    const promptBody = promptMatch ? promptMatch[1].trim() : ""

    if (!promptBody) continue

    entries.push({
      number,
      title,
      description,
      promptBody,
      searchableText: `${title}\n${description}\n${promptBody}`.toLowerCase(),
    })
  }

  return entries
}

const CATEGORY_NAMES: Record<string, string> = {
  "poster": "Poster & Illustration",
  "portrait": "Portrait & Photography",
  "ecommerce": "E-commerce",
  "ad-creative": "Ad Creative",
  "character": "Character Design",
  "ui": "UI & Social Media Mockup",
  "comparison": "Comparison & Community",
}

async function loadLibrary(libraryPath: string, language: "en" | "zh"): Promise<PromptEntry[]> {
  const cacheKey = `${libraryPath}:${language}`
  const cached = cache.get(cacheKey)
  if (cached) return cached

  // Try cases/ directory first (new format)
  const casesDir = path.join(libraryPath, "cases")
  try {
    const files = await fs.readdir(casesDir)
    const langSuffix = language === "zh" ? "_zh-CN.md" : ".md"
    const allEntries: PromptEntry[] = []
    let globalNum = 1

    for (const file of files.sort()) {
      if (!file.endsWith(langSuffix)) continue
      const baseName = file.replace(langSuffix, "")
      if (language === "en" && /_(de|es|fr|ja|ko|pt|ru|tr|zh)/.test(baseName)) continue
      const category = CATEGORY_NAMES[baseName] ?? baseName
      const content = await fs.readFile(path.join(casesDir, file), "utf-8")
      const parsed = parseCaseFile(content, category)
      for (const entry of parsed) {
        allEntries.push({ ...entry, number: globalNum++ })
      }
    }

    if (allEntries.length > 0) {
      cache.set(cacheKey, allEntries)
      return allEntries
    }
  } catch {
    // fall through to README fallback
  }

  // Fallback: single README file (legacy format)
  const filename = language === "zh" ? "README_zh-CN.md" : "README.md"
  const fullPath = path.join(libraryPath, filename)
  const content = await fs.readFile(fullPath, "utf-8")
  const parsed = parseReadme(content)
  cache.set(cacheKey, parsed)
  return parsed
}

function scoreEntry(entry: PromptEntry, keywords: string[]): number {
  if (keywords.length === 0) return 0

  const titleLower = entry.title.toLowerCase()
  const descLower = entry.description.toLowerCase()
  const bodyLower = entry.promptBody.toLowerCase()

  let score = 0
  let matched = 0

  for (const kw of keywords) {
    const inTitle = titleLower.includes(kw)
    const inDesc = descLower.includes(kw)
    const inBody = bodyLower.includes(kw)

    if (!inTitle && !inDesc && !inBody) continue
    matched++
    if (inTitle) score += 3
    if (inDesc) score += 2
    if (inBody) score += 1
  }

  // Require at least 60% of keywords to match (min 1)
  const threshold = Math.max(1, Math.ceil(keywords.length * 0.6))
  return matched >= threshold ? score : 0
}

export const Parameters = Schema.Struct({
  keyword: Schema.String.annotate({
    description: "Free-text search query. Multiple words treated as AND.",
  }),
  topK: Schema.optional(Schema.Number).annotate({
    description: "Number of templates to return. Default 3. Max 10.",
  }),
  language: Schema.optional(Schema.Literals(["en", "zh"])).annotate({
    description: "Library language. 'en' = README.md, 'zh' = README_zh.md. Default 'en'.",
  }),
  libraryPath: Schema.optional(Schema.String).annotate({
    description: "Override the library root directory.",
  }),
})

export const PromptSearchTool = Tool.define(
  "prompt_search",
  Effect.gen(function* () {
    return {
      description: DESCRIPTION,
      parameters: Parameters,
      execute: (
        params: Schema.Schema.Type<typeof Parameters>,
        ctx: Tool.Context,
      ): Effect.Effect<Tool.ExecuteResult> =>
        Effect.gen(function* () {
          const language = params.language ?? "en"
          const topK = Math.min(Math.max(params.topK ?? 3, 1), 10)
          const libraryPath =
            optionString(params.libraryPath) ??
            optionString(process.env.PROMPT_LIBRARY_PATH) ??
            DEFAULT_LIBRARY_PATH

          yield* ctx.metadata({
            title: `prompt_search: "${params.keyword}" (${language}, topK=${topK})`,
            metadata: { keyword: params.keyword, language, topK, libraryPath },
          })

          const loadResult = yield* Effect.promise(async () => {
            try {
              const entries = await loadLibrary(libraryPath, language)
              return { ok: true as const, entries }
            } catch (e) {
              return { ok: false as const, message: e instanceof Error ? e.message : String(e) }
            }
          })

          if (!loadResult.ok) {
            return {
              output: `Error: ${loadResult.message}\n\nTo fix: ensure the awesome-gpt-image-2 repo is cloned at ${libraryPath}, or set PROMPT_LIBRARY_PATH env var to its location.`,
              title: "prompt_search: library not found",
              metadata: { error: "library_not_found" },
            }
          }
          const entries = loadResult.entries

          const keywords = params.keyword
            .toLowerCase()
            .split(/\s+/)
            .map((k: string) => k.trim())
            .filter((k: string) => k.length > 0)

          const scored = entries
            .map((entry: PromptEntry) => ({ entry, score: scoreEntry(entry, keywords) }))
            .filter((s: { entry: PromptEntry; score: number }) => s.score > 0)
            .sort((a: { score: number }, b: { score: number }) => b.score - a.score)
            .slice(0, topK)

          if (scored.length === 0) {
            return {
              output: `No matches found for keyword: "${params.keyword}".\nLibrary loaded: ${entries.length} prompts.\nTry broader or different keywords.`,
              title: "prompt_search: no matches",
              metadata: { keyword: params.keyword, total: entries.length, matches: 0 },
            }
          }

          const formatted = scored
            .map(({ entry, score }: { entry: PromptEntry; score: number }) => {
              return [
                `## Match — No. ${entry.number}: ${entry.title}`,
                `Score: ${score}`,
                "",
                `**Description:** ${entry.description || "(none)"}`,
                "",
                "**Prompt Template:**",
                "```",
                entry.promptBody,
                "```",
              ].join("\n")
            })
            .join("\n\n---\n\n")

          return {
            output: `Found ${scored.length} match(es) for "${params.keyword}" (library: ${entries.length} prompts):\n\n${formatted}`,
            title: `prompt_search: ${scored.length} match(es)`,
            metadata: {
              keyword: params.keyword,
              language,
              libraryPath,
              total: entries.length,
              matches: scored.length,
              top: scored.map((s: { entry: PromptEntry; score: number }) => ({
                number: s.entry.number,
                title: s.entry.title,
                score: s.score,
              })),
            },
          }
        }),
    }
  }),
)
