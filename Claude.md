# Next Maven — Claude Code Project Context

## About This Project
This project generates Instagram carousels for Next Maven 
(NextMaven.ai) — an AI & Growth training platform.

## Brand Knowledge (MUST READ before generating any content)
Always reference these files when writing or designing carousels:

- `brand/brand-foundation.md` — Brand identity, mission, values, positioning
- `brand/brand-color-system.json` — Brand colors and gradients
- `brand/brand-typography-system.json` — Typography rules
- `brand/brand-glossary.json` — Approved terms and banned words
- `brand/tov-marketing-general.md` — General marketing tone of voice
- `brand/tov-social-media.md` — Social media tone (⭐ most important for carousels)
- `brand/visual-social-media-design.md` — Visual design guidelines
- `brand/DESIGN.md` — UI design system

## Carousel Generation
Use the `/carousel` command to generate carousels.
See `.claude/commands/carousel.md` for the full pipeline.

## Brand Voice Summary (for quick reference)
- Practical authority — we've built the systems, we show not tell
- Empathetic clarity — simplify without dumbing down
- Action-forward — every post moves the reader toward doing
- NO hype words: "revolutionary" "game-changing" 「震撼」「革命」「最強」
- Cantonese on Threads/IG (Traditional Chinese, HK voice — NOT Mainland)
- English on LinkedIn
- NEVER code-mix EN/ZH in same sentence (except proper nouns like "AI", "ChatGPT")

---

## Visual Design System — NM Signature Carousel Style

NM carousels are **editorial-bold, not editorial-quiet**. Think: Dark Purple hook that stops the scroll, cream body slides that breathe, aquamarine as the signature highlight, full brand palette doing real work. Every carousel must feel unmistakably Next Maven.

### Brand Color Palette (Official)

| Role | Color | Hex | Usage |
|---|---|---|---|
| **Primary dark** | Dark Purple | `#2D1E2F` | Hook + CTA backgrounds, callout cards |
| **Signature accent** | Aquamarine | `#A7FAFF` | Inline highlights, pills, key numbers |
| **Background light** | Cream | `#F5EFE6` | Body slide backgrounds (custom warm neutral) |
| **Pure** | White | `#FFFFFF` | Dark-slide text, pure contrast |
| **Body text dark** | Grey | `#454252` | Body copy on cream slides |
| Secondary accent | Blue | `#65CBFF` | Data points, secondary highlights |
| Positive tint | Green | `#8AFFE9` | Positive data, "after" cards |
| Positive bg | Light Green | `#E0F5F1` | "New way" comparison card |
| Divider accent | Forest Green | `#6ABAAB` | Category labels, dividers, small caps |
| Dark depth | Dark Green | `#00635D` | Dark cards on cream, muted dark accent |
| Negative / contrast | Pastel Pink | `#FF899F` | "Old way" cards, warnings, negative data |
| Tertiary accent | Ocean Blue | `#69E6FF` | Optional rotation accent (use sparingly) |

**DO NOT use any hex not in this list.** No greys outside `#454252`. No off-whites outside `#F5EFE6`/`#FFFFFF`.

### Two-Theme System (the key to visual rhythm)

Every slide is either **DARK** or **LIGHT**. Mix them deliberately:

**DARK theme** (signature NM look):
- Background: `#2D1E2F` (Dark Purple)
- Headline: `#FFFFFF` (White)
- Label: `#A7FAFF` (Aquamarine) small caps
- Body text: `#E0F5F1` (Light Green) at 85% opacity
- Accent highlights: `#A7FAFF` background on marked words
- Divider: `#A7FAFF`

**LIGHT theme** (breathing room):
- Background: `#F5EFE6` (Cream)
- Headline: `#2D1E2F` (Dark Purple)
- Label: `#00635D` (Dark Green) small caps
- Body text: `#454252` (Grey)
- Accent highlights: `#A7FAFF` background on marked words
- Divider: `#6ABAAB`

### Mandatory Slide Rhythm Pattern

Never run more than 2 light slides in a row. Default pattern for a 6-slide carousel:

| Slide | Theme | Reason |
|---|---|---|
| 1 Hook | **DARK** | Stop the scroll — NM's signature purple+aqua moment |
| 2 Body | LIGHT | Breathing room, context |
| 3 Body | LIGHT | Content density |
| 4 Body | **DARK** | Mid-carousel re-engagement (usually the "key insight") |
| 5 Body | LIGHT | Final explanation |
| 6 CTA | **DARK** | Signature close |

For 5 slides: `DARK → LIGHT → DARK → LIGHT → DARK`  
For 7–8 slides: insert extra LIGHT slides in the 2–3 and 5–6 positions.

### Typography (Official Brand Fonts)

**English:**
- **Headlines & category labels: LEXEND DECA** (brand primary)
  - Hook headline: 96–108px, Weight 700 (Bold), tracking -1%
  - Body title: 72–80px, Weight 600 (SemiBold), tracking -1%
  - Category label: 26px, Weight 500 (Medium), tracking +8%, UPPERCASE
- **Body copy & pills & code: Inter** (secondary)
  - Body text: 34–38px, Weight 400, line-height 1.35
  - Pills: 28px, Weight 500
  - Code block: 30px, Weight 500 (mono-spaced alignment via padding)
- **Counter/swipe bar: Inter Medium, 24px, tracking +5%**

**Chinese (Traditional — Cantonese HK voice):**
- Headlines & labels: **寒蝉端黑体 Heavy** (ChillDuanSans_Heavy)
  - Hook: 88–96px (Chinese renders visually heavier, size down ~10%)
  - Body title: 64–72px
- Body: 寒蝉端黑体 Medium / Regular, 32–36px
- Counter/handle: 寒蝉端黑体 Light, 24px

### Strict Layout Grid (unchanged structurally)

```
┌─────────────────────────────────┐  ← 1080×1080
│  BRAND NAME          NN / TT   │  ← 80px top bar
│─────────────────────────────────│
│                                 │
│  CATEGORY LABEL                 │  ← 60px below bar
│                                 │
│  HEADLINE WITH                  │
│  *ACCENT WORDS*                 │  ← LEXEND DECA Bold, fills width
│                                 │
│  ━━━━━                          │  ← 80px accent divider bar (not short line)
│                                 │
│  Content block(s)               │
│                                 │
│─────────────────────────────────│
│  SWIPE →           N / TOTAL   │  ← 80px bottom bar
└─────────────────────────────────┘
```

**Non-negotiables:**
1. **96px left/right padding** (was 72 — tighter felt cramped)
2. **Divider bar is a solid rectangle**, 80px × 6px, aquamarine on dark / forest-green on light
3. Top + bottom bars have 1px hairline separator (`#FFFFFF` at 15% on dark, `#2D1E2F` at 10% on light)
4. Counter format: `01 / 06` (zero-padded, always two digits)
5. SWIPE indicator: `SWIPE →` (EN) or `左滑 →` (ZH)
6. Headline max 4 lines. If it overflows, shorten the copy — never shrink the type.

### Content Block Styling (updated for dark/light themes)

#### `pills` — Tool tags
- **On LIGHT slides**: White pill, 2px Dark Purple border, Dark Purple text. Active pill = Aquamarine fill, Dark Purple text.
- **On DARK slides**: Dark purple pill, 2px Aquamarine border (50% opacity), White text. Active pill = Aquamarine fill, Dark Purple text.
- Pill padding: 20px horizontal, 14px vertical. Border radius: fully pill-shaped (height/2).
- Gap between pills: 16px

#### `comparison` — Old vs New
- **On LIGHT slides**: Pink card `#FF899F` at 25% opacity over cream + Mint card `#E0F5F1`
- **On DARK slides**: Pink card `#FF899F` at 20% opacity + Green card `#8AFFE9` at 15% opacity
- Each card: 32px radius, 40px padding, label in darker tint of card color, body text in theme default
- Stack vertically with 24px gap

#### `card` — Dark callout (only on LIGHT slides)
- Background: Dark Purple `#2D1E2F`
- Label: Aquamarine `#A7FAFF`, LEXEND DECA Medium 22px, tracking +8%
- Text: White, Inter Regular 36px
- Padding: 48px, Radius: 32px

#### `card` variant — Light callout (only on DARK slides)
- Background: Aquamarine `#A7FAFF` (10% opacity) + 1px Aquamarine border
- Label: Aquamarine, LEXEND DECA Medium 22px
- Text: White, Inter Regular 36px

#### `code_block` — macOS-style
- Background: `#1E1318` on BOTH themes (deeper than Dark Purple for contrast)
- Traffic dots: actual `#FF5F57` / `#FEBC2E` / `#28C840`
- Keyword color: Aquamarine `#A7FAFF`, Inter Medium
- Rest color: Light Green `#E0F5F1`, Inter Regular
- Padding: 48px, Radius: 24px
- Line gap: 16px

#### `image` — Product screenshots only
- Rounded corners: 32px radius
- 1px border: `#FFFFFF` at 20% on dark slides / `#2D1E2F` at 10% on light slides
- Never fill full width — leave 96px padding consistent with text

### Accent Highlight Rendering

Marked words (`*like this*`) get a **filled aquamarine rounded rectangle behind them** (not underline, not color change):
- Rectangle: `#A7FAFF` solid fill
- Radius: 8px  
- Padding: 8px horizontal, 4px vertical above/below letter bounds
- Text on top stays `#2D1E2F` (Dark Purple) on BOTH themes — so it pops on dark slides too
- Max 3 highlighted phrases per slide. 1–2 is more powerful.

### Decorative Details (Instagram-worthy polish)

Add these small elements to make slides feel *designed*, not templated:

1. **Slide-number badge** (top-right of top bar, optional on hook/CTA): Aquamarine small circle with slide number inside — adds editorial feel
2. **Arrow glyph** (→) after key phrases when transitioning ideas — use Inter Medium, aquamarine on dark / forest-green on light
3. **Accent dot rows** under category labels: three 8px circles, aquamarine, 12px gap — signals "this is a section"
4. **Oversized opening quote mark** (optional) on hook slides if headline is a quote — 200px, aquamarine 40% opacity, behind text

---

## Image Policy — Specific and Relevant, or Skip It

**Golden rule: A well-designed text-only slide beats a mediocre stock image every time.**

### When to use images
Only use `image` field when the slide directly features a specific named product/tool and you can find its actual UI screenshot or official logo.

### How to search for product images
When a specific tool is mentioned (e.g. ChatGPT, Notion, Cursor, n8n):

1. **First: official UI screenshot**
   - Search: `"[product name]" official screenshot site:[official-domain]`
   - Known domains: openai.com (ChatGPT), anthropic.com (Claude), cursor.com, notion.so, n8n.io, make.com, zapier.com, perplexity.ai, gemini.google.com
   
2. **Second: dark mode screenshot**
   - Search: `"[product name]" dark mode UI screenshot`
   
3. **Third: transparent logo**
   - Search: `"[product name]" logo transparent PNG official`

4. **If nothing good found → use `pills` instead.**
   Tool pill tags look professional and load reliably. Never settle for an irrelevant image.

### Images to NEVER use
- Stock photos with people (handshakes, laptops, headshots)
- Abstract "AI" imagery (circuit boards, glowing brains, robot hands)
- White-background images on concept slides — they clash with cream
- Low-resolution (<1080px) or watermarked images (Getty, Shutterstock)
- Pinterest sources (unclear copyright)
- Any image that isn't directly, obviously related to the slide topic

### Image quality requirements
- Minimum 1080px on shortest side
- Prefer PNG (especially for logos/UI — cleaner edges)
- Cream/light or dark backgrounds both work — avoid bright neon backgrounds
- No text overlay that duplicates what's already on the slide

---

## Config.json Notes

### Do NOT add `"colors"` override
The render script already uses the correct NM editorial cream theme by default. Do not add a colors block unless the user explicitly asks for a theme variant.

### Accent highlighting in copy
Mark 1–3 key words per slide with `*asterisks*`. Marked words get an aquamarine background highlight drawn behind them. Over-using highlights destroys the effect — use sparingly on the single most important word/phrase per slide.

### Label field (category tag above headline)
Always include a `"label"` on every slide. It provides context and creates visual rhythm across the carousel. Examples:
- Hook: `"JUST LAUNCHED"` / `"WHY THIS MATTERS"` / `"THE PROBLEM"`
- Body: `"WHAT IS IT"` / `"HOW IT WORKS"` / `"OLD WAY VS NEW WAY"` / `"KEY FEATURES"`
- CTA: no label needed
