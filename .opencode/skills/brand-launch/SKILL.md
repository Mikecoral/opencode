---
name: brand-launch
description: Creates a phased brand launch or rebrand reveal plan using the completed brand identity. Covers owned, rented, and borrowed channels across pre-launch, launch day, and post-launch phases.
triggers:
  - brand launch
  - launch plan
  - 品牌发布
  - 发布计划
  - rebrand
  - 品牌上线
  - launch strategy
---

# Brand Launch Planner

Generate a phased brand launch plan for an organization with a completed brand identity.

## Before Starting

Ask the user:
1. What is being launched? (new brand, rebrand, new product/program under existing brand)
2. What is the target launch date?
3. What channels does the org currently have? (WeChat, website, events, email list, media contacts, etc.)
4. What is the primary goal? (awareness / community sign-ups / registrations / press coverage)

Then read `[RUN_DIR]/brief.md` for brand context, audience, and positioning.

## Channel Framework: Owned / Rented / Borrowed

**Owned** — full control, compounds over time
- WeChat official account, email list, website, community group

**Rented** — algorithm-dependent, good for reach
- Weibo, Xiaohongshu, LinkedIn, Instagram, TikTok

**Borrowed** — third-party audience, high credibility, one-time
- Press/media features, partner reposts, guest content, event speaking, KOL collaborations

Launch strategy should prioritize: Owned → Rented → Borrowed (invest in owned first so borrowed traffic has somewhere to land).

## Five-Phase Launch Plan

### Phase 0: Internal Alignment (2 weeks before)
- Share new identity with all internal stakeholders
- Align on key messages and Q&A for common questions
- Prepare all channel assets (profile photos, cover images, email headers)
- Soft-test brand with trusted community members

### Phase 1: Teaser (1 week before)
- Release 1–2 "something is coming" posts on rented channels
- Use brand visual language without full reveal
- Goal: curiosity, not confusion

### Phase 2: Launch Day
- Simultaneous update of all owned channel profiles
- Primary announcement post across all rented channels
- Outreach to borrowed channels (media pitches, partner reposts)
- Launch-day community engagement (respond to every comment)

### Phase 3: Amplification (week 1–2 post-launch)
- Deep-dive content: the story behind the brand, design process, values
- User-generated content prompt (encourage community to share)
- Follow up with any press/media that didn't cover launch day

### Phase 4: Normalization (month 2+)
- Shift from "we launched" to regular brand content cadence
- Monthly content calendar using social content pillars
- Track: follower growth, engagement rate, inbound mentions

## Deliverables

For each phase, specify:
- **What** to publish/do
- **Where** (channel)
- **Who** is responsible (if org context allows)
- **Key message** for that touchpoint
- **Sample copy** (1–2 sentences ready to use)

## Output Format

Save to `[RUN_DIR]/launch-plan.md`:

```
# Brand Launch Plan: [Organization Name]

Launch Date: [date]
Primary Goal: [goal]
Channels: [list]

## Channel Inventory
| Channel | Type | Current State | Launch Action |
|---------|------|--------------|--------------|
| WeChat | Owned | Active, 2k followers | Update profile + announcement article |
| ... | | | |

---

## Phase 0: Internal Alignment
Timeline: [dates]
| Action | Channel | Message | Sample Copy |
|--------|---------|---------|-------------|
| ... | | | |

## Phase 1: Teaser
[same table structure]

## Phase 2: Launch Day
[same table structure]

## Phase 3: Amplification
[same table structure]

## Phase 4: Normalization
[same table structure]

---

## Success Metrics
| Metric | Baseline | 30-day Target | 90-day Target |
|--------|----------|--------------|--------------|
| ... | | | |

## Risk & Contingency
[2–3 likely issues and how to respond]
```

After saving, tell the user: "Launch plan saved to `[RUN_DIR]/launch-plan.md`. [N] phases across [date range]."
