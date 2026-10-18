# Dental Esthetics Boston: homepage concept (KUDUY)

An unsolicited redesign concept for dentalestheticsboston.com.

- **Stack:** static HTML, Tailwind CSS v4 (CLI), vanilla JS and Lenis. No framework, no backend.
- **Creative thesis:** "Gallery White": the practice presented like a gallery, with bright walls, large photography, oversized light serif type and credentials set like museum wall labels. See `DESIGN_PROPOSAL.md` (v3).

## Build & run
```bash
npm install
npm run build
python -m http.server 5173
```
- `npm run build` copies Lenis into `vendor/`, then compiles `src/input.css` to `dist/styles.css` (minified).
- Instead of `python -m http.server`, any static server works. Then open http://localhost:5173.
- `npm run dev` watches the CSS while you edit.

## Deploy
Upload `index.html`, `dist/`, `js/`, `vendor/` and `assets/` to any static host. There are no runtime CDNs.

## Structure
| Path | Contents |
|---|---|
| `index.html` | The page |
| `src/input.css` | Design tokens (`@theme`), fonts, utilities, Normal-intensity motion (line reveals, mask wipes, parallax layers). Imports `lenis/dist/lenis.css`. |
| `js/main.js` | One Lenis instance; one frame-batched scroll handler (hide-on-scroll header + clamped parallax); full-screen mobile menu (pauses Lenis); IntersectionObserver reveals |
| `vendor/lenis.min.js` | Lenis 1.3.27, copied from npm at build time |
| `assets/fonts` | Newsreader (variable) and Public Sans 400/600, self-hosted woff2 |
| `assets/images` | Team banner (`team-640/980.webp`, supplied by KUDUY); doctor portraits (`dr-*.webp`, cropped 600×750 from the practice's Meet the Team page); three office photos (382×510). All converted to WebP with `sharp`. Badges: `badges/top-dentists-2017…2025.webp` (320×320, trimmed from the live homepage's badge images). Case: `case-full-arch-600/1000.webp` (before/after from the live homepage). |

Project docs: `EXISTING_SITE_AUDIT.md`, `MARKET_RESEARCH.md`, `DESIGN_PROPOSAL.md`, `QA_REPORT.md`.

## Links
- Booking CTAs go to the live `/contact-us` page.
- Treatment, team, testimonial, parking, FAQ and gallery links go to the live site.
- `tel:` and Google Maps links work as is.

## TODO(client) before going live
- Which doctor each year's Boston magazine Top Dentists badge (2017–2025) names. The 2025 file name on the live site credits Dr. Papaspyridakos.
- Office hours. The live hours widget is broken; Tue–Thu 8–5 is how it reads.
- Testimonial wording (confirm it is verbatim) and permission to reuse it. Also confirm the "How a case works" wording.
- Refresh the Google rating figures (4.9, 206 reviews, read 2026-10-19) at launch, or swap in a live Google reviews widget the practice is licensed to use.
- Whether pediatric care is offered (the live site contradicts itself).
- A booking-system URL, if there is one other than `/contact-us`.
- Higher-resolution photography. The current photos are 382 px wide.
- Remove `noindex` and the concept disclaimer in the footer.

## Dependencies & licences
- **lenis 1.3.27:** MIT, smooth scrolling.
- **Fonts:** Newsreader (Production Type) and Public Sans (USWDS), both SIL OFL, installed via @fontsource.
- **Build tools only:** tailwindcss and @tailwindcss/cli 4.x; sharp (one-time image conversion).
- **Photos:** the office photos and team banner were supplied by KUDUY. The doctor portraits come from dentalestheticsboston.com/meet-the-team and are the practice's own images; get the practice's permission before using them anywhere public.
- **Credentials:** Tufts University and Boston University faculty profiles, and the practice's own website.

## Logo (concept refresh)
The logo is a double-ring seal with a light italic serif "DE" monogram, beside the "Dental Esthetics Boston" wordmark in Newsreader Light and the "Hirayama & Papaspyridakos" line in tracked Public Sans. The two rings nod to the practice's current double-arch mark.

- **Files** (`assets/logo/`): `logo-horizontal`, `logo-stacked` and `mark`, each also as a `-light` version for dark backgrounds, plus `favicon.svg` (a solid navy seal for small sizes).
- **Outlined text:** all SVG text is converted to vector outlines, so the files render correctly without the fonts installed.
- **PNG exports:** `logo-horizontal@2x.png`, `logo-horizontal-light@2x.png`, `logo-stacked@2x.png`, `mark-512.png` and `apple-touch-icon.png`.
- **Regenerating:** run `python scripts/make_logo.py .`. It needs `pip install fonttools brotli uharfbuzz`.
- **Status:** this is a proposal for the practice. Their registered logo is unchanged until they approve it.
