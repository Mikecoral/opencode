import { Effect, Schema } from "effect"
import * as Tool from "./tool"
import * as fs from "node:fs/promises"
import * as path from "node:path"
import DESCRIPTION from "./imagegen.txt"
import { Config } from "@/config/config"

const OUTPUT_DIR = "design-output"
const DEFAULT_BASE_URL = "https://api.openai.com/v1"
//const DEFAULT_BASE_URL = "https://apicz.boyuerichdata.com/v1"
const DEFAULT_MODEL = "gpt-image-2"

function optionString(value: unknown) {
  return typeof value === "string" && value.trim() ? value.trim() : undefined
}

export const Parameters = Schema.Struct({
  prompt: Schema.String.annotate({
    description: "The detailed image generation prompt describing the brand visual to generate",
  }),
  filename: Schema.String.annotate({
    description: "Output filename without extension, e.g. 'logo-primary' or 'color-palette'",
  }),
  size: Schema.optional(Schema.Literals(["1024x1024", "1024x1536", "1536x1024", "auto"])).annotate({
    description: "Image dimensions. Default: 1024x1024",
  }),
  quality: Schema.optional(Schema.Literals(["low", "medium", "high", "auto"])).annotate({
    description: "Image quality. Default: auto",
  }),
})

type ImageResponse = { data?: Array<{ b64_json?: string; url?: string }> }

export const ImageGenTool = Tool.define(
  "imagegen",
  Effect.gen(function* () {
    const config = yield* Config.Service

    return {
      description: DESCRIPTION,
      parameters: Parameters,
      execute: (params: Schema.Schema.Type<typeof Parameters>, ctx: Tool.Context): Effect.Effect<Tool.ExecuteResult> =>
        Effect.gen(function* () {
          const size = params.size ?? "1024x1024"
          const quality = params.quality ?? "auto"
          const cfg = yield* config.get()
          const openaiOptions = cfg.provider?.["openai"]?.options ?? {}
          const apiKey = optionString(process.env.OPENAI_API_KEY) ?? optionString(openaiOptions.apiKey)
          const baseURL = (
            optionString(process.env.OPENAI_BASE_URL) ??
            optionString(openaiOptions.baseURL) ??
            DEFAULT_BASE_URL
          ).replace(/\/+$/, "")
          const model =
            optionString(process.env.OPENAI_IMAGE_MODEL) ??
            optionString(openaiOptions.imageModel) ??
            optionString(openaiOptions.image_model) ??
            DEFAULT_MODEL

          yield* ctx.metadata({
            title: `Generating ${params.filename}.png (${size})`,
            metadata: { filename: params.filename, size, quality, model },
          })

          yield* ctx.ask({
            permission: "imagegen",
            patterns: [params.filename],
            always: ["*"],
            metadata: {
              prompt: params.prompt.slice(0, 120),
              filename: params.filename,
              size,
              quality,
              model,
            },
          })

          if (!apiKey) {
            return {
              output:
                "Error: no OpenAI API key configured. Set OPENAI_API_KEY or provider.openai.options.apiKey in .opencode/opencode.jsonc before using the imagegen tool.",
              title: "imagegen: missing API key",
              metadata: { error: "missing_api_key" },
            }
          }

          const response = yield* Effect.promise(() =>
            fetch(`${baseURL}/images/generations`, {
              method: "POST",
              headers: {
                Authorization: `Bearer ${apiKey}`,
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                model,
                prompt: params.prompt,
                n: 1,
                size,
                quality,
              }),
              signal: ctx.abort,
            }),
          )

          if (!response.ok) {
            const text = yield* Effect.promise(() => response.text())
            return {
              output: `OpenAI API error (HTTP ${response.status}): ${text.slice(0, 500)}`,
              title: "imagegen: API error",
              metadata: { error: "api_error", status: response.status },
            }
          }

          const json: ImageResponse = yield* Effect.promise(() => response.json() as Promise<ImageResponse>)

          const image = json.data?.[0]
          const buffer = image?.b64_json
            ? Buffer.from(image.b64_json, "base64")
            : yield* Effect.promise(async () => {
                if (!image?.url) return undefined
                const imageResponse = await fetch(image.url, { signal: ctx.abort })
                if (!imageResponse.ok) return undefined
                return Buffer.from(await imageResponse.arrayBuffer())
              })
          if (!buffer) {
            return {
              output: "OpenAI returned no image data.",
              title: "imagegen: empty response",
              metadata: { error: "empty_response" },
            }
          }

          // Callers sometimes reason in full run paths like `design-output/20260518-2304/logo-primary`,
          // but this tool already owns the `design-output/` root. Normalize that prefix so it is not doubled.
          const filename = params.filename.replace(/^design-output[\\/]+/, "")
          const outputPath = path.join(process.cwd(), OUTPUT_DIR, `${filename}.png`)
          yield* Effect.promise(() => fs.mkdir(path.dirname(outputPath), { recursive: true }))
          yield* Effect.promise(() => fs.writeFile(outputPath, buffer))

          return {
            output: `Image saved to: ${outputPath}\nModel: ${model} | Size: ${size} | Quality: ${quality}\nPrompt: ${params.prompt.slice(0, 200)}`,
            title: `imagegen: ${params.filename}.png`,
            metadata: { path: outputPath, size, quality, model },
          }
        }),
    }
  }),
)
