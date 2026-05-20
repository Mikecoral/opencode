/// <reference path="../env.d.ts" />
import { tool } from "@opencode-ai/plugin"
import * as path from "node:path"

const DOMAINS = [
  "auto",
  "citizenship",
  "environment",
  "family",
  "health",
  "nationalidentity",
  "religion",
  "roleofgovernment",
  "socialinequality",
  "socialnetworks",
  "workorientations",
] as const
const DOMAIN_SELECTORS = ["keyword", "llm"] as const
const SAMPLING_STRATEGIES = ["country_diverse", "llm_plan"] as const

export default tool({
  description: `Run a complete AI-Press-inspired crowd critic simulation for brand design assets.

This tool is a thin OpenCode wrapper around .opencode/scripts/crowd_critic_runner.py. The Python runner owns profile sampling, profile x image VLM analysis, simulated audience comments, JSONL artifacts, and validation.`,
  args: {
    outputDir: tool.schema.string().describe("Directory containing brief.md and design-assets.md"),
    projectSummary: tool.schema.string().describe("Original brand request or concise project summary"),
    sampleSize: tool.schema
      .number()
      .min(1)
      .max(200)
      .default(100)
      .describe("Number of profiles to sample. Default 100; use 24 or smaller for cheaper smoke tests."),
    seed: tool.schema.string().default("crowd-critic").describe("Stable seed for reproducible sampling"),
    domain: tool.schema.enum(DOMAINS).default("auto").describe("Optional SocioBench domain"),
    domainSelector: tool.schema
      .enum(DOMAIN_SELECTORS)
      .default("keyword")
      .describe("How to choose the single SocioBench domain when domain=auto."),
    samplingStrategy: tool.schema
      .enum(SAMPLING_STRATEGIES)
      .default("country_diverse")
      .describe("Use llm_plan to let the model create executable buckets from the selected domain's empirical field summary."),
    samplingOnly: tool.schema
      .boolean()
      .default(false)
      .describe("Only generate domain/profile/sampling artifacts and skip VLM calls."),
    allowSmallSample: tool.schema
      .boolean()
      .default(false)
      .describe("Allow sample sizes below 100. Use only for smoke tests or explicit debugging."),
  },
  async execute(args) {
    const proc = Bun.spawn(
      [
        "python3",
        path.join(process.cwd(), ".opencode/scripts/crowd_critic_runner.py"),
        "--output-dir",
        args.outputDir,
        "--project-summary",
        args.projectSummary,
        "--sample-size",
        String(args.sampleSize),
        "--seed",
        args.seed,
        "--domain",
        args.domain,
        "--domain-selector",
        args.domainSelector,
        "--sampling-strategy",
        args.samplingStrategy,
        ...(args.samplingOnly ? ["--sampling-only"] : []),
        ...(args.allowSmallSample ? ["--allow-small-sample"] : []),
      ],
      {
        cwd: process.cwd(),
        env: process.env,
        stdout: "pipe",
        stderr: "pipe",
      },
    )
    const [stdout, stderr, code] = await Promise.all([new Response(proc.stdout).text(), new Response(proc.stderr).text(), proc.exited])
    if (code !== 0) throw new Error([`crowd_critic_runner.py failed with exit code ${code}`, stderr, stdout].filter(Boolean).join("\n\n"))
    return stdout.trim()
  },
})
