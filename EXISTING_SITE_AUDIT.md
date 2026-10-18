# Existing Site Audit: dentalestheticsboston.com

Audited 2026-10-18 in the built-in browser. Pages were fetched from the live origin, styles were computed in the browser, and the homepage was rendered at desktop width and at 375px.

## 1. Coverage
- **45 URLs** in `pages-sitemap.xml`. All 45 were fetched and inspected one by one: HTTP status, `<title>`, meta description, `h1`, word count and forms. All returned 200; none were inaccessible.
- **Rendered:** homepage on desktop and at mobile 375px (Wix serves a fixed 320px mobile layout).
- **Not rendered visually:** inner page templates. They were inspected from their HTML only. Blog posts and portfolio sub-sitemaps were not crawled.

## 2. Visual identity (computed values)
| Token | Value | Note |
|---|---|---|
| Logo | Blue double-arch tooth mark with a bold sans wordmark, "DENTAL ESTHETICS BOSTON / Hirayama & Papaspyridakos" | 317px JPEG. It is cropped in the desktop header. |
| Headings | `fraunces` 400. h1 50px, h2 56px (larger than h1), h3 20px | |
| Body copy | `fraunces` 15px / 21px. Header and footer text falls back to Arial 10px. | Serif body copy at 15px reads poorly. |
| Font families in use | **9**: Arial, Helvetica, lato-light, raleway, fraunces, helvetica-w01, avenir-light, proxima-n, poppins-semibold, cormorantgaramond-light | There is no type system. |
| Colors | Black text `#000`, white, grey `#E8E6E6`, button blue `#4388E4` / `#4588E4`, navy `#224F7F`, light blue `#ABC3F9` | The blue is the Wix default. Black text on blue buttons is about 4.5:1, which is borderline. |
| Buttons | Square corners, uppercase, 10px Arial computed (visually larger in the Wix layer) | |
| Motion | None found apart from Wix defaults. There is a floating chat widget. | |

## 3. Structure and content
- **Homepage:** a hero with a team photo (Dr. Panos and two staff), the headline "Exceptional Dentistry For All Ages", Watch Video and Book buttons, five service blurbs, "The Best Dentists", a CTA, and office hours.
- **Navigation:** a hamburger menu at every size, including desktop, which hides the information architecture.
- **Services:** about 25 pages built from one template, each around 220–570 words.
- **Team:** a team page with about 5,100 words (CV-length), two staff pages, and one doctor page.
- **Trust pages:** awards (109 words), testimonials (6 quotes and a form), and a smile gallery.

## 4. Interactions (tested)
- **"BOOK ONLINE"** in the header was clicked at 375px and **nothing happened**: no navigation, no dialog, no iframe. Both it and "BOOK APPOINTMENT NOW!" have no `href`.
- "WATCH VIDEO" has no `href` and the page contains no video element. This was not clicked.
- Only **one** visible `tel:` link exists on mobile.
- The chat widget sits on top of the award badges on mobile.

## 5. Strengths to preserve
- **Real expertise.** Two prosthodontists who teach; the team page says "two world-renowned prosthodontists".
- **Boston magazine "Top Dentists" badges, 2022–2025.** These are shown in the hero. I did not independently verify them; see `TODO(client)`.
- Real patient testimonials naming the doctor and the treatment.
- A real team photo of Dr. Panos with staff.
- Supporting pages worth linking to: parking/commuter, FAQs, smile gallery.
- Brand recognition: the navy/blue mark and the "Hirayama & Papaspyridakos" line.

## 6. UX and visual issues
- The logo is cropped in the desktop header.
- The hero headline sits over a busy photo.
- The office-hours widget is broken: day names and times render as separate lists.
- Nine font families; an h2 larger than the h1; 15px serif body text.
- Desktop uses a hamburger menu even though there is room for a nav bar.
- The mobile layout is a fixed 320px Wix layout, and the hero image loads blurred first.

## 7. Content and conversion problems
| Problem | Where |
|---|---|
| The primary CTA doesn't work (Book Online / Book Appointment) | Homepage |
| Typo "SERVICES INLUDE:" used as the **h1** | /specialty-dentistry, /general-dentistry, /preventative-care, /cosmetic-dentistry |
| Meta description describes **"Dr. Jeanne Un"**, who is not on the team | /meet-the-team/sabrina, /meet-the-team/kerry |
| Boilerplate mentions **pediatric** dentistry on about 26 service pages, and the home meta says "multidisciplinary clinic… Pediatric Dentistry" | This conflicts with the Tufts profile ("practice limited to prosthodontics and implant dentistry") |
| Home meta says "downtown Boston"; the practice is in Back Bay | Homepage |
| Two `h1`s on the homepage; **no** `h1` on /contact-us or /dental-veneers | |
| Published leftovers: /coming-soon-01, /copy-of-portfolio (a duplicate of the smile gallery), /meet-dr-panos (5 words) | |
| Dr. Hirayama is barely mentioned outside the team page | Whole site |
| Superlatives ("The Best Dentists in Boston") replace credentials that can be checked | Homepage |
| No insurance or fees information found on any page | Whole site |

## 8. Opportunities
1. Make the specialist credentials the main message, and show the Top Dentists badges as supporting proof.
2. Give one working booking path, repeated, plus a tap-to-call on mobile.
3. Resolve the positioning: complex restorative and implant work first, general care second. Ask the client whether pediatric care is actually offered.
4. Clean up SEO: one `h1` per page, correct metas, remove leftover pages, and set the Back Bay locality.
5. Build one type system and one color system. Keep the navy as a nod to the brand.

## 9. Evidence limits
- The booking flow may exist in a Wix lightbox that didn't fire in the emulated browser. It needs a check on a real device.
- I couldn't verify the Top Dentists badges independently in Boston magazine search results.
- Inner page templates were checked as HTML only, not visually.
