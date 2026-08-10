# SEO Optimization & Site Audit Fix Plan — sanjaygl30ai.vercel.app

This implementation plan addresses all critical, medium, and minor issues identified in the portfolio site audit report and implements the SEO Optimization Package.

## User Review Required

> [!IMPORTANT]
> - **Unified Instagram Handle**: `https://www.instagram.com/me__sanjaygl8123` will be used as the official personal Instagram handle across all pages, schema tags, and AI Knowledge Base. The secondary `code_catalyst_collective` handle will be explicitly labeled as "Dev Content / Tech Collective".
> - **Exact Verified Counts**: Based on dataset analysis of `js/projectsData.js` and `js/certificatesData.js`, the exact counts are **28 Projects** and **86 Certificates**. All pages, meta tags, schema data, and JS count update hooks will be synchronized to `28+ Projects` and `86+ Certificates`.

## Proposed Changes

---

### 1. Assets & Social Preview (`og:image`)

#### [NEW] [og-banner.png](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/assets/og-banner.png)
- Generate a high-resolution 1200×630px PNG banner image for Open Graph and Twitter cards featuring:
  - Dark cyber aesthetic matching portfolio theme (`#0a0f1d`)
  - Sanjay G. L. title, "Full Stack AI Developer & BCA Student"
  - Key statistics badge: `28+ Projects | 86+ Certificates`
  - Clean logo and tech stack highlights

---

### 2. Main Page (`index.html`)

#### [MODIFY] [index.html](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/index.html)
- Trim meta description to ~155 characters for optimal Google search snippet rendering.
- Update Open Graph and Twitter Card tags to use absolute image URL (`https://sanjaygl30ai.vercel.app/assets/og-banner.png`), 1200×630 dimensions, alt text, and `summary_large_image` Twitter card.
- Insert schema.org `Person` JSON-LD structured data before `</head>` with full profile details, alumni info, `sameAs` array, `knowsAbout` skills, and `sanjaygl30ai.vercel.app` canonical domain.
- Unify project counts (`28+ Projects` / `Projects (28)`) and certificate counts (`86+ Certificates` / `Certificates (86+)`).
- Unify Instagram links and clarify social badges.

---

### 3. Projects Page (`projects.html`)

#### [MODIFY] [projects.html](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/projects.html)
- Fix canonical URL to `https://sanjaygl30ai.vercel.app/projects.html`.
- Add full Open Graph and Twitter card meta tags using `og-banner.png`.
- Update Title and Meta Description to match unified `28` projects count.
- Fix header link "View Certificates (102+)" -> "View Certificates (86+)".
- Unify nav link `Projects (28)` and visible count span `28`.
- Add static HTML `<noscript>` / fallback structure containing indexable text for projects so search engine crawlers can index project titles, descriptions, and tech stacks.

---

### 4. Certificates Page (`certificates.html`)

#### [MODIFY] [certificates.html](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/certificates.html)
- Fix canonical URL to `https://sanjaygl30ai.vercel.app/certificates.html`.
- Add full Open Graph and Twitter card meta tags using `og-banner.png`.
- Update Title and Meta Description to match unified `86+` certificates count.
- Fix top nav link "View Projects (23)" -> "View Projects (28)" and footer "Projects (28)".
- Add static HTML fallback containing indexable text for certificates.

---

### 5. Dynamic Count Synchronization Scripts

#### [MODIFY] [js/home.js](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/js/home.js)
#### [MODIFY] [js/projectsPage.js](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/js/projectsPage.js)
#### [MODIFY] [js/certificatesPage.js](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/js/certificatesPage.js)
- Implement dynamic count updater logic on DOM load that calculates `PROJECTS_DATA.length` (28) and `CERTIFICATES_DATA.length` (86) and updates DOM text elements automatically to prevent any future count drift.

---

### 6. Crawl & SEO Files (`robots.txt`, `sitemap.xml`)

#### [MODIFY] [robots.txt](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/robots.txt)
- Ensure clean standard format with `Allow: /` and `Sitemap: https://sanjaygl30ai.vercel.app/sitemap.xml`.

#### [MODIFY] [sitemap.xml](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/sitemap.xml)
- Ensure clean XML urlset for `/`, `/projects.html`, and `/certificates.html` under `sanjaygl30ai.vercel.app`.

---

### 7. AI Knowledge Base & Backend Data

#### [NEW] [assets/agent_knowledge.json](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/assets/agent_knowledge.json)
#### [MODIFY] [knowledge.json](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/knowledge.json)
#### [MODIFY] [app.py](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/app.py)
- Create `assets/agent_knowledge.json` as single source of truth for the Gemini AI assistant.
- Synchronize `knowledge.json` and `app.py` prompt context with exact project details, 28 projects, 86 certificates, and consistent social links.

---

## Verification Plan

### Automated Tests
- Run Python verification script to check:
  - Canonical URLs in all HTML files point to `sanjaygl30ai.vercel.app`.
  - All project count references across HTML/JS match `28` / `28+`.
  - All certificate count references across HTML/JS match `86` / `86+`.
  - `og:image` meta tags use absolute `https://sanjaygl30ai.vercel.app/assets/og-banner.png` path.
  - JSON-LD syntax in HTML files is valid JSON.
  - `assets/og-banner.png` exists and has dimensions 1200×630.

### Manual Verification
- View pages in browser (via local web server or file inspect) to confirm visual count alignment, OG preview meta tags, and structured JSON-LD data.
