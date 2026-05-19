import { Effect, Schema } from "effect"
import * as Tool from "./tool"
import * as fs from "node:fs/promises"
import * as path from "node:path"
import DESCRIPTION from "./image_analyze.txt"
import { Config } from "@/config/config"
const DEFAULT_BASE_URL = "https://api.openai.com/v1"
//const DEFAULT_BASE_URL = "https://apicz.boyuerichdata.com/v1"
const DEFAULT_ANALYSIS_PROMPT = `You are a senior brand design critic. Analyze this brand design image and provide:

1. **Composition & Layout**: How is the image structured? Is the visual hierarchy clear?
2. **Color Use**: What colors are present? Is the palette coherent and appropriate? Any AI-default clichés (purple→blue gradients, generic indigo)?
3. **Typography**: What text appears? Is it legible, well-set, and appropriate to the brand context?
4. **Design Quality**: Does this look like professional brand design or generic AI output? Specific issues?
5. **Cultural Appropriateness**: If cultural motifs are present, are they accurately and respectfully rendered?
6. **Overall Assessment**: Score 1-10 and summarize the key strengths and weaknesses in 2-3 sentences.

Be specific and critical. Vague praise is not useful.`

function optionString(value: unknown) {
  return typeof value === "string" && value.trim() ? value.trim() : undefined
}

export const Parameters = Schema.Struct({
  imagePath: Schema.String.annotate({
    description:
      "Path to the PNG file — relative to cwd (e.g. design-output/20260518-1423/logo-primary.png) or absolute.",
  }),
  question: Schema.optional(Schema.String).annotate({
    description: "Specific question about the image. Defaults to a comprehensive brand design quality assessment.",
  }),
  logFile: Schema.optional(Schema.String).annotate({
    description:
      "If provided, the exact prompt and full response are appended verbatim to this file after every call. Use for crowd-critic session logs (e.g. design-output/20260518-1423/crowd-critic-full-log.md).",
  }),
})

export const ImageAnalyzeTool = Tool.define(
  "image_analyze",
  Effect.gen(function* () {
    const config = yield* Config.Service

    return {
      description: DESCRIPTION,
      parameters: Parameters,
      execute: (
        params: Schema.Schema.Type<typeof Parameters>,
        ctx: Tool.Context,
      ): Effect.Effect<Tool.ExecuteResult> =>
        Effect.gen(function* () {
          const cfg = yield* config.get()
          const openaiOptions = cfg.provider?.["openai"]?.options ?? {}
          const apiKey =
            optionString(process.env.OPENAI_API_KEY) ?? optionString(openaiOptions.apiKey)
          const baseURL = (
            optionString(process.env.OPENAI_BASE_URL) ??
            optionString(openaiOptions.baseURL) ??
            DEFAULT_BASE_URL
          ).replace(/\/+$/, "")
          const model =
            optionString(process.env.OPENAI_VISION_MODEL) ??
            optionString(openaiOptions.visionModel) ??
            optionString(openaiOptions.modelId) ??
            "gpt-4o"

          const analysisPrompt = params.question ?? DEFAULT_ANALYSIS_PROMPT

          yield* ctx.metadata({
            title: `Analyzing ${path.basename(params.imagePath)}`,
            metadata: { imagePath: params.imagePath, model },
          })

          if (!apiKey) {
            return {
              output:
                "Error: no OpenAI API key configured. Set OPENAI_API_KEY or provider.openai.options.apiKey.",
              title: "image_analyze: missing API key",
              metadata: { error: "missing_api_key" },
            }
          }

          // Resolve path — support both relative (to cwd) and absolute
          const resolvedPath = path.isAbsolute(params.imagePath)
            ? params.imagePath
            : path.join(process.cwd(), params.imagePath)

          const readResult = yield* Effect.promise(async () => {
            try {
              const buf = await fs.readFile(resolvedPath)
              return { ok: true as const, base64: buf.toString("base64") }
            } catch (e) {
              return {
                ok: false as const,
                message: e instanceof Error ? e.message : String(e),
              }
            }
          })

          if (!readResult.ok) {
            return {
              output: `Error reading image file: ${readResult.message}\nResolved path: ${resolvedPath}`,
              title: "image_analyze: file not found",
              metadata: { error: "file_not_found", path: resolvedPath },
            }
          }

          const response = yield* Effect.promise(() =>
            fetch(`${baseURL}/chat/completions`, {
              method: "POST",
              headers: {
                Authorization: `Bearer ${apiKey}`,
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                model,
                max_tokens: 4000,
                messages: [
                  {
                    role: "user",
                    content: [
                      {
                        type: "image_url",
                        image_url: {
                          url: `data:image/png;base64,${readResult.base64}`,
                          detail: "high",
                        },
                      },
                      { type: "text", text: analysisPrompt },
                    ],
                  },
                ],
              }),
              signal: ctx.abort,
            }),
          )

          if (!response.ok) {
            const text = yield* Effect.promise(() => response.text())
            return {
              output: `OpenAI vision API error (HTTP ${response.status}): ${text.slice(0, 500)}\n\nNote: ensure your model supports vision (gpt-4o, gpt-4.1, etc.).`,
              title: "image_analyze: API error",
              metadata: { error: "api_error", status: response.status },
            }
          }

          type ChatResponse = {
            choices?: Array<{ message?: { content?: string } }>
            error?: { message?: string }
          }
          const json: ChatResponse = yield* Effect.promise(() => response.json() as Promise<ChatResponse>)

          const content = json.choices?.[0]?.message?.content
          if (!content) {
            return {
              output: `OpenAI returned no analysis content. Response: ${JSON.stringify(json).slice(0, 300)}`,
              title: "image_analyze: empty response",
              metadata: { error: "empty_response" },
            }
          }

          if (params.logFile) {
            const logPath = path.isAbsolute(params.logFile)
              ? params.logFile
              : path.join(process.cwd(), params.logFile)
            const entry = [
              "---",
              `Asset: ${path.basename(params.imagePath)}`,
              `Timestamp: ${new Date().toISOString()}`,
              "Prompt sent:",
              analysisPrompt,
              "",
              "Response received:",
              content,
              "---",
              "",
            ].join("\n")
            yield* Effect.promise(() => fs.appendFile(logPath, entry, "utf8").catch(() => {}))
          }

          return {
            output: `## Image Analysis: ${path.basename(params.imagePath)}\n\n${content}`,
            title: `image_analyze: ${path.basename(params.imagePath)}`,
            metadata: { path: resolvedPath, model },
          }
        }),
    }
  }),
)
