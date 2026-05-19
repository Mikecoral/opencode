/// <reference path="../env.d.ts" />
import { tool } from "@opencode-ai/plugin"
import * as fs from "node:fs/promises"
import * as path from "node:path"

const SOCIOBENCH_ROOT = "/Users/hongyuecheng/python-learn/SII/AIdesign/SocioBench-main"
const DATA_DIR = path.join(SOCIOBENCH_ROOT, "Dataset_all", "A_GroundTruth_sampling500")

const DOMAIN_FILE = {
  citizenship: "issp_answer_citizenship.json",
  environment: "issp_answer_environment.json",
  family: "issp_answer_family.json",
  health: "issp_answer_health.json",
  nationalidentity: "issp_answer_nationalidentity.json",
  religion: "issp_answer_religion.json",
  roleofgovernment: "issp_answer_roleofgovernment.json",
  socialinequality: "issp_answer_socialinequality.json",
  socialnetworks: "issp_answer_socialnetworks.json",
  workorientations: "issp_answer_workorientations.json",
} as const

const PROFILE_FIELDS = [
  "Country Prefix ISO 3166",
  "Sex of Respondent",
  "Age of respondent",
  "Year of birth",
  "Highest completed education level: Categories for international comparison",
  "Education I: years of schooling",
  "Currently, formerly, or never in paid work",
  "Hours worked weekly",
  "Main status",
  "Employment relationship",
  "Occupation ISCO/ ILO 2008",
  "Occupation ISCO 2008",
  "Supervise anyone directly responsible",
  "Supervise other employees",
  "Trade union membership",
  "Type of organisation, for-profit/ non-profit",
  "Type of organisation, for-profit/non-profit",
  "Type of organisation, public/ private",
  "Type of organisation, public/private",
  "Living in steady partnership",
  "Legal partnership status",
  "Father's country of birth",
  "Mother's country of birth",
  "Groups of religious affiliations (derived from nat_RELIG)",
  "Comparative: groups of religious affiliations",
  "Attendance of religious services",
  "Top-Bottom self-placement",
  "Did respondent vote in last general election",
  "Did respondent vote in last general election?",
  "R: Party voted for in last general election: left-right (derived from nat_PRTY)",
  "Party respondent voted for in last general election: left-right scale",
  "How many persons in household",
  "How many adults in household",
  "How many children in household: children between [school age] and 17 years of age",
  "How many children above school entry age in household",
  "How many toddlers in household: children up to [school age -1] years",
  "How many children below school age in household",
  "Place of living: urban - rural",
  "Administrative mode of data-collection",
] as const

const FIELD_ALIASES = {
  country: ["Country Prefix ISO 3166", "Country/ Sample Prefix ISO 3166 Code - alphanumeric"],
  sex: ["Sex of Respondent", "Sex of respondent"],
  age: ["Age of respondent"],
  education: [
    "Highest completed education level: Categories for international comparison",
    "ISCED 2011 simplified: highest completed degree of education",
    "ISCED 2011: highest completed degree of education [merged variable]",
  ],
  schooling: ["Education I: years of schooling", "Years of full-time schooling"],
  religion: ["Groups of religious affiliations (derived from nat_RELIG)", "Comparative: groups of religious affiliations"],
  children: [
    "How many children in household: children between [school age] and 17 years of age",
    "How many children above school entry age in household",
  ],
} as const

type Domain = keyof typeof DOMAIN_FILE
type RawRecord = {
  person_id?: unknown
  attributes?: Record<string, unknown>
}

function clean(value: unknown) {
  if (typeof value !== "string") return undefined
  const text = value.trim()
  if (!text || /^(NAP|NAV|Not available|No answer)/i.test(text)) return undefined
  return text
}

function firstValue(attributes: Record<string, unknown>, fields: readonly string[]) {
  return fields.map((field) => clean(attributes[field])).find(Boolean)
}

function country(attributes: Record<string, unknown>) {
  const value = firstValue(attributes, FIELD_ALIASES.country)
  if (value === "United Stated") return "United States"
  return value
}

function countrySpecific(attributes: Record<string, unknown>, profileCountry: string | undefined, needles: readonly string[]) {
  if (!profileCountry) return []
  const normalizedCountry = profileCountry.toLowerCase()
  return Object.entries(attributes).flatMap(([field, value]) => {
    const text = clean(value)
    const lower = field.toLowerCase()
    if (!text) return []
    if (!lower.includes(normalizedCountry)) return []
    if (!needles.some((needle) => lower.includes(needle))) return []
    return [[field, text]]
  })
}

function ageBand(attributes: Record<string, unknown>) {
  const age = Number.parseInt(firstValue(attributes, FIELD_ALIASES.age) ?? "", 10)
  if (!Number.isFinite(age)) return undefined
  if (age <= 30) return "18-30"
  if (age <= 45) return "31-45"
  if (age <= 60) return "46-60"
  if (age <= 75) return "61-75"
  return "76+"
}

function hash(input: string) {
  return Array.from(input).reduce((value, char) => (value * 31 + char.charCodeAt(0)) >>> 0, 2166136261)
}

function inferDomain(projectSummary: string): Domain {
  const text = projectSummary.toLowerCase()
  if (/(health|medical|hospital|care|wellness)/.test(text)) return "health"
  if (/(environment|climate|sustainability|green|energy)/.test(text)) return "environment"
  if (/(family|parent|child|gender)/.test(text)) return "family"
  if (/(government|policy|public sector|civic)/.test(text)) return "roleofgovernment"
  if (/(religion|faith|spiritual)/.test(text)) return "religion"
  if (/(national|identity|culture|country)/.test(text)) return "nationalidentity"
  if (/(inequality|class|income|fairness|equity)/.test(text)) return "socialinequality"
  if (/(network|community|social|friend|relationship)/.test(text)) return "socialnetworks"
  if (/(citizen|citizenship|rights|participation)/.test(text)) return "citizenship"
  return "workorientations"
}

function profileFromRecord(record: RawRecord) {
  const attributes = record.attributes ?? {}
  const profileCountry = country(attributes)
  const selected = Object.fromEntries(
    [
      ...PROFILE_FIELDS,
      ...FIELD_ALIASES.country,
      ...FIELD_ALIASES.sex,
      ...FIELD_ALIASES.education,
      ...FIELD_ALIASES.schooling,
      ...FIELD_ALIASES.religion,
      ...FIELD_ALIASES.children,
    ]
      .flatMap((field) => {
        const value = clean(attributes[field])
        return value ? [[field, value]] : []
      })
      .concat(
        countrySpecific(attributes, profileCountry, [
          "highest completed degree",
          "personal income",
          "household income",
          "party voted",
          "region",
          "ethnic group",
          "religious affiliation",
        ]),
      ),
  )
  return {
    person_id: typeof record.person_id === "number" || typeof record.person_id === "string" ? record.person_id : undefined,
    segment: {
      country: profileCountry ?? "Unknown",
      sex: firstValue(attributes, FIELD_ALIASES.sex) ?? "Unknown",
      age_band: ageBand(attributes) ?? "Unknown",
      work_status: clean(attributes["Main status"]) ?? clean(attributes["Currently, formerly, or never in paid work"]) ?? "Unknown",
      place: clean(attributes["Place of living: urban - rural"]) ?? "Unknown",
    },
    attributes: selected,
  }
}

export default tool({
  description: `Sample compact demographic profiles from the local SocioBench ISSP data for crowd-based brand design critique.

Use this before running crowd critic. The tool automatically chooses a loose SocioBench domain from the project summary unless a domain is provided, then returns diverse, compact profiles suitable for VLM-based audience simulation.`,
  args: {
    projectSummary: tool.schema.string().describe("Brief summary of the brand design project or target audience context"),
    sampleSize: tool.schema.number().min(1).max(48).default(12).describe("Number of profiles to sample. Default: 12"),
    seed: tool.schema.string().default("crowd-critic").describe("Stable seed for reproducible profile sampling"),
    domain: tool.schema
      .enum(["auto", ...Object.keys(DOMAIN_FILE)] as ["auto", Domain, ...Domain[]])
      .default("auto")
      .describe("Optional SocioBench domain. Use auto unless the project clearly maps to one domain."),
  },
  async execute(args) {
    const domain = args.domain === "auto" ? inferDomain(args.projectSummary) : args.domain
    const records = JSON.parse(await fs.readFile(path.join(DATA_DIR, DOMAIN_FILE[domain]), "utf8")) as RawRecord[]
    const shuffled = records
      .map((record) => profileFromRecord(record))
      .sort((a, b) => hash(`${args.seed}:${a.person_id}`) - hash(`${args.seed}:${b.person_id}`))

    const byCountry = Map.groupBy(shuffled, (profile) => profile.segment.country)
    const countries = Array.from(byCountry.keys()).sort(
      (a, b) => hash(`${args.seed}:country:${a}`) - hash(`${args.seed}:country:${b}`),
    )
    const sampled = Array.from({ length: args.sampleSize })
      .flatMap((_, index) => countries.flatMap((country) => byCountry.get(country)?.[index] ?? []))
      .slice(0, args.sampleSize)

    return JSON.stringify(
      {
        source: {
          dataset: "SocioBench ISSP sampling500",
          path: path.join(DATA_DIR, DOMAIN_FILE[domain]),
          domain,
          sample_size: sampled.length,
          seed: args.seed,
        },
        note: "Profiles are demographic context for simulated audience critique, not real design preference labels.",
        profiles: sampled,
      },
      null,
      2,
    )
  },
})
