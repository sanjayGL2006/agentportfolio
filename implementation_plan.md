# Implementation Plan — Portfolio Update & Premium Enhancement

This plan outlines the professional updates and premium enhancements for Sanjay G. L.'s portfolio website. The focus is to transform the site into a state-of-the-art developer platform without removing any existing projects, achievements, certificates, or animations.

---

## User Review Required

> [!IMPORTANT]
> - **Theme colors:** Nature-inspired colors (emerald green, purple, yellow, orange, coral-pink) will remain primary. Avoid using blue as the primary accent color.
> - **No Rebuilding:** Code updates will build directly on existing HTML files (`index.html`, `projects.html`, `certificates.html`), stylesheet (`css/styles.css`), and Javascript engines (`js/home.js`, `js/projectsPage.js`, `js/certificatesPage.js`, `js/background3d.js`, `js/aiAssistant.js`).
> - **Dockerfile Exclusion:** Docker roadmap will explicitly omit `Dockerfile` and `Deployment Basics`, keeping only requested topics.

---

## Open Questions

- *Are there specific mockup image styles you prefer for the new featured projects (Accident Risk Prediction & Sai AI Assistant)?*
  - **Proposed Approach:** I will generate two high-fidelity dark-themed illustrations for these project backgrounds using our AI image generation engine (`generate_image`) with neon-emerald and purple glows.

---

## Proposed Changes

### Component 1: Core Datasets & Configurations

Modify the local JSON/JS data representations to incorporate the new featured projects, updated statistics, and refined roadmaps.

#### [MODIFY] [projectsData.js](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/js/projectsData.js)
- Add two new featured projects to the top of the `PROJECTS_DATA` array:
  1. **Accident Risk Prediction** (Artificial Intelligence & Machine Learning)
  2. **Sai AI Assistant** (Artificial Intelligence)
- Include metadata properties for these projects such as detailed tech stacks, features, structure modules, statistics, and future roadmaps.

#### [MODIFY] [knowledge.json](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/knowledge.json)
- Update education profile to "3rd Year · 5th Sem" (Bachelor of Computer Applications).
- Update statistics counter values.
- Refine the Docker subtopics list to include: `Containers`, `Images`, `Docker CLI`, `Docker Hub`, `Docker Compose`, `Networking Basics`, `Volumes` (ensure no mention of `Dockerfile`).
- Add the new skills (Machine Learning, Random Forest, Flask, Scikit-learn, Pandas, NumPy, SQLite, SQL, Gemini API, Prompt Engineering, Docker).
- Add the two new projects to the projects list.

---

### Component 2: Stylesheet & Animation Systems

Upgrading styling for premium cards, floating overlays, grids, and introducing missing smooth animations.

#### [MODIFY] [styles.css](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/css/styles.css)
- **Nature Inspired Accents:** Double down on HSL/RGB colors for Emerald Green (`#10b981`), Purple (`#8b5cf6`), Golden-Yellow (`#f59e0b`), Orange (`#f97316`), and Coral-Pink (`#ec4899`). Avoid any blue elements as primary accents.
- **Premium Cards styling:** Add layout styles for the Featured Projects cards, featuring:
  - Gradient animated borders (`@keyframes borderRotate`)
  - Back-glow effect (`box-shadow: 0 0 40px rgba(16,185,129,0.15)`)
  - Glassmorphic backdrop (`backdrop-filter: blur(16px)`)
- **Detailed Dialog Popup:** Style a premium dialog modal (`.premium-modal-overlay`) with backdrop-blur, slide-and-scale animations (`@keyframes modalZoomIn`), close buttons with hover rotations, and multiple content tabs (Overview, Architecture, Features, Structure, Future).
- **New Section Styles:** Add styling for the Research & AI Projects timeline (nodes, links, cards, icons).
- **Core Animations:** Add support for:
  - *Character & Word Reveal animations* (using delay variables)
  - *Ripple Click effect* (`.ripple-effect` with keyframes)
  - *Smooth Page Transition* overlay (`.page-transition-overlay` fade)
  - *3D Tilt variables* (`--rx`, `--ry`)
  - *Certificate card Zoom* and *Glow overlays*.

---

### Component 3: Javascript Engines & Interactive Logic

Upgrading script components to enable premium interactions, chatbot intelligence, and constellation backgrounds.

#### [MODIFY] [projectsPage.js](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/js/projectsPage.js)
- Update card rendering to support the premium featured project layout at the top.
- Add mousemove-listener for **3D Tilt effect** on the featured cards.
- Add modal logic to open the **Premium Dialog Box** when clicking "Read More". The modal will render the detailed layout (image, statistics, overview, architecture, feature lists, modules, structure trees, timeline, etc.).

#### [MODIFY] [home.js](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/js/home.js)
- Call `renderHomeFeaturedCertificates()` inside the `DOMContentLoaded` event listener (fixing the missing render call).
- Update the home page featured projects render layout to include the two new projects at the beginning.

#### [MODIFY] [certificatesPage.js](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/js/certificatesPage.js)
- Update gallery grid rendering to show the Certificate Image (`lh3.googleusercontent.com` drive image), course name, organization, completion day, month, year, credential ID, skills learned, and verification link.
- Enhance the lightbox modal to display the certificate image, using the premium glass-modal design.

#### [MODIFY] [aiAssistant.js](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/js/aiAssistant.js)
- Update chatbot knowledge triggers.
- Support detailed response HTML for queries:
  - *Show Featured Projects*
  - *Tell me about Sai AI Assistant*
  - *Tell me about Accident Risk Prediction*
  - *Show AI Projects*
  - *Show Machine Learning Projects*
- Inject quick links or project cards directly in chatbot answers.

#### [MODIFY] [background3d.js](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/js/background3d.js)
- Update `TECH_OBJECTS` array to contain Python, Flask, Machine Learning, AI Chip, Gemini, Database, SQL, React, JavaScript, Docker, GitHub, Git, Linux, Cloud, and Terminal.
- Implement a **Constellation Effect** on the background canvas: draw thin, faint lines between particles that are close to each other.
- Add **Floating Stars** and subtle mouse reactivity (moving coordinates based on mouse position relative to center).

---

### Component 4: HTML Page Structures

Adding layouts, placeholders, and structure containers.

#### [MODIFY] [index.html](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/index.html)
- Update biography text and degree labels to "3rd Year · 5th Sem" (lines 188, 248, 272).
- Update the Stats Grid to show 8 statistics counters instead of 4, matching the new counts exactly:
  - Projects: 25+
  - Featured Projects: 2
  - AI Projects: 5+
  - Certificates: 70+
  - Technologies: 20+
  - Live Deployments: 8+
  - Machine Learning Projects: 1+
  - AI Assistants: 2+
- Add the **Research & AI Projects** section (Timeline & Modern Cards Layout) on the homepage.
- Add the new skills to the technical skillset section grid.
- Update the Docker showcase to match the specified topics (Images, Containers, Docker CLI, Docker Hub, Docker Compose, Networking Basics, Volumes) and ensure no mention of `Dockerfile`.

#### [MODIFY] [projects.html](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/projects.html)
- Integrate a premium details modal overlay element (`<div id="premiumProjectModal" class="premium-modal-overlay"></div>`).
- Ensure the header stats and descriptions reflect "25+ projects".

#### [MODIFY] [certificates.html](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/certificates.html)
- Ensure title, stats, and description count match the updated profile details.
- Add necessary HTML containers for the upgraded certificate gallery.

---

## Verification Plan

### Automated Tests
- Build verification scripts to test Javascript syntax correctness across updated engines.
- Test endpoint availability and asset loaders.

### Manual Verification
- Deploy a local development server using `http-server` or equivalent node tools.
- Verify on a web browser:
  - 3D Tilt responsiveness on the featured cards.
  - Correct opening, tabs navigation, and animations of the Premium Project Modal.
  - Interactive timeline scrolling in the Research & AI section.
  - Chatbot reactions to the updated query set.
  - Constellation background rendering smoothness and mouse interactions.
  - Search and filter behavior in both projects and certificates pages.
