# QA Report: 2026-10-18 (v3, Gallery White)

## Checks performed
| Check | How | Result |
|---|---|---|
| Layout at 768 and 1440 | Full-length headless Edge captures, sliced and reviewed | **Pass.** |
| Layout at 1440×900 | Headless Edge, split-banner hero | **Pass.** The headline sits left, the photo bleeds right with no gaps, and the caption plate sits bottom-left. |
| Layout at 375 | Built-in browser, mobile emulation | **Pass after fix.** No horizontal overflow (`scrollWidth` = 375). The wordmark is on one line. |
| Lenis | Active (`html.lenis` class) | **Pass.** One instance, `autoRaf`. |
| Anchor offset | Mobile menu link to #practice | **Pass.** Lands 96px from the top (`scroll-padding-top: 6rem`). |
| Mobile menu | Open and close | **Pass.** Opens full-screen and the label changes Menu → Close. `aria-expanded` toggles. Lenis stops while open and restarts on close. Page scroll is locked. Clicking a link closes the menu, then scrolls. Escape closes it and returns focus to the toggle. |
| Header behaviour | Scroll down, then up | **Pass.** It hides after 320px of downward scroll and returns when scrolling up, when focus is inside it, or when the menu opens. |
| Structure | DOM checks | One `h1` holding the full hero sentence. Every image has alt text. |
| Contrast | Calculated | Ink on paper is about 17:1. Graphite on paper is about 6:1. Navy button text is about 11:1. Fog on ink is about 8:1. The process numerals were raised to graphite/75 (decorative, large). |
| Console and network | Built-in browser | No errors. No failed requests. |
| Build | `npm run build` | **Pass.** |

## Fixed during QA
- **Parallax showed image edges on tall viewports.** The shift is now clamped to the 6% overscan.
- **The mobile wordmark wrapped onto two lines.** The header is a flex row below `lg` and a three-column grid at `lg` and up.
- **The process numerals had low contrast.** They now use graphite/75.
- **Image corners (client choice):** a subtle 6px radius on every image frame. The hero photo is rounded on its inner (left) edge only at desktop, and is square where it meets the screen edge. Verified by zooming on the rendered corners.
- **Recognition section added (client request):** all nine Boston magazine Top Dentists badges, 2017–2025, taken from the live homepage and shown in a 9-column row at lg and a 3×3 grid at 375. All images load, no overflow. Verified at 1440 and 375.
- **Treatments became six icon cards (client request):** the live homepage's "Experience Excellence" items (implants, cosmetic, advanced technology, whitening, family, recognition) on the dark section, with custom 1.15px line icons. Hover inverts the icon. The CTAs align to the card bottoms. Mobile cards are compacted to 333px. Verified at 1440 and 375.
- **Case study added (client request):** the live site's full-arch before/after (1190px original, served at 600/1000w WebP) with a treatment and clinician label and CTAs. Checked at 1440 and 375: no overflow, image loads.
- **Reviews section rebuilt (client request):**
  - **Google rating card:** 4.9 stars from 206 reviews, a 5★/4★/1–3★ breakdown (201/1/4) and the most-mentioned topics. All figures were read from the Google Maps listing on 2026-10-19.
  - **Slider:** the six testimonials published on the practice's site, on a native scroll-snap track with prev/next buttons, arrow keys, a 01/06 counter, a progress bar and `aria-hidden` on the off-screen slides. Tested at 1120 and 375: buttons, keys and swipe all update the state, and the buttons disable at each end.
  - **Google review text not copied:** verbatim review text was not copied from Google because it belongs to its authors. A "Read all reviews on Google" link goes to the listing instead.
- **Bug found and fixed:** the slider column grew to fit all six slides (page 1031px wide at 375). Fixed with `min-w-0` on the grid item.
- **Header nav wrapped at about 1120px** ("The practice" on two lines). Fixed with `whitespace-nowrap` and a tighter gap below `xl`.

## Not verified
- **Reduced-motion behaviour** was checked in code only, not with emulation. All reveal and parallax CSS is under `prefers-reduced-motion: no-preference`, parallax JS is skipped, and Lenis `respectReducedMotion` is on its default.
- **No Lighthouse run and no real-device or Safari test.** Hover states were checked in code only.

## Known limits
- **Photo permissions:** the office photos are 382px wide, so they hang small by design. The portraits and team photo are the practice's own images, so get permission before any public use.
- **Hero crop:** the split-banner hero crops the staff member on the left edge at desktop widths. Staff are not named because who is who is unverified.
- **The page is set to `noindex`** because it's a concept.
- The remaining `TODO(client)` items are listed in the README.
