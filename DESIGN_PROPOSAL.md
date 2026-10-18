# Design Proposal v2: Dental Esthetics Boston homepage (cold-pitch concept)

Supersedes v1. It now incorporates `EXISTING_SITE_AUDIT.md` and the KUDUY v2 rules (Lenis, layout selector, creative thesis, anti-slop).

## 1. Objectives and audience
- **KUDUY's goal:** the practice reads the concept, recognises itself, and books a call.
- **Patients' goal:** book a consultation or call.
- **Audience:** adults aged 40–75 weighing implant, full-mouth or esthetic work. A small secondary group of family/general patients. See `MARKET_RESEARCH.md`.

## 2. Audit summary
The live site uses Wix with 9 fonts and default blue. **The Book CTA does nothing.** The headline is a superlative ("Best Dentists in Boston"). There are SEO errors (typo `h1`s, a wrong-dentist meta description, leftover pages) and contradictory pediatric copy. Full detail is in `EXISTING_SITE_AUDIT.md`.

## 3. What to keep
- The name and the "Hirayama & Papaspyridakos" line.
- Navy brand color (`#224F7F`), deepened.
- The real testimonials.
- The Top Dentists badges (flagged for checking).
- The office photos.
- Links to the parking, FAQ and smile-gallery pages.

## 4. Market findings
- Back Bay competitors are general/cosmetic practices and multi-specialty groups that promote with superlatives and directory badges.
- **Two teaching prosthodontists** is the rarest asset in the set, and the current site doesn't say it.

## 5. Journey hypotheses
1. "Do I need a specialist?"
2. "Are these the right ones?"
3. "What will happen, and will it hurt?"
4. "How do I book?"

The page answers them in that order: credentials, then the specialists, then treatments, then process, then words from patients, then the visit details.

## 6. Recommended direction
**Clinical Editorial.** Authority comes from typography and facts that can be checked, not from imagery or slogans. This suits a high-trust, high-cost decision and sets the practice apart from template-driven competitors.

## 7. Your selections
- Style: industry recommendation, plus luxury/refined editorial, plus clean modern clinical.
- Layout: the recommended "clinical record" Swiss/editorial grid.
- Motion: Lite.
- Smooth scrolling: Lenis.
- Top Dentists badges: shown, with a flag.

## 8. Creative thesis
> **"The clinical record": the page reads like a specialist's case notes. It is ruled, numbered and precise, so expertise is shown through documented fact rather than claimed.**

- **Personality:** calm, exact, quietly confident; academic without being cold.
- **Composition:** a strict 12-column grid, hairline rules, numbered sections ("01 — Specialists") set in serif sentence case instead of all-caps eyebrows. The asymmetry comes from the grid, not from decoration.
- **Signature moments:**
  1. A **hero credentials ledger**: a ruled table beside the headline, listing each doctor's board certification, academic post and publications, like a chart header.
  2. A **treatment index**, numbered like a table of contents.
  3. An **arch frame** on the photos, echoing Back Bay brownstone doorways.
- **Anti-references:** stock smiles, teal/blue gradients, "Best dentist" headlines, icon tiles, card grids, chat bubbles, pill-button clusters, all-caps labels on every section.

## 9. Type, color, imagery, layout
- **Type:** Newsreader (display, variable) and Public Sans (text). Two families, self-hosted.
- **Color:**
  - Porcelain `#F5F3EE` (background)
  - Ink-navy `#172A3A` (text and dark bands; a deepened version of the brand's `#224F7F`)
  - Slate `#4A5A66`
  - Hairline `#D9D4CA`
  - One accent, brass `#8A5A22`, or `#D2A465` on dark backgrounds
  - All text pairs meet AA.
- **Imagery:** 3 real office photos. They are low-resolution (382px), so they are shown framed at native size or smaller and never full-bleed. Doctor portraits are `TODO(client)`.
- **Hero layout:** headline at 7/12 width. The ledger and the arch photo share the right 5/12. One primary CTA (a rectangular button with a small radius), with the phone as a text link.

## 10. Hierarchy and conversion
Sections run in this order: Hero/ledger, Specialists, Treatments index, How a case works, The practice, Patients' words, Visit.

Conversion paths:
- A working "Book a consultation" link to `/contact-us` in the header, hero and Visit section.
- `tel:` links throughout.
- On mobile, a sticky Call / Book bar.

## 11. UI and interaction
- Desktop shows a visible nav bar; the hamburger appears only below 1024px.
- Treatment rows highlight on hover and focus.
- The hours table is real, semantic table markup.
- Skip link and visible focus states.

## 12. Lenis
- `lenis@1.3.27` from npm, copied to `vendor/` at build time. No CDN, no bundler.
- One instance using `autoRaf` (a single animation loop).
- `anchors` offset for the sticky header and `stopInertiaOnNavigate`.
- `respectReducedMotion` stays at its default (on).
- Lenis is paused while the mobile menu is open.
- CSS `scroll-behavior: smooth` is removed; `scroll-padding-top` stays as a fallback if JS doesn't load.
- Tuning: `lerp 0.12` for responsive feel, not slow drag.

## 13. Reveal intensity: Lite
- Opacity plus a 12px rise, about 600ms, minimal stagger.
- A clip-path wipe on the 3 photos.
- Off entirely under reduced motion.

## 14. Dependencies
Lenis only. GSAP, ScrollTrigger and Three.js are not needed at Lite intensity.

## 15. Responsive, accessibility, performance
- Composed (not just shrunk) for 375, 768, 1280 and 1536.
- One `h1`, landmarks, AA contrast, keyboard-operable menu.
- Under about 300 KB total including fonts, with no layout shift (image width and height are set).

## 16. Acceptance and assumptions
- **Acceptance:** no overflow; no console errors; every link works; Lenis anchors land below the header; every fact is verified or tagged `TODO(client)`.
- **Open questions for the client:**
  - Which doctor and which years the badges cover
  - Whether pediatric care is offered
  - Office hours
  - Booking URL
  - Doctor portraits
  - Exact testimonial wording

---

# v3: Gallery White (approved 2026-10-18, supersedes the v2 visual layer)
The client found v2 not premium enough. They chose **Gallery White** and **Normal** motion. The audit, research, facts and conversion paths are carried over from v2.

- **Creative thesis:** *The practice presented like a gallery.* Bright walls, large photography and oversized light serif type, with credentials set like museum wall labels. Quiet, exact, expensive.
- **Palette:**
  - Paper `#FAF9F6`
  - Wall `#F1EFEA`
  - Ink `#121820`
  - Graphite `#5E656C`
  - Rule `#E4E1DA`
  - One accent: the practice's navy `#1F3A56`, used for the main button and the mobile Book button
  - One dark "room" (Treatments) and a dark footer give the page depth
- **Type:** Newsreader Light at display scale (up to about 9rem) with italic accents, and Public Sans for body text. Small caps-style labels appear only in the nav, captions and labels.
- **Layout:**
  - Centered-wordmark header that hides on scroll down
  - Hero (client request: keep the earlier split banner): headline, copy and CTA on the left; the team photo bleeds to the right edge with a paper caption plate. On mobile the photo is full-width below the CTA.
  - A one-paragraph statement
  - Specialists: large portraits staggered like hung works, each with a credentials label
  - Treatments: an oversized index on ink
  - Process with large numerals
  - Practice photos hung on a wide wall
  - One large quote
  - Visit
  - A giant-wordmark footer
- **Motion (Normal, CSS + vanilla JS + Lenis, no GSAP):**
  - Headlines reveal line by line
  - Images wipe in behind a mask and settle from a slight zoom
  - Clamped parallax on the hero and practice photos
  - Treatment rows nudge sideways on hover, and their arrow rotates
  - Button arrows slide
  - Everything is inert under reduced motion
