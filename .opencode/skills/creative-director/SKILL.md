---
name: creative-director
description: AI creative director with recursive self-assessment. Uses SIT, TRIZ, SCAMPER, Synectics, and Bisociation methodologies to generate and evaluate creative directions for brand design briefs. Run before the designer to stress-test visual direction options.
triggers:
  - creative director
  - creative direction
  - campaign concept
  - stress test the brief
  - 创意方向
  - 创意评审
---

# Creative Director Skill

Run this skill after the planner produces `brief.md` and before the designer starts asset generation. Its job is to pressure-test the visual direction and generate 2-3 genuinely differentiated creative concepts — not variations of the same idea.

---

## Phase 1: Brief Stress-Test

Read `{OUTPUT_DIR}/brief.md`. For each of these questions, answer honestly (not diplomatically):

1. **Predictability test** — If you described this brief to a designer and said "make something for this," what would they make? That is the default. The default is what we must avoid.
2. **Category convention test** — What does every brand in this category look like? (Tech = dark/gradient/sans. Education = blue/crest/serif. Food = warm/handwritten/rustic.) Does the brief push against or reinforce the convention?
3. **Cultural specificity test** — How many elements in Section 5 (Cultural & Visual DNA) are *specific to this subject* vs. generic category attributes? Anything that could describe 50 other brands is not a differentiator.
4. **Tension test** — Does the brief have an interesting contradiction or tension to explore? (e.g., ancient institution using cutting-edge research; premium brand with democratic access; playful product in a serious industry.) Tension = creative energy.

Output: a 3-sentence diagnosis of the brief's creative risk and opportunity.

---

## Phase 2: Methodology Application

Apply **two** of the following methodologies to generate divergent directions. Choose the two most relevant to the brief's tension.

### SCAMPER
Systematically challenge each element of the expected visual identity:
- **Substitute**: Replace one expected element with something unexpected. What if the logo used [X] instead of [expected form]?
- **Combine**: What two normally separate visual languages could be merged? (e.g., scientific diagram + folk art)
- **Adapt**: What visual system from a different industry could be adapted? (e.g., wayfinding system for a school; trading card aesthetics for a product)
- **Modify/Magnify**: What if one element was exaggerated to the point of becoming the entire identity?
- **Put to other uses**: What non-brand artifact could become the brand's visual language? (e.g., a ledger, a field guide, a score sheet)
- **Eliminate**: What expected brand element can be removed entirely? What if there's no logo mark — only typography?
- **Reverse**: What if the brand identity worked opposite to category convention?

### SIT (Systematic Inventive Thinking)
Apply these five patterns to the visual identity problem:
- **Subtraction**: Remove a key element everyone else has. What remains is the identity.
- **Multiplication**: Take one existing element and multiply it. The repetition becomes the system.
- **Division**: Split a standard element into parts and rearrange them.
- **Task unification**: Give an existing element a new, additional function.
- **Attribute dependency**: Make visual properties vary based on brand data (e.g., color shifts with season, type weight shifts with message urgency).

### Bisociation (Koestler)
Find two unrelated domains and force a creative collision:
- Domain A: the brand's core activity/context (from brief Section 2)
- Domain B: a completely unrelated field (choose one that has rich visual vocabulary: astronomy, botany, cartography, musical notation, textile weaving, surgical instruments, Japanese woodblock printing, etc.)
- Collision: what visual language emerges from treating Domain A *as if it were* Domain B?

### Synectics
Use analogical thinking:
- **Direct analogy**: What in nature does this brand resemble in function? What does that look like visually?
- **Personal analogy**: If the brand were a person, what would they wear, carry, how would they move?
- **Symbolic analogy**: What paradoxical phrase captures the brand's essence? (e.g., "organized chaos", "warm precision", "ancient future") What visual system embodies that paradox?

---

## Phase 3: Generate 3 Creative Concepts

Based on your Phase 1 diagnosis and Phase 2 methodology work, propose **3 genuinely different creative concepts**. Each must:
- Have a clear strategic rationale (not just "it looks different")
- Be traceable to brief evidence (Section 5, 7, or the tension identified in Phase 1)
- Be differentiated from the other two in *approach*, not just in color or typeface

For each concept:

```
### Concept [N]: [Name — 2-4 words]

**Strategic idea in one sentence:**
[What is the brand saying through this visual approach?]

**Visual language:**
[What does it look like? Be specific: describe form, texture, motion language, typographic register, color temperature, compositional logic]

**Key differentiator from category defaults:**
[What convention does this break and why is that the right move?]

**Methodology source:**
[Which Phase 2 method generated this, and how]

**Risk:**
[What could go wrong with this approach]

**Recommended for:**
[What type of client/context this works best in]
```

---

## Phase 4: Recursive Self-Assessment

For each concept, evaluate it against 3 axes calibrated to award-level work (Cannes / D&AD / HumanKind criteria):

| Axis | Question | Score 1-10 |
|------|----------|-----------|
| **Craft** | Would a senior designer at a top studio feel proud of this direction? | |
| **Cultural truth** | Does this feel earned — rooted in something real about the brand — or imposed? | |
| **Distinctiveness** | Could this be mistaken for another brand in 3 years? | |

Minimum thresholds for a concept to proceed: Craft ≥6, Cultural truth ≥7, Distinctiveness ≥6.

Eliminate any concept below threshold. If all three fail, run Phase 2 again with different methodologies.

---

## Phase 5: Recommendation

Output a final recommendation:

```
## Creative Direction Recommendation

**Recommended concept:** [Name]
**Rationale:** [2-3 sentences on why this is the strongest]

**For the designer:**
- Visual direction to develop: [specific description]
- Key motifs to carry forward: [list]
- What to avoid: [specific traps this brand risks falling into]

**Alternative concept:** [Name] — pursue if [condition]

**Rejected concept:** [Name] — reason: [why it failed the self-assessment]
```

Save to `{OUTPUT_DIR}/creative-direction.md`.
