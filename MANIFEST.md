# Near-Critical Sensing — Project Manifest

## Manifest (2026-03-29, corrected)

This archive contains all current source files for the "Near-Critical Sensing" project.

---

### Atmospheric Instruments Dossier

| File | Version | Status |
|---|---|---|
| `atmospheric-dossier/dossier-atmospheric-instruments-v0.1.3-FROZEN.md` | 0.1.3 | **Frozen** |
| `atmospheric-dossier/drafts/dossier-v0.1.0.md` | 0.1.0 | Superseded |
| `atmospheric-dossier/drafts/dossier-v0.1.1.md` | 0.1.1 | Superseded |
| `atmospheric-dossier/drafts/dossier-v0.1.2.md` | 0.1.2 | Superseded |

**Title:** *From Natural Signs to Measurement Networks: A Historical Dossier on Atmospheric Instruments (15th–19th Century)*
**Role:** Coastline (historical survey)
**~12,000 words**

**Correction note (v0.1.3):** The front-matter status line in the markdown source must read `Status: Frozen (source-hardened, editorially tightened)`. An earlier draft of v0.1.3 contained the status line `Status: Draft — source-hardened, editorially tightened, not frozen`, which contradicted the frozen status declared in the MANIFEST, README, and CITATION.cff. This was a header-propagation error, not a content discrepancy.

---

### Essay: Amplifiers at the Boundary

| File | Version | Status |
|---|---|---|
| `essay/amplifiers-at-the-boundary-v0.4.1.md` | 0.4.1 | **Current draft** (polished) |
| `essay/drafts/amplifiers-v0.3.0.md` | 0.3.0 | Superseded |
| `essay/drafts/amplifiers-v0.4.0.md` | 0.4.0 | Superseded |
| `essay/drafts/amplifiers-v0.2.0.md` | 0.2.0 | Superseded |
| `essay/drafts/amplifiers-v0.2.1.md` | 0.2.1 | Superseded |
| `essay/outlines/outline-v0.0.1.md` | 0.0.1 | Superseded |
| `essay/outlines/outline-v0.0.2.md` | 0.0.2 | Superseded (with perception thread) |

**Title:** *Amplifiers at the Boundary: On the Epistemology of Near-Critical Sensing*
**Role:** Sail (interpretive essay)
**~6,010 words**

---

### Quantum Boundary-Sensing Dossier (in progress)

| File | Version | Status |
|---|---|---|
| `quantum-dossier/research-notes.md` | — | Literature survey and Phase 1 notes |
| `quantum-dossier/outline-v0.1.md` | 0.1 | Detailed outline (Phase 2) |
| `quantum-dossier/section0-v0.1.1-FROZEN.md` | 0.1.1 | **Section 0 frozen** (Preamble and Definitions) |
| `quantum-dossier/section1-v0.1.0-draft.md` | 0.1.0 | Section 1 draft (Structural Boundaries) |

**Title:** *Quantum Systems Near Critical Points: A Boundary-Sensing Taxonomy*
**Role:** Coastline (technical survey)
**Projected ~18,000 words; Sections 2–8 pending**

---

### Site Infrastructure

| File | Description |
|---|---|
| `README.md` | Project README |
| `LICENCE.md` | CC BY 4.0 |
| `CITATION.cff` | Machine-readable citation metadata |
| `MANIFEST.md` | This file |
| `AUDIT.md` | Consistency audit report (2026-03-29) |
| `site/build.py` | Build script: markdown → HTML |
| `site/css/scholarly.css` | Stylesheet |
| `site/index.html` | Landing page (generated) |
| `site/dossier.html` | Dossier HTML (generated) |
| `site/essay.html` | Essay HTML (generated) |
| `site/README.md` | Site-level README |
| `site/LICENCE.md` | Site-level licence |
| `site/CITATION.cff` | Site-level citation metadata |
| `.github/workflows/deploy.yml` | GitHub Pages deployment workflow |

---

### Version History Summary

- **Atmospheric dossier:** v0.1.0 → v0.1.1 (source-hardened) → v0.1.2 (editorially tightened) → **v0.1.3 (frozen)**
- **Essay:** outline v0.0.1 → v0.0.2 (perception thread) → draft v0.2.0 → v0.2.1 (polished) → v0.3.0 (quantum section added) → v0.4.0 (polished) → **v0.4.1 (review response)**
- **Quantum dossier:** research notes → outline v0.1 → **Section 0 frozen (v0.1.1)** → Section 1 draft (v0.1.0)

### Build and Deployment

Run `python site/build.py` from the repository root to regenerate HTML from markdown sources. The GitHub Actions workflow (`.github/workflows/deploy.yml`) runs this automatically on push to `main` and deploys the `site/` directory to GitHub Pages.

**Note:** The build script requires the `markdown` Python package (`pip install markdown`).
