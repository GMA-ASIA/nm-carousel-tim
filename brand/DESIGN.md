DESIGN.md — NextMaven.ai UI Design System
Version: 1.0.0 · Last updated: 2026-04-09
Brand essence: "We're authoritative, but not bossy. We're insightful, but not boring."

Table of Contents
Visual Theme & Atmosphere
Color Palette & Roles
Typography Rules
Component Stylings
Layout Principles
Depth & Elevation
Do's and Don'ts
Responsive Behavior
Agent Prompt Guide
1. Visual Theme & Atmosphere
Design Philosophy
NextMaven's visual identity draws from the cosmic metaphor — the mysterious expanse of dark space illuminated by vibrant, energetic aquamarine light. The brand personality is 70% Magician, 30% Sage: transformative, insightful, and forward-looking.

Atmosphere Keywords
Dimension	Description
Mood	Futuristic, energetic, trustworthy, approachable
Feeling	Like stepping into a cutting-edge AI lab that still feels human and warm
Contrast Model	Deep cosmic dark × Electric aquamarine glow
Personality	Conversational, genuine, clear, simple, consistent, a bit of dry humor, never snobbish
Information Density
High-clarity, medium-density — Every element must earn its space
Prefer progressive disclosure over overwhelming upfront data
Use generous whitespace to let aquamarine accents breathe against dark surfaces
Content-to-chrome ratio should always favor content
Visual Metaphor
Dark Purple (cosmos)  →  the foundation, depth, trust
Aquamarine (energy)   →  the spark, action, technology
Pure White (stars)    →  clarity, illumination, readability
2. Color Palette & Roles
2.1 Primary Colors
Semantic Name	Hex	RGB	Role
Cosmos (Dark Purple Deep)	#2D1E2F	45, 30, 47	Primary background (dark mode), deepest surface
Cosmos Light	#454252	69, 66, 82	Secondary background, card surfaces, nav bars
Aquamarine	#68E6FD	104, 230, 253	Primary brand accent, CTAs, active states, links
Aquamarine Bright	#8AFFE9	138, 255, 233	Hover states, highlights, success glow
Aquamarine Muted	#6ABAAB	106, 186, 171	Secondary text on dark, subtle accents, borders
Ghost White	#E0F5F1	224, 245, 241	Light background tint, card bg (light mode)
Pure White	#FFFFFF	255, 255, 255	Text on dark, light-mode background, clarity
2.2 Extended Aquamarine Tints
Semantic Name	Hex	RGB	Role
Sky Aqua	#65CBFF	101, 203, 255	Info indicators, secondary links
Frost Aqua	#A7FAFF	167, 250, 255	Badges, tags, soft highlights
2.3 Secondary / Accent Colors (use sparingly)
Semantic Name	Hex	RGB	Role
Deep Teal	#00635D	0, 99, 93	Success states, positive indicators, verified
Coral Red	#FE5F55	254, 95, 98	Error, destructive actions, urgent alerts
Electric Violet	#8C49FF	140, 73, 255	Premium/pro badges, special features
Neon Cyan	#69E6FF	105, 230, 255	Interactive highlights, data visualization accent
Soft Blue	#60AFFF	96, 175, 255	Information callouts, secondary icons
Blush Pink	#FF899F	255, 137, 159	Warnings (soft), notifications, warmth accents
2.4 Semantic Color Mapping
--color-bg-primary:       #2D1E2F      /* Dark mode base */
--color-bg-secondary:     #454252      /* Dark mode elevated surface */
--color-bg-light:         #FFFFFF      /* Light mode base */
--color-bg-light-tint:    #E0F5F1      /* Light mode subtle surface */

--color-text-primary:     #FFFFFF      /* On dark surfaces */
--color-text-secondary:   #6ABAAB      /* On dark surfaces, muted */
--color-text-dark:        #2D1E2F      /* On light surfaces */
--color-text-dark-muted:  #454252      /* On light surfaces, muted */

--color-accent:           #68E6FD      /* Primary interactive */
--color-accent-hover:     #8AFFE9      /* Hover / focus glow */
--color-accent-muted:     #6ABAAB      /* Disabled accent, borders */

--color-success:          #00635D
--color-error:            #FE5F55
--color-warning:          #FF899F
--color-info:             #60AFFF
--color-premium:          #8C49FF
2.5 Gradient Definitions
Name	Value	Usage
Gradient Light	linear-gradient(135deg, #454252 0%, #68E6FD 100%)	Light-to-dark hero sections, cards on dark bg
Gradient Dark	linear-gradient(135deg, #68E6FD 0%, #E0F5F1 100%)	CTA buttons, feature highlights
Gradient Glow	linear-gradient(180deg, #8AFFE9 0%, #68E6FD 100%)	Icon fills, decorative elements
Gradient Cosmic	linear-gradient(135deg, #2D1E2F 0%, #454252 100%)	Dark surface variation, modal overlays
3. Typography Rules
3.1 Font Families
Priority	Language	Font Family	Fallback Stack
Primary	English	Lexend Deca	'Lexend Deca', 'Spline Sans', system-ui, -apple-system, sans-serif
Secondary	English	Spline Sans	'Spline Sans', 'Lexend Deca', sans-serif
Primary	Chinese	寒蝉端黑体 (HanChan)	'HanChan', 'Noto Sans HK', 'Noto Sans TC', sans-serif
Fallback	Chinese	Noto Sans HK	'Noto Sans HK', 'Noto Sans TC', 'PingFang TC', sans-serif
Design principle: Always maintain sans-serif style typeface across all contexts.

3.2 Type Scale
Token	Font	Weight	Size (desktop)	Size (mobile)	Line Height	Letter Spacing	Usage
h1	Lexend Deca	Black (900)	38px / 2.375rem	28px / 1.75rem	1.15	-0.02em	Page titles, hero headlines
h2	Lexend Deca	Bold (700)	32px / 2rem	24px / 1.5rem	1.2	-0.015em	Section headings
h3	Lexend Deca	SemiBold (600)	24px / 1.5rem	20px / 1.25rem	1.3	-0.01em	Subsection headings, card titles
h4	Lexend Deca	Medium (500)	20px / 1.25rem	18px / 1.125rem	1.35	0	Minor headings, labels
body	Lexend Deca	Regular (400)	16px / 1rem	16px / 1rem	1.6	0	Body copy, descriptions
body-sm	Lexend Deca	Regular (400)	14px / 0.875rem	14px / 0.875rem	1.5	0.005em	Captions, helper text
caption	Lexend Deca	Regular (400)	12px / 0.75rem	12px / 0.75rem	1.4	0.01em	Footnotes, timestamps, terms
button	Lexend Deca	SemiBold (600)	16px / 1rem	16px / 1rem	1.0	0.02em	Button labels
button-sm	Lexend Deca	Medium (500)	14px / 0.875rem	14px / 0.875rem	1.0	0.02em	Small button labels
overline	Lexend Deca	Medium (500)	12px / 0.75rem	11px / 0.6875rem	1.4	0.08em	Section labels, uppercase tags
3.3 Chinese Typography Scale
Token	Font	Weight	Size (desktop)	Size (mobile)	Usage
zh-h1	寒蝉端黑体	Regular	36px	26px	Chinese hero titles
zh-h2	寒蝉端黑体	Regular	30px	22px	Chinese section headings
zh-body	寒蝉端黑体	Regular	16px	16px	Chinese body copy
Note: Chinese typeface uses Regular weight only; visual hierarchy is achieved through size and color contrast rather than weight.

3.4 Typography Rules
Minimum body text size: 16px (never go below 12px for any UI text)
Maximum line width: 72ch for body text, 20ch for headlines
Paragraph spacing: 1.5× the body font size
No underlines except on text links inside body copy
ALL CAPS only for overline token; never for body or headings
4. Component Stylings
4.1 Buttons
Primary Button (CTA)
Background:    linear-gradient(135deg, #68E6FD 0%, #8AFFE9 100%)
Text:          #2D1E2F
Font:          button token (Lexend Deca SemiBold 16px)
Padding:       12px 32px
Border-radius: 8px
Border:        none
State	Style
Default	Gradient aquamarine bg, dark text
Hover	Brightness +10%, box-shadow: 0 4px 20px rgba(104, 230, 253, 0.4)
Active / Pressed	Brightness −5%, shadow reduced to 0 2px 8px rgba(104, 230, 253, 0.3)
Focus	2px outline #8AFFE9, offset 2px
Disabled	Opacity 0.4, cursor not-allowed, no shadow
Loading	Text replaced with spinner, maintain width
Secondary Button
Background:    transparent
Text:          #68E6FD (dark mode) / #2D1E2F (light mode)
Border:        1.5px solid #68E6FD (dark) / #454252 (light)
Padding:       12px 32px
Border-radius: 8px
State	Style
Default	Transparent bg, aquamarine border + text
Hover	Background rgba(104, 230, 253, 0.1), border stays
Active	Background rgba(104, 230, 253, 0.2)
Focus	2px outline #8AFFE9, offset 2px
Disabled	Opacity 0.4
Ghost Button (Tertiary)
Background:    transparent
Text:          #6ABAAB (dark mode) / #454252 (light mode)
Border:        none
Padding:       12px 24px
Border-radius: 8px
State	Style
Default	Text only, no border
Hover	Background rgba(104, 230, 253, 0.08), text color becomes #68E6FD
Active	Background rgba(104, 230, 253, 0.15)
Destructive Button
Background:    #FE5F55
Text:          #FFFFFF
Border-radius: 8px
4.2 Cards
Standard Card
Background (dark):  #454252
Background (light): #FFFFFF
Border-radius:      12px
Padding:            24px
Border:             1px solid rgba(104, 230, 253, 0.1)   /* dark mode */
                    1px solid rgba(69, 66, 82, 0.12)     /* light mode */
Shadow:             elevation-1 (see §6)
State	Style
Default	Subtle border, low shadow
Hover	border-color: rgba(104, 230, 253, 0.3), elevation-2 shadow, translateY(-2px)
Active / Selected	border-color: #68E6FD, left border 3px accent, elevation-2
Disabled	Opacity 0.5, no hover effects
Feature / Premium Card
Background:     linear-gradient(135deg, #454252 0%, #2D1E2F 100%)
Border:         1px solid rgba(140, 73, 255, 0.3)
Accent:         Small #8C49FF badge in top-right corner
4.3 Input Fields
Text Input
Background (dark):  rgba(45, 30, 47, 0.6)
Background (light): #FFFFFF
Border:             1.5px solid #6ABAAB (dark) / 1.5px solid #C0C0C0 (light)
Border-radius:      8px
Padding:            12px 16px
Font:               body token
Text color:         #FFFFFF (dark) / #2D1E2F (light)
Placeholder color:  #6ABAAB (dark) / #999 (light)
State	Style
Default	Muted border
Hover	Border color #68E6FD at 60% opacity
Focus	Border #68E6FD, box-shadow: 0 0 0 3px rgba(104, 230, 253, 0.2)
Error	Border #FE5F55, box-shadow: 0 0 0 3px rgba(254, 95, 98, 0.15), error text below in #FE5F55
Success	Border #00635D, check icon in suffix
Disabled	Opacity 0.4, background slightly darker
Label
Font:     body-sm token, SemiBold
Color:    #E0F5F1 (dark) / #454252 (light)
Margin:   0 0 6px 0
4.4 Navigation Bar
Top Navigation
Background (dark):  rgba(45, 30, 47, 0.85) + backdrop-filter: blur(16px)
Background (light): rgba(255, 255, 255, 0.9) + backdrop-filter: blur(16px)
Height:             64px
Padding:            0 24px
Border-bottom:      1px solid rgba(104, 230, 253, 0.1)
Element	Style
Logo	Left-aligned, max-height 32px
Nav links	body token, color #E0F5F1 (dark) / #454252 (light)
Active link	Color #68E6FD, underline 2px #68E6FD, offset 6px below text
Hover link	Color #8AFFE9, transition 200ms ease
CTA button	Primary button, right-aligned
Mobile toggle	Hamburger icon in #68E6FD, 44×44px touch target
4.5 Badges & Tags
Background:     rgba(104, 230, 253, 0.15)
Text:           #68E6FD
Border-radius:  100px (pill)
Padding:        4px 12px
Font:           caption token, SemiBold
Variant	Background	Text
Default	rgba(104, 230, 253, 0.15)	#68E6FD
Success	rgba(0, 99, 93, 0.15)	#00635D
Error	rgba(254, 95, 98, 0.15)	#FE5F55
Premium	rgba(140, 73, 255, 0.15)	#8C49FF
4.6 Icons
Style: Sharpen shapes line × gradient filled
Grid: 24×24px base, multiples of 24 (48, 72) for larger
Stroke width: 1.5px–2px
Colors: Use #2D1E2F (dark grey), #FFFFFF (white), #DAECED (light plain green), gradient #68E6FD → #8AFFE9 (aquamarine), or #65CBFF (smart plain blue)
Touch target: Always pad to minimum 44×44px interactive area
5. Layout Principles
5.1 Spacing Scale (8px base unit)
Token	Value	Usage
space-1	4px	Tight inline gaps, icon-to-text
space-2	8px	Inside compact components
space-3	12px	Input padding, badge padding
space-4	16px	Default component padding
space-5	24px	Card padding, section inner spacing
space-6	32px	Between component groups
space-7	48px	Between sections
space-8	64px	Major section separation
space-9	96px	Hero-level spacing, page top padding
space-10	128px	Full-bleed section breaks
Rule: Always use multiples of 8px. The 4px token (space-1) is the only exception, reserved for micro adjustments.

5.2 Grid System
Property	Value
Type	12-column grid
Gutter	24px (desktop), 16px (tablet), 16px (mobile)
Margin	64px (desktop ≥1280px), 32px (tablet), 16px (mobile)
Max content width	1200px
Column behavior	Fluid within breakpoints
Common Layout Patterns
Full width hero:       12 cols
Content + sidebar:     8 cols + 4 cols
Two equal columns:     6 cols + 6 cols
Three card grid:       4 cols × 3
Four card grid:        3 cols × 4
5.3 Whitespace Philosophy
"Let it breathe" — Aquamarine accents need surrounding negative space to feel electric rather than chaotic
Content blocks should have at least space-7 (48px) vertical breathing room
Never stack more than 3 component types without a visual break (divider, whitespace, or bg change)
Card-to-card gap: space-5 (24px) minimum
Section-to-section gap: space-8 (64px) minimum
5.4 Content Alignment
Text: Left-aligned by default. Center-aligned only for hero sections and single-line CTAs
Cards: Center within their grid column
Forms: Left-aligned, max-width 480px
Modals: Center of viewport, max-width 560px
6. Depth & Elevation
6.1 Elevation Levels
Level	Token	Box Shadow	Usage
0	elevation-0	none	Flat elements, inline content
1	elevation-1	0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.08)	Cards (resting), input fields
2	elevation-2	0 4px 12px rgba(0,0,0,0.15), 0 2px 4px rgba(0,0,0,0.1)	Cards (hover), dropdowns
3	elevation-3	0 8px 24px rgba(0,0,0,0.2), 0 4px 8px rgba(0,0,0,0.12)	Modals, popovers, floating toolbars
4	elevation-4	0 16px 48px rgba(0,0,0,0.25), 0 8px 16px rgba(0,0,0,0.15)	Full-screen overlays, drawers
6.2 Glow Effect (Brand Signature)
For interactive elements on dark surfaces, add an aquamarine glow:

/* Aqua glow — use on hover / focus for primary interactive elements */
box-shadow: 0 4px 20px rgba(104, 230, 253, 0.35);

/* Intense aqua glow — use for hero CTAs or feature highlights */
box-shadow: 0 0 30px rgba(104, 230, 253, 0.25), 0 4px 20px rgba(104, 230, 253, 0.4);
6.3 Surface Hierarchy (Dark Mode)
Layer	Color	Usage
Base	#2D1E2F	Page background
Surface 1	#454252	Cards, panels, sidebars
Surface 2	#54516A (approx +12% lightness)	Nested elements inside Surface 1
Surface 3	#636080 (approx +24% lightness)	Tooltips, elevated dropdowns
Overlay	rgba(45, 30, 47, 0.75) + blur(16px)	Modal backdrops
6.4 Surface Hierarchy (Light Mode)
Layer	Color	Usage
Base	#FFFFFF	Page background
Surface 1	#E0F5F1	Cards, panels, tinted sections
Surface 2	#F5FDFB	Nested elements
Overlay	rgba(45, 30, 47, 0.5) + blur(16px)	Modal backdrops
7. Do's and Don'ts
✅ DO
#	Rule
1	Use aquamarine (#68E6FD) as the single dominant accent — it is the brand signature
2	Maintain high contrast — white text on dark purple, dark text on light surfaces (WCAG AA minimum)
3	Use gradients for primary CTAs and decorative elements, not for large background fills on text-heavy sections
4	Use secondary/accent colors sparingly — only for semantic states (error, success, premium)
5	Respect the cosmic dark ↔ aquamarine light duality in every layout decision
6	Use Lexend Deca consistently for all UI text; reserve Spline Sans only as a paired display alternative
7	Keep icons in the "sharpen shapes line × gradient filled" style using the defined icon color palette
8	Apply 8px spacing rhythm across all margins, paddings, and gaps
9	Use the glow effect on primary actions in dark mode for the signature brand feel
10	Progressive disclosure — Show summary first, details on demand
🚫 DON'T
#	Anti-Pattern
1	Don't use aquamarine on aquamarine — accent elements need contrast with their background
2	Don't mix serif typefaces — the brand is exclusively sans-serif
3	Don't use pure black (#000000) for backgrounds — always use #2D1E2F or #454252
4	Don't overuse secondary colors — they're accents, not themes. Max 1–2 per screen
5	Don't apply Coral Red (#FE5F55) for non-error contexts — it's semantically reserved for danger
6	Don't break the gradient direction — always 135deg or 180deg, never random angles
7	Don't set body text below 16px or ignore the min 12px rule for any UI text
8	Don't make touch targets smaller than 44×44px on interactive elements
9	Don't use ALL CAPS for body text or headings — only for overline tokens
10	Don't use elevation-3+ shadows on light backgrounds in light mode — they will look too heavy; cap at elevation-2
11	Don't place the Coral Red and Electric Violet next to each other — they clash without a neutral separator
12	Don't add borders AND heavy shadows simultaneously — choose one depth mechanism per element
8. Responsive Behavior
8.1 Breakpoints
Token	Range	Columns	Gutter	Margin	Target
xs	0 – 479px	4	16px	16px	Small phones
sm	480 – 767px	4	16px	16px	Large phones
md	768 – 1023px	8	16px	32px	Tablets
lg	1024 – 1279px	12	24px	32px	Small laptops
xl	1280 – 1439px	12	24px	64px	Desktops
2xl	1440px +	12	24px	auto (center at 1200px max)	Large displays
8.2 Touch Targets
Minimum touch target: 44 × 44px (iOS HIG / WCAG 2.5.5)
Recommended for primary CTA: 48 × 48px
Spacing between adjacent targets: minimum 8px gap
On mobile, full-width buttons for primary actions in forms and modals
8.3 Collapse & Reflow Strategy
Component	xl +	md – lg	xs – sm
Top Nav	Full horizontal links + CTA button	Hamburger menu + logo + CTA	Hamburger menu + logo only
Card Grid (3-col)	3 columns	2 columns	1 column, full-width
Card Grid (4-col)	4 columns	2 columns	1 column
Content + Sidebar	8 + 4 columns side-by-side	Sidebar collapses below content	Sidebar hidden behind toggle / accordion
Hero Section	Full layout with illustration	Stack vertically, image above text	Stack vertically, image reduced or hidden
Data Tables	Full table	Horizontal scroll with sticky first column	Card layout (each row = 1 card)
Modal	Centered, max-width 560px	Centered, max-width 90vw	Full-screen bottom sheet
Form	max-width 480px, left-aligned	max-width 90%, centered	Full-width with 16px padding
8.4 Typography Scaling
Headings scale down on mobile (see §3.2). Body text remains at 16px across all breakpoints to ensure readability.

8.5 Responsive Spacing
Screen	Section gap	Card gap	Component padding
xl +	64px	24px	24px
md – lg	48px	20px	20px
xs – sm	32px	16px	16px
9. Agent Prompt Guide
9.1 Quick Color Reference (Copy-Paste Ready)
/* === NextMaven Primary Colors === */
--nm-cosmos-deep:     #2D1E2F;   /* Dark bg */
--nm-cosmos:          #454252;   /* Surface bg */
--nm-aquamarine:      #68E6FD;   /* Brand accent */
--nm-aquamarine-bright:#8AFFE9;  /* Hover glow */
--nm-aquamarine-muted:#6ABAAB;   /* Muted accent */
--nm-ghost-white:     #E0F5F1;   /* Light tint */
--nm-white:           #FFFFFF;   /* Pure white */

/* === NextMaven Secondary Colors === */
--nm-success:         #00635D;   /* Deep teal */
--nm-error:           #FE5F55;   /* Coral red */
--nm-premium:         #8C49FF;   /* Electric violet */
--nm-info:            #60AFFF;   /* Soft blue */
--nm-warning:         #FF899F;   /* Blush pink */
--nm-highlight:       #69E6FF;   /* Neon cyan */

/* === NextMaven Gradients === */
--nm-gradient-cta:    linear-gradient(135deg, #68E6FD, #8AFFE9);
--nm-gradient-dark:   linear-gradient(135deg, #2D1E2F, #454252);
--nm-gradient-light:  linear-gradient(135deg, #68E6FD, #E0F5F1);
9.2 AI Agent Prompts
Use these prompts when instructing AI coding agents (Cursor, Copilot, Claude, etc.) to generate UI consistent with NextMaven's design system.

🎨 General UI Generation Prompt
You are building UI for NextMaven.ai, an AI & Growth training platform.

DESIGN SYSTEM:
- Dark mode primary: bg #2D1E2F, surface #454252, text #FFFFFF / #6ABAAB
- Light mode primary: bg #FFFFFF, surface #E0F5F1, text #2D1E2F / #454252
- Brand accent: #68E6FD (aquamarine) — used for CTAs, links, active states
- Hover glow: #8AFFE9 with box-shadow: 0 4px 20px rgba(104,230,253,0.4)
- Error: #FE5F55 | Success: #00635D | Premium: #8C49FF | Info: #60AFFF
- CTA gradient: linear-gradient(135deg, #68E6FD, #8AFFE9) with dark text #2D1E2F
- Font: 'Lexend Deca' (sans-serif), Chinese: 'Noto Sans HK'
- Spacing: 8px base unit. Border-radius: 8px buttons, 12px cards
- Shadows: elevation-1 for resting cards, elevation-2 on hover
- Touch targets: min 44×44px
- Never use pure black #000000. Never use serif fonts.
- Tone: futuristic, clean, cosmic dark with electric aquamarine energy
🧩 Component Generation Prompt
Create a [COMPONENT_NAME] following NextMaven design system:

Colors → Dark surface #454252 on #2D1E2F bg. Accent #68E6FD. Text #FFFFFF.
Typography → Lexend Deca. Headings: SemiBold. Body: Regular 16px.
Spacing → 8px grid. Padding 24px for cards. Gaps 16–24px.
Border-radius → 8px for buttons/inputs, 12px for cards, 100px for badges.
States → Default / Hover (#8AFFE9 glow) / Active / Focus (outline #8AFFE9) / Disabled (opacity 0.4).
Icons → Line style, 24px grid, 1.5px stroke, aquamarine gradient fill option.
📱 Responsive Layout Prompt
Implement responsive layout for NextMaven.ai:

Breakpoints: xs(<480), sm(480-767), md(768-1023), lg(1024-1279), xl(1280-1439), 2xl(1440+)
Grid: 12-col at lg+, 8-col at md, 4-col at xs-sm
Max content: 1200px centered
Gutter: 24px (lg+), 16px (xs-md)
Margin: 64px (xl+), 32px (md-lg), 16px (xs-sm)
Nav: full at xl+, hamburger at md-, logo always visible
Cards: stack to 1-col on mobile, 2-col on tablet
Buttons: full-width in mobile forms
Modals: bottom-sheet on mobile
Min touch target: 44×44px
🎭 Dark / Light Mode Prompt
Support both modes for NextMaven.ai:

DARK MODE (default):
  --bg: #2D1E2F → #454252 (surface)
  --text: #FFFFFF (primary) → #6ABAAB (secondary)
  --accent: #68E6FD → #8AFFE9 (hover)
  --border: rgba(104,230,253,0.1)
  --glow: box-shadow 0 4px 20px rgba(104,230,253,0.35)
  --nav: rgba(45,30,47,0.85) + backdrop-blur(16px)

LIGHT MODE:
  --bg: #FFFFFF → #E0F5F1 (surface)
  --text: #2D1E2F (primary) → #454252 (secondary)
  --accent: #68E6FD → #00635D (hover on light can use teal)
  --border: rgba(69,66,82,0.12)
  --nav: rgba(255,255,255,0.9) + backdrop-blur(16px)
9.3 Design Token Summary (JSON)
json
{
  "color": {
    "primary": {
      "cosmosDeep": "#2D1E2F",
      "cosmos": "#454252",
      "aquamarine": "#68E6FD",
      "aquamarineBright": "#8AFFE9",
      "aquamarineMuted": "#6ABAAB",
      "ghostWhite": "#E0F5F1",
      "white": "#FFFFFF"
    },
    "secondary": {
      "deepTeal": "#00635D",
      "coralRed": "#FE5F55",
      "electricViolet": "#8C49FF",
      "neonCyan": "#69E6FF",
      "softBlue": "#60AFFF",
      "blushPink": "#FF899F"
    },
    "extended": {
      "skyAqua": "#65CBFF",
      "frostAqua": "#A7FAFF"
    }
  },
  "font": {
    "family": {
      "en": "'Lexend Deca', 'Spline Sans', system-ui, sans-serif",
      "zh": "'HanChan', 'Noto Sans HK', 'Noto Sans TC', sans-serif"
    }
  },
  "spacing": {
    "unit": 8,
    "scale": [4, 8, 12, 16, 24, 32, 48, 64, 96, 128]
  },
  "radius": {
    "sm": "4px",
    "md": "8px",
    "lg": "12px",
    "xl": "16px",
    "full": "100px"
  },
  "breakpoint": {
    "xs": "0px",
    "sm": "480px",
    "md": "768px",
    "lg": "1024px",
    "xl": "1280px",
    "2xl": "1440px"
  }
}
🚀 NextMaven.ai — Master the Future with AI and Growth Training.

"Move fast, embrace change. Test, measure, iterate. Achieve more with less."