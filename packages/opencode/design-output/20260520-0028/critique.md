# Brand Design Critique: 上海创智学院 / Shanghai Innovation Institute

## Safety Checks
| Check | Status | Notes |
|-------|--------|-------|
| Text Hallucination | FAIL | Core lockups are mostly correct, but `west-bund-campus-glass-signage.png` contains misspelled/garbled small signage text, including “Intellgence” and likely “Presentaion Hall.” |
| Mockup Single-Object | FAIL | `west-bund-campus-glass-signage.png` is a multi-scene collage with exterior sign, floor directory, and hanging wayfinding signs in one frame. |
| Privacy Information | FAIL | `official-website-home-surface.png` shows non-placeholder contact details in the footer, including an email, phone number, and street-style address. |

## Anti-AI Slop Scan
| Sin | Status | Asset | Note |
|-----|--------|-------|------|
| Generic gradient | PASS | All | The system uses navy, white, graphite, and cyan rather than a generic purple-blue trust gradient. |
| Default tech accent | PASS | All | Cyan is brief-specified as Intelligence Cyan, not an arbitrary default indigo/violet accent. |
| Emoji icons | PASS | All | Icons are line/grid icons, not emoji; however some symbols drift into generic education icons. |
| Rounded card + left border | PASS | `official-website-home-surface.png` | The website uses cards, but not the canonical rounded-card plus colored-left-border AI template. |
| Invented metrics | FAIL | `official-website-home-surface.png`, `doctoral-program-recruitment-banner.png` | Visible claims such as “2020,” “300+,” “180+,” “60+,” “100+,” “10,000+,” and “50+” are not substantiated by the brief. |
| Filler copy | PASS | All | No lorem ipsum or “Feature One” style filler is visible. |
| Uniform sans-serif | PASS | All | Sans, mono, and one editorial serif display treatment appear; typography is differentiated enough. |

## Craft Notes
### Color
The palette is strategically aligned: midnight navy and cool white dominate, cyan acts as the primary signal, and violet is mostly restrained. The system is strongest in `intelligence-grid-system-board.png` and `research-category-module-system.png`. Accent discipline weakens on the website and event assets, where cyan appears in many simultaneous highlights and starts to feel like decoration rather than a scarce signal.

### Typography
The bilingual institutional typography is clear and credible. All-caps English labels are generally tracked appropriately, and mono labels support the engineering/research tone. Weaknesses: several assets carry too many tiny text tiers, some Chinese supporting text is too small to verify cleanly, and the whitepaper’s high-contrast serif title introduces a more traditional academic voice that is elegant but slightly separate from the core grid-tech system.

### Hierarchy
The best hierarchy appears in the recruitment banner and whitepaper cover: one strong headline, one visual system, then supporting modules. The website has more than five competing focal points—hero, stats, five cards, four lower panels, partner logos, footer—which creates dashboard density. The signage mockup fails the single-object rule and dilutes evaluation by showing three different physical applications at once.

## Dimension Scores

<DIM name="strategy_alignment" score="8">The assets strongly express a credible AI talent/research infrastructure brand through grid logic, institutional navy, bilingual systems, and Shanghai/West Bund context, though some generic education icons and invented scale metrics reduce strategic precision.</DIM>
<DIM name="logo_quality" score="7">The modular SII mark is coherent and scalable in principle, but the “S” construction can feel like a generic block-tech monogram and several assets use slightly different mark expressions.</DIM>
<DIM name="color_system" score="7">The briefed navy/cyan/white system is mostly disciplined and non-generic, but cyan is overused as a repeated decorative accent on dense assets.</DIM>
<DIM name="typography" score="7">The bilingual sans/mono system is credible and technically appropriate, with good label tracking, but small text density and occasional editorial-serif divergence weaken consistency.</DIM>
<DIM name="application_coherence" score="7">The identity feels largely unified across boards, web, reports, events, and signage, but the signage collage, invented contact data, and inconsistent mark variants prevent a clean system-level delivery.</DIM>

**Overall Score: 7.2/10** (average of 5 dimensions, rounded to 1 decimal)

## MUST_FIX Items

<MUST_FIX asset="west-bund-campus-glass-signage.png">
Regenerate as a single-object mockup only: one exterior glass/wall sign in one frame, with no collage panels, no separate floor directory, and no hanging wayfinding sequence.
</MUST_FIX>

<MUST_FIX asset="west-bund-campus-glass-signage.png">
Correct all hallucinated signage text. Replace misspellings such as “Intellgence” and “Presentaion Hall” with verified, simple strings or remove microcopy entirely.
</MUST_FIX>

<MUST_FIX asset="official-website-home-surface.png">
Remove all realistic privacy/contact data from the footer. Replace email, phone number, and address with placeholders such as “contact@example.edu,” “+86 00 0000 0000,” and “Shanghai, China.”
</MUST_FIX>

<MUST_FIX asset="official-website-home-surface.png; doctoral-program-recruitment-banner.png">
Remove or neutralize unverified metrics not present in the brief, including “300+,” “180+,” “60+,” “100+,” “10,000+,” and “50+.” Use non-numeric category labels or brief-supported facts only.
</MUST_FIX>

## Strengths
- The overall Intelligence Grid idea is consistently visible: modular grids, hub cells, path logic, mono labels, and cyan signal lines make the brand feel systematic rather than decorative.
- `bilingual-institution-lockup.png` is the strongest identity-system asset: the Chinese/English hierarchy, clear-space rules, monochrome versions, and minimum-size examples feel institution-ready.
- `research-category-module-system.png` successfully extends the core grid into labs, programs, tags, course codes, door plates, and digital modules.
- The navy/cyan palette avoids the most common AI gradient clichés while retaining a high-tech, public-institution tone.

## Top 3 Iteration Recommendations

### 1. Regenerate signage as one controlled physical application
**Issue:** The signage asset is a multi-object collage and contains hallucinated microcopy.
**Fix:** Show only one exterior entrance sign, keep text minimal, and avoid small wayfinding labels.
**Ready-to-use imagegen prompt:**
Create a single-object architectural signage mockup for Shanghai Innovation Institute. One exterior glass-and-stone campus entrance wall only, photographed straight-on at West Bund Shanghai, no collage, no extra panels, no floor directory, no hanging signs. Use the modular SII lettermark and bilingual lockup text exactly: “上海创智学院” and “Shanghai Innovation Institute”. Optional secondary line only: “West Bund AI Campus”. Midnight navy sign surface, cool white letters, restrained Intelligence Cyan edge light. No phone numbers, no email, no address, no extra room names, no misspelled microcopy.

### 2. Replace invented metrics with evidence-safe hierarchy
**Issue:** Website and recruitment banner use impressive but unsupported numeric claims.
**Fix:** Convert metrics into qualitative pillars or use only facts from the brief.
**Ready-to-use imagegen prompt:**
Regenerate the Shanghai Innovation Institute homepage hero and program modules using the same Intelligence Grid visual system. Remove all unverified metrics and numeric claims. Replace stat blocks with four evidence-safe pillars: “AI Talent Platform”, “Research Translation”, “Industry Collaboration”, “Open Innovation”. Keep bilingual Chinese/English labels, midnight navy background, cool white text, cyan used only for primary signals. Footer must use placeholder contact text only: “contact@example.edu”, “+86 00 0000 0000”, “Shanghai, China”. No real addresses, no real phone numbers, no real emails.

### 3. Tighten the mark system and reduce generic education symbolism
**Issue:** The modular SII system is promising, but some applications use inconsistent mark variants and generic education icons such as caps/books.
**Fix:** Use one canonical 8×8 SII mark and derive all icons from node/path/category logic instead of education clichés.
**Ready-to-use imagegen prompt:**
Create a revised brand system board for Shanghai Innovation Institute focused on one canonical 8×8 modular SII lettermark. Show the exact mark, clear-space, monochrome, small-size proof, and a derived icon family built only from grid cells, nodes, paths, hubs, datasets, models, compute, mentors, projects, and venture translation. Do not use graduation caps, books, lightbulbs, robots, brains, rockets, or emoji-like icons. Palette: #071A2D, #F6F9FC, #2B3440, #7E8A99, #00B8FF, with #6B5CFF used only once as a secondary category example.

## Verdict
REDESIGN
The strategic foundation is strong, but delivery is blocked by hard safety failures, invented metrics, and a multi-object mockup that must be regenerated before shipment.
