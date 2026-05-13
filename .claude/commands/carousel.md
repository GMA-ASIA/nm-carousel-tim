# Instagram Carousel

Generate a branded Instagram carousel. Request: $ARGUMENTS

---

## Input Parsing

Parse `$ARGUMENTS` to determine the input type:

- **Starts with `zh `** → set `language = "zh"`, strip the prefix, write in Traditional Chinese (Cantonese voice)
- **YouTube URL** (contains `youtube.com` or `youtu.be`): Pull transcript, extract key insights
- **Topic string** (anything else): Research the topic, write original content

If no arguments, ask the user what topic and language they want a carousel about.

---

## Pipeline

Run stages 1-3 automatically, then STOP for user approval before rendering.

### 1. INPUT

**If YouTube URL:**
- Extract the video ID from the URL
- Pull transcript using `youtube-transcript-api`:
  ```bash
  cd "$CLAUDE_PROJECT_DIR" && .venv/bin/python3 -c "
  from youtube_transcript_api import YouTubeTranscriptApi
  ytt = YouTubeTranscriptApi()
  transcript = ytt.fetch('<VIDEO_ID>')
  text = ' '.join([s.text for s in transcript.snippets])
  print(text)
  "
  ```
- Extract the video title and transcript text

**If topic string:**
- Use the topic directly as the content brief

### 2. RESEARCH + AUTONOMOUS IMAGE SOURCING

#### 2a — Slide plan

Design 5–8 slides following this structure AND rhythm:

| Slide | Type | Theme | Purpose |
|---|---|---|---|
| 1 | `hook` | **DARK** | Bold claim, category label, subtitle, optional pills |
| 2 | `body` | LIGHT | First key idea — context or definition |
| 3 | `body` | LIGHT or DARK | Second key idea |
| 4 | `body` | **DARK** | Mid-carousel anchor (strongest insight or comparison) |
| 5 | `body` | LIGHT | Supporting detail or example |
| N | `cta` | **DARK** | Headshot + name + follow CTA |

**Rhythm rule: never place more than 2 LIGHT slides in a row. Hook and CTA are always DARK.**

**Per-slide content rules:**
- Every slide MUST have a `label` (category tag, e.g. `"WHAT IS IT"`, `"OLD WAY VS NEW WAY"`)
- Every slide MUST declare its `"theme": "dark"` or `"theme": "light"` in config
- Every body/hook slide MUST have a `title` or strong `text` block
- Mix 2 content block types max per body slide
- Use `*asterisks*` around **1–2** key words per slide (3 is the absolute max)
- The strongest slides are sparse — label + headline + one content block

**Content block selection guide:** (unchanged — pills, comparison, card, code_block, image, bullets)**Step 2b — Automatic Image Planning:**

For each slide, decide the image type based on content:

| Slide Content | Auto-Select Image Type |
|---|---|
| Tool mention | Official product screenshot or logo |
| Workflow/process | Diagram, flowchart, or UI screenshot |
| Comparison | Side-by-side product logos |
| Stat/data point | Relevant abstract/tech imagery or chart |
| Concept/abstract idea | Unsplash-style clean tech photo |
| Person/team mention | Avoid (use text-only slide instead) |
| Quote/testimonial | Text-only (no image) |
| News/announcement | Official announcement hero image |

**Step 2c — Autonomous Search Strategy:**

For each image needed, execute this search cascade:

1. **First attempt — Official sources:**
   ```
   WebSearch: "<product name> official screenshot site:<likely-official-domain>"
   ```
   Known official domains for common AI tools:
   - ChatGPT → openai.com
   - Claude → anthropic.com / claude.com
   - Gemini → deepmind.google / gemini.google.com
   - Cursor → cursor.com
   - n8n → n8n.io
   - Make → make.com
   - Zapier → zapier.com
   - Notion → notion.so
   - Perplexity → perplexity.ai
   - (extend this list based on topic)

2. **Second attempt — Press kits & brand assets:**
   ```
   WebSearch: "<product name> press kit OR brand assets OR media kit"
   ```

3. **Third attempt — Free stock sources:**
   ```
   WebSearch: "<concept> site:unsplash.com"
   WebSearch: "<concept> site:pexels.com"
   ```

4. **Fourth attempt — General web with quality filter:**
   ```
   WebSearch: "<topic> high resolution image"
   ```
   Then filter results for: official domains, .png/.jpg URLs, minimum 1080px indicators

**Step 2d — Image Evaluation Checklist:**

Before downloading, verify each image:
- [ ] Source is reputable (official site > stock photo > random blog)
- [ ] Resolution indicator suggests ≥1080px
- [ ] Not watermarked (Getty, Shutterstock = skip)
- [ ] Not AI-generated deepfake or fake screenshot
- [ ] Matches the slide's message (relevant, not just decorative)

**Step 2e — Download & Log:**

Download each selected image:
```bash
curl -L -o "carousels/workspace/<name>/reference/<descriptive-name>.jpg" "<image-url>"
```

Create `reference/SOURCES.md` logging:
```markdown
# Image Sources for <Carousel Name>

## slide_2_chatgpt-ui.png
- Source: https://openai.com/chatgpt
- License: Official product screenshot (fair use, editorial)
- Downloaded: 2026-04-21

## slide_3_workflow-diagram.png
- Source: https://unsplash.com/photos/xyz
- Photographer: @username
- License: Unsplash Free License
- Downloaded: 2026-04-21
```

**Step 2f — Fallback Strategy:**

If no suitable image found after all 4 search attempts:
1. Note it in the slide plan: "⚠️ No image found — using text-only layout"
2. Suggest the user provide one, OR
3. Generate a stronger text-only slide with bold typography
4. NEVER use a low-quality or irrelevant image just to fill space

**Step 2g — Quality Standards (Non-Negotiable):**

- Minimum 1080px on shortest side
- Prefer PNG for UI/logos, JPG for photos
- Aquamarine/dark color palette preferred (matches Next Maven brand)
- Clean, tech-forward aesthetic (matches `brand/visual-social-media-design.md`)
- No clichéd stock photos (handshakes, people pointing at screens, etc.)

### 3. WRITE + PREVIEW

Structure the content into carousel slides, then present a **text preview** for the user to approve before rendering.

**Slide 1 (hook):** Bold, attention-grabbing statement. 1-2 sentences max. **Must always have an image** (YouTube thumbnail, product screenshot, or relevant hero image). Optional subtitle for secondary context.

**Slides 2-7 (body):** Mix of:
- Text-only slides for key statements
- Bullet slides for lists/comparisons (max 4 bullets per slide)
- Image slides for visual evidence
- Use section titles to create structure
- Use `*asterisks*` around keywords to highlight in accent color

**Last slide (CTA):** Call to action with `button_text` (e.g., "Follow for more")

**Rules:**
- 5-8 slides total (including hook and CTA)
- Hook slide must always have an image (never text-only)
- Every 2nd-3rd slide should have an image
- Keep text concise - people swipe, not read
- Max ~150 characters per text block
- Max 4 bullets per slide
- Body text renders in bold (Inter Bold) - write accordingly (short, punchy lines)

**>>> STOP HERE. Present the slide plan to the user as a numbered list:**

```
Slide 1 (hook): "Hook text here"
  - Image: description of what image will be used
  - Annotation: "annotation text"

Slide 2 (body): Title: "Section Title"
  - Text: "Body text here"
  - Bullets: ["bullet 1", "bullet 2"]
  - Image: description
  ...

Slide N (cta): "CTA text"
  - Button: "Follow for more"
```

Ask: **"Here's the slide plan. Want me to change anything before I render?"**

Wait for the user to approve or request changes. Iterate on the text plan until they're happy.

### 4. CONFIG + IMAGES

After user approves the slide plan:

- Create the workspace directory: `carousels/workspace/<carousel-name>/`
- Download any reference images needed
- Generate `config.json` (see Config Schema below)

### 5. RENDER

```bash
cd "$CLAUDE_PROJECT_DIR"
python3 carousels/render.py "carousels/workspace/<carousel-name>"
```

### 6. REVIEW

After rendering, read each slide PNG and display them to the user.

Present a summary:
- Total slides
- Slide-by-slide breakdown (type, has image, text preview)
- Ask: "Happy with this? Any changes needed?"

**If changes requested:**
- Edit the config.json as needed
- Add/swap/regenerate images in reference/ if needed
- Re-run the render script
- Show updated slides

---

## Config Schema

File: `workspace/<carousel-name>/config.json`

```json
{
  "title": "Carousel Title",
  "language": "en",
  "profile": {
    "display_name": "NEXT MAVEN",
    "handle": "@nextmaven.ai"
  },
  "slides": [
    {
      "type": "hook",
      "theme": "dark",
      "label": "JUST LAUNCHED",
      "text": "Claude just made automation *stupid simple*.",
      "subtitle": "It turns Claude into a full automation platform — scheduling, webhooks, API triggers.",
      "pills": ["n8n", "Make.com", "Zapier", "All of them"],
      "pills_active": 3
    },
    {
      "type": "body",
      "theme": "light",
      "label": "WHAT IS IT",
      "title": "Routines = Claude running your workflows *automatically*.",
      "text": "No dragging nodes. No mapping variables. No credentials to manage.",
      "code_block": [
        ["Schedule", "run at 5:10am every day"],
        ["Webhook", "fires when something happens"],
        ["API call", "trigger from any external system"]
      ]
    },
    {
      "type": "body",
      "theme": "light",
      "label": "OLD WAY VS NEW WAY",
      "title": "The drag-and-drop era is *over*.",
      "comparison": {
        "old": { "label": "OLD WAY", "text": "Drag nodes. Map variables. Fix broken connections. 2–3 hours per workflow." },
        "new": { "label": "NEW WAY", "text": "Write plain English. Set a trigger. Done in 2 minutes." }
      }
    },
    {
      "type": "body",
      "theme": "dark",
      "label": "KEY INSIGHT",
      "title": "Claude is now the *logic layer*.",
      "text": "Same event in. Same output out. But now a reasoning model sits between them — not a brittle chain of nodes."
    },
    {
      "type": "body",
      "theme": "light",
      "label": "WHO SHOULD CARE",
      "title": "If you build automations, *this matters*.",
      "bullets": [
        "Solopreneurs replacing $200/mo SaaS stacks",
        "Agencies shipping client workflows in hours",
        "PMs who couldn't touch n8n without a dev"
      ]
    },
    {
      "type": "cta",
      "theme": "dark",
      "text": "Follow for more AI & automation drops",
      "button_text": "Follow @nextmaven.ai"
    }
  ]
}
```

### Slide Types

| Type | Purpose | Fields |
|------|---------|--------|
| `hook` | First slide, grabs attention | `text` (required), `image` (required), `subtitle` (optional), `annotation` (optional) |
| `body` | Content slides | `text`, `title`, `bullets`, `image`, `annotation` (all optional, at least one required) |
| `cta` | Last slide, call to action | `text` (required), `button_text` (optional) |

### Field Notes

- `language`: `"en"` (default) or `"zh"` — switches font stack to Noto Sans HK for Cantonese; footer text also switches to localized copy
- `image`: filename relative to `reference/` directory, or `asset:<filename>` to load from the shared `assets/` folder
- `title`: rendered uppercase in Bebas Neue with accent underline bar (English only — `zh` mode keeps original case)
- `text`: supports `*accent words*` syntax for colored highlighting
- `subtitle`: hook slides only, rendered smaller in muted color below the main text
- `bullets`: array of strings with `*accent*` support, rendered with colored dots
- `button_text`: renders a gradient pill button on CTA slide (left-to-right accent color gradient)
- `annotation`: handwritten Caveat text with a curved arrow pointing down toward content

---

## Voice & Tone

When writing carousel content, aim for:
- Direct, confident, no fluff
- Data-driven when possible (specific numbers > vague claims)
- Slightly provocative hooks that challenge assumptions
- Educational but not preachy
- Short sentences, clear structure

Customize this section to match your own brand voice.