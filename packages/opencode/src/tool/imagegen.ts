import { Effect, Schema } from "effect"
import * as Tool from "./tool"
import * as fs from "node:fs/promises"
import * as path from "node:path"
import DESCRIPTION from "./imagegen.txt"

export const Parameters = Schema.Struct({
  prompt: Schema.String.annotations({ description: "The detailed image generation prompt describing the brand visual to generate" }),
  filename: Schema.String.annotations({ description: "Output filename without extension, e.g. 'logo-primary' or 'color-palette'" }),
  size: Schema.optional(
    Schema.Literal("1024x1024", "1024x1792", "1792x1024")
  ).annotations({ description: "Image dimensions. Default: 1024x1024" }),
  quality: Schema.optional(
    Schema.Literal("low", "medium", "high", "auto")
  ).annotations({ description: "Image quality. Default: auto" }),
})

type ImageResponse = { data: Array<{ b64_json: string }> }

export const ImageGenTool = Tool.define(
  "imagegen",
  Effect.gen(function* () {
    return {
      description: DESCRIPTION,
      parameters: Parameters,
      execute: (params: Schema.Schema.Type<typeof Parameters>, ctx: Tool.Context) =>
        Effect.gen(function* () {
          const size = params.size ?? "1024x1024"
          const quality = params.quality ?? "auto"

          yield* ctx.metadata({
            title: `Generating ${params.filename}.png (${size})`,
            metadata: { filename: params.filename, size, quality },
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
            },
          })

          const apiKey = process.env.OPENAI_API_KEY
          if (!apiKey) {
            return {
              output: "Error: OPENAI_API_KEY environment variable is not set. Please set it before using the imagegen tool.",
              title: "imagegen: missing API key",
              metadata: { error: "missing_api_key" },
            }
          }

          const response = yield* Effect.promise(() =>
            fetch("https://api.openai.com/v1/images/generations", {
              method: "POST",
              headers: {
                Authorization: `Bearer ${apiKey}`,
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                model: "gpt-image-2",
                prompt: params.prompt,
                n: 1,
                size,
                quality,
                response_format: "b64_json",
              }),
            })
          )

          if (!response.ok) {
            const text = yield* Effect.promise(() => response.text())
            return {
              output: `OpenAI API error (HTTP ${response.status}): ${text.slice(0, 500)}`,
              title: "imagegen: API error",
              metadata: { error: "api_error", status: response.status },
            }
          }

          const json: ImageResponse = yield* Effect.promise(
            () => response.json() as Promise<ImageResponse>
          )

          const b64 = json.data[0]?.b64_json
          if (!b64) {
            return {
              output: "OpenAI returned no image data.",
              title: "imagegen: empty response",
              metadata: { error: "empty_response" },
            }
          }

          const outputDir = path.join(process.cwd(), "design-output")
          yield* Effect.promise(() => fs.mkdir(outputDir, { recursive: true }))

          const outputPath = path.join(outputDir, `${params.filename}.png`)
          yield* Effect.promise(() =>
            fs.writeFile(outputPath, Buffer.from(b64, "base64"))
          )

          return {
            output: `Image saved to: ${outputPath}\nSize: ${size} | Quality: ${quality}\nPrompt: ${params.prompt.slice(0, 200)}`,
            title: `imagegen: ${params.filename}.png`,
            metadata: { path: outputPath, size, quality },
          }
        }),
    }
  }),
)
