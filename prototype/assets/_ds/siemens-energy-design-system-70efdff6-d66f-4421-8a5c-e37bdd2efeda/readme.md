# Siemens Energy Design System

A design system built for **Siemens Energy** work, grounded in the **Siemens Design
Language** as implemented by the open-source **[Siemens Element](https://github.com/siemens/element)**
design system (Angular component library + documentation site for the "smart infrastructure
domain"). This project translates Element's tokens, foundations, and component patterns into a
framework-agnostic kit (CSS custom properties + small React components) for prototyping and
production-adjacent design work.

## Sources

- **[siemens/element](https://github.com/siemens/element)** — the component library, theme SCSS,
  and documentation (`docs/fundamentals/`) this system is built from. Explore it directly for the
  full ~100-family Angular component inventory, exact SCSS tokens, and usage guidance beyond what's
  reproduced here.
- **[siemens/element-icons](https://github.com/siemens/element-icons)** — the icon SVG set;
  `assets/icons/` in this project is a curated copy (~24 of the 1000+ available icons).
- Siemens' full brand system ([Brandville](https://brandville.siemens.com)) is internal-only and
  was not available; colors and type here come from Element's public documentation site, which
  explicitly publishes the real Siemens brand hex values (the Element **npm package itself ships
  a placeholder "ExampleOrg" theme** without real brand colors — see the note at the top of
  `docs/fundamentals/colors/ui-colors.md` in the repo).

If you have access to the private Siemens Figma library or Brandville, use those as the primary
source and treat this system as a starting scaffold, not the final word.

## Company / product context

Siemens Energy is a spin-off of Siemens focused on energy technology (power generation,
transmission, grid software). It doesn't maintain its own public design system; the **Siemens
Element** design system is Siemens' shared design language for professional/industrial software
(building management, grid monitoring, industrial dashboards) and is the closest available source
of ground truth for enterprise Siemens-family UI. This system treats Element's tokens and
components as the foundation for Siemens Energy-branded interfaces.

## Scope note on components

Element's Angular library defines over 100 component families (datepicker, datatable, dashboard
widgets, formly forms, chat messages, launchpad, and more — see `projects/element-ng/` in the
source repo). Reproducing all of them was out of scope for this pass; instead, **13 core
primitives** were built with exact values lifted from Element's SCSS (padding, radius, colors,
font sizes) — see the Components list below. Treat this as a faithful starter set, not the full
inventory, and pull additional components straight from the source repo as needed.

## Directory index

- `styles.css` — root stylesheet, imports everything under `tokens/`.
- `tokens/colors.css` — UI, base, action, text, status, and data-visualization color tokens (light
  + optional dark scope).
- `tokens/typography.css` — type scale (display/heading/body/caption) + font stack.
- `tokens/spacing.css` — 12-step spacing scale (base spacer 16px).
- `tokens/shape.css` — corner radii + elevation (shadow) tokens.
- `guidelines/` — 18 foundation specimen cards (colors, type, spacing, brand/shape/elevation,
  iconography) shown in the Design System tab.
- `assets/icons/` — curated SVG icons copied from `siemens/element-icons`.
- `assets/logos/element-wordmark.svg` — the **Element design-system's own wordmark** (not a
  Siemens Energy logo — see Iconography section below for why no company logo is included).
- `components/` — reusable React primitives, grouped by concern:
  - `core/` — Icon, Card, Avatar
  - `buttons/` — Button, IconButton
  - `forms/` — TextInput, Select, Checkbox, Switch
  - `feedback/` — Badge, EmptyState, StatusDot
  - `navigation/` — Tabs
- `ui_kits/asset-monitoring/` — a click-through recreation of a Siemens Element-style industrial
  monitoring dashboard (the kind of product Element itself is designed for).
- `SKILL.md` — portable skill definition for use in Claude Code or other agent environments.

## Components

| Component | Location | Notes |
|---|---|---|
| Icon | `components/core/Icon.jsx` | Mask-based recolorable SVG icon |
| Card | `components/core/Card.jsx` | Container, header, accent border |
| Avatar | `components/core/Avatar.jsx` | Initials or photo |
| Button | `components/buttons/Button.jsx` | 6 variants × 3 sizes |
| IconButton | `components/buttons/IconButton.jsx` | Circular icon-only button |
| TextInput | `components/forms/TextInput.jsx` | Label, hint, invalid state |
| Select | `components/forms/Select.jsx` | Native-backed dropdown |
| Checkbox | `components/forms/Checkbox.jsx` | Incl. indeterminate |
| Switch | `components/forms/Switch.jsx` | Binary toggle |
| Badge | `components/feedback/Badge.jsx` | 10 semantic types |
| EmptyState | `components/feedback/EmptyState.jsx` | Title/explanation/action pattern |
| StatusDot | `components/feedback/StatusDot.jsx` | Status color + label |
| Tabs | `components/navigation/Tabs.jsx` | Underline tab nav |

### Intentional additions

None of the above are inventions beyond Element's own patterns — `Icon` and `StatusDot` are
thin wrappers Element itself expresses differently (via `si-icon` and `si-circle-status`
Angular components) but which needed a simple framework-agnostic equivalent here.

## CONTENT FUNDAMENTALS

Source: `docs/fundamentals/ux-text-style-guide/` in siemens/element.

**Tone & voice**
- Natural and conversational, never "robotic, funny, cool or clever."
- Don't address the user directly in the UI itself; direct address ("you") is reserved for
  formal contexts — emails, app tours.
- Gender-neutral, polite, but **no "please," "sorry," or apologies**.
- Positive framing over negative: say what something *does*, not what it fails to do.
- Avoid contractions generally (though "cannot," "will not" are fine as Do's — the guide's
  own examples still show contracted modals like "you will").

**Capitalization**
- Sentence case everywhere: titles, buttons, menu items, tooltips. Never all-caps
  (`PLANNING` → `Planning`).
- Named UI elements and app functions are capitalized: "Go to **Settings**," "Press **OK**."

**Length & structure**
- Fewest words possible; short, scannable segments over paragraphs.
- Sentences under 25 words (aim for ~15); titles under 65 characters.
- Avoid abbreviations and acronyms; when unavoidable, spell out on first use:
  "light emitting diodes (LEDs)."

**Grammar**
- Present simple for instructions/actions ("click," "browse," "file loads").
- Present participle + ellipsis for in-progress states: **"Saving project…"** → **"Project saved"**
  (echo the same verb in the confirmation).
- Active voice always: "Admin provides read-only access," never "Read-only access is provided."

**Dialogs & buttons**
- Concise, generic dialog titles — never instance names ("Delete building," not "Delete
  Wittelsbacherplatz München").
- Buttons describe the action and relate to the title: `Add user` → `Cancel`, `Add` (never
  `Cancel`, `OK`).
- Primary action sits on the right: `Cancel, Save` — never `Save, Cancel`.
- Avoid "Yes"/"No" — use the actual verb ("Delete," "Discard").

**Empty states**
- Three-part structure: title (what's missing) → explanation (why/context) → action (how to
  fix it). E.g. *No users* / *Add users to current site* / **Add users**.
- Never over-communicate; the empty state should read as intentional, not broken.

**Time-based wording**
- "Latest" implies more may follow; "last" implies finality. Prefer "Latest update" over "Last
  update" for anything ongoing.

## VISUAL FOUNDATIONS

Source: `docs/fundamentals/` (colors, typography, shapes, elevation, illustrations) in
siemens/element.

**Color** — Colors are organized into five semantic layers, never used as raw hex in product
code: **UI** (structure/icons/borders — `ui-0`…`ui-6`), **Base** (surface backgrounds —
`base-0`…`base-4` plus status-tinted backgrounds), **Action** (button states — primary /
secondary / warning / danger, each with hover), **Text** (primary/secondary/disabled/semantic),
and **Status** (information/success/caution/warning/danger/critical — mode-independent hue used
for badges, alarms, charts). The brand accent is a **deep teal** (`#006b80`, `ui-0`/
`action-primary`) in light mode, replaced by a **bright coral** (`#00cccc`→coral family) in dark
mode — the two modes are not just inverted lightness, they swap hue family entirely. A qualitative
data-visualization palette (petrol, turquoise, royal blue, coral, plum, purple, orchid, orange,
yellow, red, green, avocado, sand) exists separately for charts and must not be reused for UI.

**Typography** — One typeface family throughout (headings and body share it; no serif/mono
pairing except for code). Hierarchy comes from **size + weight**, not style changes — italics are
used "sparingly, for cases like technical terms," never for emphasis in running text. Display
styles (40–56px) are reserved for hero/dashboard headlines and used sparingly. Body defaults to
14px/16px line-height; the type scale is tight and utilitarian, built for dense data-forward UIs
rather than editorial reading.

**Spacing** — An additive scale based on a 16px root spacer (2, 4, 6, 8, 12, 16, 20, 24, 32,
64, 96px). Everything aligns to this rhythm; card padding is 16px, form field padding is 8px,
button vertical padding is 8px (sm: 4px, lg: 12px).

**Backgrounds** — Flat and utilitarian: solid `base-0`/`base-1` surfaces, **no gradients** in UI
chrome (gradients exist only as named data tokens for range/temperature visualizations — e.g. a
danger gradient from neutral to red — and in one bold-green→coral brand gradient reserved for
marketing use, not UI). No repeating patterns or textures. Full-bleed imagery is not a UI
pattern; when photography appears it's contained (cards, headers), not full-bleed.

**Illustration** — Follows Siemens' internal "Brandville" illustration guidelines: simple, clean,
purposeful line-based illustrations for onboarding/empty-states/marketing, in the approved brand
palette, with theme-specific (light/dark) variants where needed. Avoid heavy gradients or
patterns in illustration work. None were available to copy into this project (Brandville access
is internal-only) — use plain icon placeholders or ask the user for real illustration assets
rather than hand-drawing new ones.

**Animation** — Element specifies short, functional transitions only: `0.15s ease-in-out` for
color/background/border changes (buttons, inputs), `0.2s ease-in-out` as a general base
transition, `0.3s ease-out` for modal entrances (subtle translate + scale, not bounce), `0.35s
ease` for collapse/expand. No bounce or elastic easing anywhere — motion is quick and
utility-first, never decorative.

**Hover / press states** — Hover states shift to a **dedicated hover token** per action/surface
(e.g. `action-primary-hover`, `base-1-hover`) rather than a generic darken/lighten filter — in
light mode primary hover goes from teal to a darker teal-green; in dark mode it inverts to a
lighter mint. Press/active states use a third dedicated token, one step further (e.g.
`base-1-selected`). No scale/shrink press effects were found in the source.

**Borders & shadows** — Borders are 1px `ui-4` (a soft gray), used to separate same-level
content — "layout sections or grouped content" — not to decorate every container. **Cards never
have shadows** (explicitly stated: "Components without overlapping behavior, such as cards, must
not have shadows"). Shadows are reserved for genuinely floating/overlapping elements — menus,
popovers, modals, toasts — via 4 elevation levels (4/8/16/32px blur, two-layer black at 8–16%
opacity). Elevation is otherwise conveyed by base-color layering (`base-0` → `base-1` → `base-4`),
not by drop shadow.

**Transparency & blur** — Used narrowly: a translucent scrim (`base-translucent-1`, 30–70%
black) behind modals, and a near-opaque translucent surface (`base-translucent-2`, ~88% opacity)
for toasts — no frosted-glass/backdrop-blur pattern was found.

**Corner radii** — Four-step scale: 0 / 2px (buttons, inputs) / 4px (cards, containers,
default) / 8px (larger containers), plus a pill radius for badges (12px) and fully-round for
avatars/dots/switches.

**Cards** — 4px radius, `base-1` fill, no border by default (an optional `ui-4` 1px outline
variant exists for a "card-outline" treatment), no shadow, 16px body padding, 12–16px header
padding, optional 8px solid accent border on the leading edge for status cards (one accent color
only, never combined with the outline variant).

**Imagery** — No stock photography or generic imagery patterns were found in the source
repository (Element is a component library, not a marketing site) — do not invent a "warm/cool/
grainy" photographic style; ask the user for real product photography if a design needs it.

## ICONOGRAPHY

Source: `docs/fundamentals/icons.md` in siemens/element; SVGs from `siemens/element-icons`.

- **System**: a large first-party icon set (1000+ icons), available both as **individual SVGs**
  (preferred) and as an icon font (`element-*` CSS classes) for legacy compatibility — SVGs were
  introduced specifically to cut bundle size versus the 100KB+ font.
- **Style**: outlined by default, 2px uniform stroke weight, built on a 32×32px grid with a 2px
  safe zone; corners use a consistent 2px radius. Filled variants exist for emphasis/active states
  only (e.g. `alarm-filled`, `validation-success-filled`) — outlined is the default everywhere
  else.
- **Sizes**: 16px (dense/inline), 20px (default, pairs with body text), 24px (prominent, pairs
  with body-lg). Additional sizes only in 4px increments if truly necessary.
- **Color**: single flat color per icon (no multi-color icons except intentional "composite"
  icons that overlay two icons for status meaning, e.g. an alarm bell + a check). Default colors
  are `ui-1` (primary) / `ui-2` (secondary) — icons otherwise follow the same semantic color
  tokens as text.
- **No emoji, no unicode glyphs-as-icons** — this is a strictly SVG/icon-font system.
- **Copied into this project**: 24 representative icons in `assets/icons/` (account, home,
  settings, alarm, edit, delete, download, upload, plus, cancel, search, four `validation-*`
  status icons, navigation chevrons, menu, calendar, dashboard, document, filter, refresh). Full
  set (1000+) is in `siemens/element-icons` — copy more in as needed rather than hand-drawing.
- **Logo**: no Siemens Energy (or Siemens corporate) logo was available in the provided source —
  `siemens/element` only contains the **Element design system's own wordmark**
  (`assets/logos/element-wordmark.svg`), which is a self-referential mark for the component
  library, not a company brand asset. **Do not use it as a stand-in for a Siemens or Siemens
  Energy logo.** Wherever a logo would appear in a mockup, render the company name in plain type
  instead, and ask the user for the real logo file.

## Font substitution — please read

Element's real typeface is **Siemens Sans Pro**, a proprietary Siemens brand font. Its files are
explicitly excluded from the open-source repo ("part of the official Siemens branding and must
not be used in non-Siemens applications"). This system substitutes **Noto Sans** (Google Fonts, in
`tokens/typography.css`) as the closest freely-licensable neutral humanist grotesque, at the same
size/weight/line-height scale Element defines. **If you have access to real Siemens Sans Pro font
files, please share them** so this system can be updated to use the authentic typeface.

## Dark mode

Element is a dual-mode system, and the real brand palette swaps hue family between modes (teal ↔
coral), not just lightness. A `[data-theme='dark']` scope is included in `tokens/colors.css` with
the documented dark-mode hex values; apply `data-theme="dark"` to a container to opt in. UI kits
in this project are built light-mode only — ask if you'd like dark-mode screens too.
