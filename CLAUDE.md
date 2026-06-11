# CLAUDE.md — longfu88-malaysia.com

> Project memory for Claude Code. This file is the single source of truth for building and
> maintaining the **Malaysia** site in the Longfu88 Brand SEO Campaign. Read it fully before
> editing anything. The Singapore site (`longfu88sgd.com`) is a separate repo with its own
> CLAUDE.md — do not mix market-specific content between the two.

---

## 1. What this project is

A **static, ranking-optimised affiliate review site** for the **Longfu88** online casino brand,
targeting the **Malaysia** market. It is an independent information/review platform (NOT the
operator). All content is framed as an editorial review of the official Longfu88 brand, with a
transparent affiliate disclosure.

- **Domain:** `longfu88-malaysia.com`
- **Market:** Malaysia (English only)
- **Brand reviewed:** Longfu88 — official site `https://longfubet8888.com/`
- **Engagement:** 3-month brand SEO campaign (12 weeks), part of a 2-site build (MY + SG).
- **Goal:** Rank the 13 Malaysia brand keywords (see §6), achieve Tier-1 keyword page-one
  positions within the 90-day window, and outrank the brand's own weak-EEAT pages on its own
  brand queries.

**Why this site exists (the SERP gap):** The official Longfu88 site scores near-zero on E-E-A-T
(white-label boilerplate About page, no licence disclosure, no author attribution) and top
positions for "Longfu88 …" queries are currently held by phishing/unoptimised affiliates. This
site is built to be the most trustworthy, best-optimised result for those brand queries.

---

## 2. Tech stack & hosting (fixed — do not substitute)

| Layer | Choice |
|---|---|
| Markup | **Static HTML** (hand-built, no CMS, no SSG runtime, no React/JS framework) |
| Styling | **Tailwind CSS** via a shared design system / component set |
| Interactivity | Vanilla JS only, kept minimal (FAQ accordions, mobile nav) |
| Repo | **GitHub** (repo created by client; full commit history required) |
| Hosting | **GitHub Pages** (free tier) |
| DNS / CDN / SSL | **Cloudflare** (free tier; SSL by default) |
| Analytics | **Cloudflare Web Analytics** (privacy-friendly, no cookie banner needed) |
| Search | **Google Search Console** (sitemap submission + 3-month monitoring) |

**Constraints that follow from static + GitHub Pages:**
- No server-side code, no databases, no build server. A static build step (Tailwind CLI) is fine.
- All pages must work as plain HTML served from a CDN.
- Performance budget: optimise for Core Web Vitals (LCP, CLS, INP). Inline critical CSS where it
  helps, lazy-load images, compress assets. The site must pass Google's Core Web Vitals.

---

## 3. Brand CI (from client-supplied JSON)

Use the official Longfu88 palette/fonts. Take **layout/structure** inspiration from the reference
sites in §12, but **ignore their branding** — colours, fonts and logo come only from here.

```
Color scheme : light
Background   : #FFFFFF
Primary      : #C70028   (brand red — primary CTAs, key accents)
Secondary    : #9F0020   (darker red — hover/active, depth)
Accent       : #EB002F   (bright red — highlights)
Link         : #EB002F
Text primary : #635B5B   (body copy — warm grey)
Font         : "Sofia Sans", sans-serif   (headings AND body)
H1 / H2 size : 28px       Body size: 14px
Spacing base : 4px grid
Border radius: 0px        (sharp corners — no rounded edges)
Tone         : bold, high-energy
```

- **Logo:** Longfu88 logo PNG was supplied as base64 in the brand JSON. Save it to
  `assets/img/logo.png` and reference locally — do not hotlink.
- **Favicon:** the brand JSON points to `https://longfubet8888.com/favicon.ico`. Download a copy
  and self-host at `assets/img/favicon.ico` rather than hotlinking the operator's domain.
- Implement the palette as Tailwind theme tokens (e.g. `brand-primary`, `brand-secondary`,
  `brand-accent`, `brand-link`, `brand-text`) so colours are never hard-coded ad hoc.
- Respect **0px border radius** everywhere and the **4px spacing scale** — this is a deliberate
  sharp, bold aesthetic.

---

## 4. Editorial / legal framing (read before writing any copy)

- This is an **independent affiliate review site**, not Longfu88 itself. Never claim to *be* the
  operator. Use language like "our review of Longfu88", "based on our testing".
- Gambling content is **YMYL (Your Money or Your Life)**. Every factual claim (bonus amounts, game
  providers, payment methods, app availability) **must be verified against the live official site**
  `https://longfubet8888.com/` before publishing. No invented numbers, ever.
- Every page that makes claims carries a visible **"Reviewed by [Author] · Last updated [Date]"**
  byline.
- Include a clear, honest **affiliate disclosure** (dedicated page + short notice on review pages).
- Include **responsible-gambling** messaging and link **Befrienders Malaysia** as the local help
  resource (this is the MY-specific resource — the SG site uses NCPG instead).
- Content is **English only** for this site.
- Written authorisation to use the Longfu88 name/logo/trademarks is provided by the client before
  kickoff — confirm it exists before publishing brand assets.

---

## 5. Site architecture — page map

Per the proposal, each site has **16 SEO content pages + 3 utility pages**. (Note: the proposal's
section header says "43 pages total" while the stat blocks say "32 pages built" — 16×2 sites = 32
content pages. Treat the page map below as canonical and confirm the exact count with the client if
it matters for invoicing.)

### Primary ranking pages (5)
| Page | URL | Word target |
|---|---|---|
| Homepage | `/` | 2,000–2,500 |
| Login & Register | `/login-register` | 1,500–2,000 |
| Bonus & Free Credit | `/bonus` | 1,500–2,000 |
| App Download | `/app-download` | 1,200–1,500 |
| Review & Trust | `/review` | 2,000–2,500 |

### Game category reviews (6) — Malaysia ordering leads with Sportsbook
| Page | URL |
|---|---|
| Sportsbook | `/sportsbook` |
| Live Casino | `/live-casino` |
| Slots | `/slots` |
| Fishing Games | `/fishing-games` |
| P2P Games | `/p2p-games` |
| Esports | `/esports` |

### E-E-A-T trust pages (5)
| Page | URL |
|---|---|
| About Us | `/about-us` |
| Review Methodology | `/methodology` |
| Author Bio | `/author/[name]` |
| Affiliate Disclosure | `/affiliate-disclosure` |
| Responsible Gambling | `/responsible-gambling` |

### Utility pages (3)
`/privacy-policy`, `/terms`, `/sitemap` (plus generate `sitemap.xml` + `robots.txt`).

---

## 6. Target keywords — Malaysia (13)

Tier definitions:
- **Tier 1** — dedicated primary page, full on-page optimisation, link-build target.
- **Tier 2** — captured as secondary intent within supporting pages + FAQ schema.
- **Tier 3** — long-tail capture via FAQ schema and natural content inclusion.

| # | Keyword | Tier | Landing page |
|---|---|---|---|
| 1 | Longfu88 | T1 | Homepage `/` |
| 2 | Longfu88 Malaysia | T1 | Homepage `/` |
| 3 | Longfu88 casino Malaysia | T1 | Homepage `/` |
| 4 | Longfu88 login Malaysia | T1 | `/login-register` |
| 5 | Longfu88 register Malaysia | T1 | `/login-register` |
| 6 | Longfu88 official Malaysia | T1 | Homepage `/` |
| 7 | Longfu88 bonus | T2 | `/bonus` |
| 8 | Longfu88 free credit Malaysia | T2 | `/bonus` |
| 9 | Longfu88 app download Malaysia | T2 | `/app-download` |
| 10 | Longfu88 deposit | T2 | `/login-register` (FAQ) |
| 11 | Longfu88 trusted Malaysia | T3 | `/review` |
| 12 | Longfu88 customer service Malaysia | T3 | `/review` (FAQ) |

> The proposal title states "13 keywords" but the table lists 12 clearly. **Confirm the 13th MY
> keyword with the client** and add it here before finalising the keyword map.

**Geo-signal rule:** "Malaysia" must appear naturally in titles, H1/H2, meta descriptions and body
copy of every primary page. Primary link-build anchor for this site is **"Longfu88 Malaysia"**.

---

## 7. On-page SEO rules (apply to every page)

- Unique, optimised **`<title>`** and **meta description** per page, with the page's target keyword
  cluster and a "Malaysia" geo-signal.
- One **`<h1>`** per page containing the primary keyword; logical **H2/H3** hierarchy with
  secondary keywords. (The official brand site is missing an H1 on its homepage — never repeat that
  mistake here.)
- Geo-signals ("Malaysia") in titles and copy.
- Visible **"Reviewed by [Author] · Last updated [Date]"** byline on review/category pages.
- Internal-linking architecture that pushes authority to Tier-1 priority pages (Homepage,
  Login/Register, Bonus). Every page links contextually to relevant priority pages.
- Descriptive, keyword-aware image `alt` text; clean semantic HTML; canonical tags; OpenGraph tags.
- All bonus amounts, provider names and payment methods **verified against the live official site**.

---

## 8. E-E-A-T architecture (the core differentiator)

Build measurable signals on every dimension:

- **Experience** — every review/category page documents *specific* Longfu88 features with verified
  data: exact provider names, exact bonus amounts, real payment methods. Zero generic filler.
- **Expertise** — a named **author** with stated iGaming industry experience, bylined on every
  review/category page and linked via **Person schema**. A full **Review Methodology** page
  (`/methodology`) explaining the scoring criteria.
- **Authoritativeness** — documented review methodology, transparent affiliate disclosure, specific
  provider/payment references, and internal linking that distributes authority to priority pages.
- **Trust** — SSL by default (Cloudflare), transparent contact info, responsible-gambling resources
  (**Befrienders Malaysia**), and **"Last verified [Date]"** stamps on critical pages.

---

## 9. Schema markup (JSON-LD on the specified pages)

| Schema | Applied to | SERP benefit |
|---|---|---|
| `Organization` | Sitewide, via footer | Brand entity establishment |
| `WebSite` + `SearchAction` | Homepage | Sitelinks search box eligibility |
| `BreadcrumbList` | All non-homepage pages | Rich breadcrumb display |
| `Article` + `Person` | All review & category pages | Author byline in snippets |
| `FAQPage` | Login, Bonus, App, Review pages | FAQ accordion in SERP |
| `Review` + `AggregateRating` | Brand review pages | Star rating display |

Validate every page with **Google Rich Results Test** before marking it done. Keep schema in sync
with on-page content (no schema-only claims).

---

## 10. Repo & file structure (suggested)

```
/
├── CLAUDE.md
├── index.html                 # Homepage
├── login-register.html
├── bonus.html
├── app-download.html
├── review.html
├── sportsbook.html
├── live-casino.html
├── slots.html
├── fishing-games.html
├── p2p-games.html
├── esports.html
├── about-us.html
├── methodology.html
├── affiliate-disclosure.html
├── responsible-gambling.html
├── author/<name>.html
├── privacy-policy.html
├── terms.html
├── sitemap.html
├── sitemap.xml
├── robots.txt
├── CNAME                      # custom domain for GitHub Pages
├── assets/
│   ├── css/                   # compiled Tailwind output
│   ├── js/                    # minimal vanilla JS
│   └── img/                   # logo.png, favicon.ico, screenshots
├── partials/ or _templates/   # shared header/footer/schema snippets (build-time)
└── tailwind.config.js
```

- Keep **shared header, footer, schema and component markup** in reusable templates/partials so the
  16 pages stay consistent. (Static includes via a small build step are acceptable.)
- `CNAME` must contain `longfu88-malaysia.com` for GitHub Pages custom-domain routing.

---

## 11. Build & deploy workflow

1. Develop locally; compile Tailwind to `assets/css`.
2. Commit with clear messages (full commit history is a contractual deliverable).
3. Push to the client-owned GitHub repo → GitHub Pages serves `main`.
4. Cloudflare sits in front for DNS + SSL + Web Analytics.
5. Submit `sitemap.xml` to Google Search Console; request indexing for Tier-1 pages first.

**Prerequisites the client must provide before kickoff (Week 1):** brand colour palette + hex
codes (have it — see §3), brand fonts (Sofia Sans), written trademark authorisation, **domain
registered in client's name**, **Cloudflare account**, and **GitHub account**. Do not assume these
exist — confirm before the build phase.

---

## 12. Reference sites (layout/structure direction only — ignore their branding)

- `https://www.bk8.fishing/`
- `https://bk8myplay.com/`
- `https://bk8-my.org/`

Use these for page structure, section ordering, review-page patterns and trust-signal placement.
Do **not** copy their colours, fonts, logos or text. Never copy copy verbatim from any source —
all content is original.

---

## 13. Timeline & milestones (12 weeks)

- **Month 1 — Foundation, Content & Build**
  - W1: Domain/Cloudflare/GitHub setup, GSC + analytics, keyword collection, content briefs.
  - W2: HTML templates, Tailwind design system, schema templates, responsive components —
    **client approval required before content begins**.
  - W3: **All Malaysia pages written & built; site pushed to production; sitemap submitted; Tier-1
    indexation push.**
  - W4: (Singapore pages built on the other repo; both sites live.)
- **Month 2 — Authority Push & Indexation Monitoring**
  - W5: GSC indexation tracking, Core Web Vitals, schema validation, technical fixes.
  - W6: **1,000 social-profile link build for this site** (USDT 200), anchors on homepage + top-3
    priority pages.
  - W7: First ranking-movement report; internal-linking tweaks from GSC click data.
  - W8: Mid-point report; strategy adjustment; client check-in.
- **Month 3 — Optimisation, Final Push & Handover**
  - W9: On-page tweaks for keywords in positions 11–20; FAQ schema additions from PAA queries.
  - W10: Re-verify bonus details against live offers; refresh top-traffic pages.
  - W11: Handover package prep; "How to Edit Your Site" guide.
  - W12: Final ranking report; **full ownership transfer** (GitHub, Cloudflare, GSC, analytics).

**Expected ranking timeline:** brand keywords on these light-competition SERPs typically reach
page one within 4–6 weeks of clean indexation + backlink execution. Tier-1 is the 90-day primary
target; Tier-2/3 follow from overall authority.

---

## 14. Link-build parameters (Month 2)

- 1,000 social-profile links for this site (USDT 200), built on high-authority platforms for brand
  entity + citation diversity.
- Anchor distribution: **30% branded / 40% partial-match / 20% URL / 10% generic**.
- Concentrate anchors on **Homepage, Login, Bonus**. Primary anchor: **"Longfu88 Malaysia"**.

---

## 15. Deliverables checklist (this site's share)

- [ ] Fully built, responsive, ranking-optimised static HTML site (16 content + 3 utility pages)
- [ ] Original SEO content on every page, all facts verified against the live brand site
- [ ] Complete JSON-LD schema on all ranking pages (validated)
- [ ] E-E-A-T architecture: author bio + Person schema, methodology page, affiliate disclosure,
      responsible-gambling page (Befrienders Malaysia)
- [ ] Google Search Console set up + sitemap submitted + 3-month monitoring
- [ ] Cloudflare Web Analytics configured
- [ ] 3 monthly ranking reports (covering the 13 MY keywords)
- [ ] 1,000 social-profile link build executed (Month 2)
- [ ] GitHub repo with full commit history, transferred to client
- [ ] Handover docs: "How to Edit Your Site" guide, file-structure guide, backup/rollback
      instructions, credentials documented
- [ ] 30-day post-handover bug-fix email support

---

## 16. Quick rules for Claude (do / don't)

**Do:** keep all 16 pages visually and structurally consistent; verify every gambling fact against
`https://longfubet8888.com/`; use the exact brand palette/fonts; one H1 per page; add + validate
schema; write original, specific, non-generic copy; commit frequently with clear messages.

**Don't:** invent bonus amounts/providers/payment methods; hotlink the operator's assets; use a
JS framework or CMS; round corners or break the 4px spacing scale; mix Singapore content into this
repo; claim to be the operator; copy text from reference or competitor sites.
