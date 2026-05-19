---
name: social-content
description: Generates platform-specific social media content using a completed brand identity. Requires a brand brief and design assets to already exist.
triggers:
  - social media content
  - social posts
  - 社交媒体内容
  - 社媒文案
  - 品牌社媒
  - generate posts
---

# Social Content Generator

Generate platform-specific social media content for a brand that has a completed identity (brief + visual assets).

## Before Starting

Ask the user:
1. Which platforms? (WeChat / Weibo / Xiaohongshu / LinkedIn / Instagram / Twitter — select all that apply)
2. What is the occasion? (brand launch, event promotion, ongoing content, campaign)
3. How many posts per platform?

Then read:
- `[RUN_DIR]/brief.md` — brand voice, audience, values
- `[RUN_DIR]/copy.md` — taglines and voice guidelines (if it exists)

## Content Pillars

Before writing posts, define 3 content pillars from the brief:
- **Pillar 1**: What the brand builds / does (educational, product-led)
- **Pillar 2**: The community / people it serves (social proof, stories)
- **Pillar 3**: The brand's point of view / values (thought leadership)

Each post should belong to one pillar.

## Platform Rules

### WeChat / 微信公众号
- Tone: warm, thoughtful, longer-form acceptable
- Structure: hook sentence → story or insight → soft CTA
- Length: 150–400 characters for headline posts; full articles for in-depth
- Emoji: 1–2 max, functional not decorative

### Xiaohongshu / 小红书
- Tone: authentic, peer-to-peer, experience-sharing
- Structure: relatable hook → personal angle → useful info → tags
- Length: 150–300 characters
- Include 5–8 relevant hashtags
- First line must stop the scroll — use a question or bold claim

### Weibo
- Tone: punchy, opinionated, shareable
- Length: ≤140 characters ideally
- End with a question or open statement to drive comments
- Include 2–3 topic tags (#tag#)

### LinkedIn
- Tone: professional but human, insight-driven
- Structure: 1-line hook → 3–5 short paragraphs → CTA
- Length: 150–300 words
- No jargon; lead with a concrete observation or result

### Instagram
- Tone: visual-first, aspirational but grounded
- Caption: hook in first line (shown before "more"), 3–5 sentences, CTA
- Include 8–15 hashtags in first comment or end of caption
- Alt-text suggestion for each post

## Hook Formulas (use one per post)

- **Curiosity**: "Most people don't know that [surprising fact about brand/field]..."
- **Story arc**: "Six months ago, [problem]. Today, [transformation]."
- **Value lead**: "Here's how to [outcome] in [timeframe]:"
- **Contrarian**: "Everyone says [common belief]. We disagree."
- **Question**: "[Relatable question the audience asks themselves]?"

## Output Format

Save to `[RUN_DIR]/social-content.md`:

```
# Social Content: [Organization Name]

## Content Pillars
- Pillar 1: ...
- Pillar 2: ...
- Pillar 3: ...

---

## [Platform Name]

### Post 1 — Pillar: [X] | Hook type: [Y]
[Full post copy ready to publish]
Tags: ...

### Post 2 — ...

---

[Repeat for each platform]
```

After saving, tell the user: "Social content ready at `[RUN_DIR]/social-content.md`. [N] posts across [platforms]."
