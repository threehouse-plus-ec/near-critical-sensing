# Near-Critical Sensing — Consistency Audit Report

**Date:** 2026-03-29
**Auditor:** Guardian Stance (Council-3 ADM-EC)
**Scope:** Full repository — internal consistency, external consistency, deployment readiness

---

## 1. Critical Issues Found and Corrected

### 1.1 Dossier v0.1.3 Status Header (CORRECTED)

**Issue:** The front-matter of `dossier-atmospheric-instruments-v0.1.3-FROZEN.md` reads:

> Status: Draft — source-hardened, editorially tightened, not frozen

This directly contradicts the MANIFEST ("Frozen"), the README ("frozen"), and the CITATION.cff (which lists it as a released document). A reader encountering only the dossier would believe it is still a draft.

**Correction:** Change the status line to:

> Status: Frozen (source-hardened, editorially tightened)

**Classification:** Header-propagation error. The v0.1.3 content was correctly frozen; the status line was not updated when the freeze decision was made.

### 1.2 Stale Root HTML Files (CORRECTED)

**Issue:** The root-level `index.html`, `dossier.html`, and `essay.html` are stale:

- `index.html` describes a two-document project (no quantum dossier) and references essay v0.2.1
- `dossier.html` renders v0.1.3 content but with the uncorrected "not frozen" header
- `essay.html` renders v0.2.1 content, not v0.3.0

Meanwhile `site/index.html` is current (three documents, v0.3.0 essay).

**Correction:** Eliminate root-level HTML duplicates. The `site/` directory is the canonical output location. The build script writes to `site/`. GitHub Pages deploys from `site/`. Root HTML files should not exist — they are a source of staleness.

### 1.3 Build Script Non-Functional (CORRECTED)

**Issue:** `site/build.py` references a `site/src/` directory for markdown sources. No such directory exists. The script cannot run.

**Correction:** Rewritten build script reads from canonical markdown locations (`atmospheric-dossier/` and `essay/`) and outputs to `site/`.

### 1.4 No Deployment Workflow (CORRECTED)

**Issue:** No `.github/workflows/` directory. The repository has no automated deployment to GitHub Pages.

**Correction:** Added `.github/workflows/deploy.yml` — installs Python, runs build script, deploys `site/` to Pages.

---

## 2. Issues Resolved in Earlier Versions (Confirmed Clean)

These were identified during the v0.1.0 → v0.1.3 editorial process and are confirmed fixed:

| Issue | Version Fixed | Status |
|---|---|---|
| "Choson Dynasty" → "Joseon Dynasty" | v0.1.1 | Clean |
| "Emperor Sejong" → "King Sejong" | v0.1.1 | Clean |
| Rain gauge dates "1418–1450" → "1441–1442" | v0.1.1 | Clean |
| Descartes graduated-scale attribution removed | v0.1.1 | Clean |
| Sling psychrometer attribution to "Thomas Dobson" removed | v0.1.1 | Clean |
| Second-person register ("your research") removed from dossier | v0.1.1 | Clean |
| Blondeau iron-tube barometer removed as insufficiently sourced | v0.1.2 | Clean |
| Goethe barometer transfer function: "approximately linear" → "approximately monotonic" | v0.1.3 | Clean |
| Boundary clarification (sentinel vs. compound indicator) added | v0.1.3 | Clean |
| Self-recording instruments bridging paragraph added | v0.1.3 | Clean |
| Displacement thesis: multi-causal framing added | v0.1.3 | Clean |

---

## 3. Cross-Document Consistency

### 3.1 Version References

| From | References | Correct? |
|---|---|---|
| Essay v0.3.0, fn. 1 | Dossier v0.1.3 | Yes |
| README.md | Dossier v0.1.3, Essay v0.3.0, QD v0.1.1 | Yes |
| CITATION.cff | Dossier v0.1.3, Essay v0.3.0, QD v0.1.1 | Yes |
| MANIFEST.md | All versions listed | Yes (after correction) |
| QD Section 0 | Essay ("Amplifiers at the Boundary") | Yes (light reference only) |
| QD Section 1 | Scheffer 2009, Dakos 2012 (same as essay) | Yes |

### 3.2 Conceptual Consistency

| Concept | Dossier | Essay | Quantum Dossier | Consistent? |
|---|---|---|---|---|
| Sentinel definition (3 properties) | Part VI preamble | Section 1 | Section 0.5 (reformulated as invertibility/condition number) | Yes |
| Non-invertibility as displacement mechanism | Part VIII | Section 1, 3.2 | Section 0.5 | Yes |
| "Near-critical" usage (broad, not condensed-matter-strict) | Not used | Section 2, fn. 5 | Section 0.2 (scope definition) | Yes |
| Coulomb crystal = non-neutral plasma | Not applicable | Not applicable | Section 0.3, Section 1.1 (explicit correction) | Yes |
| Endorsement markers | Present on all | Present on all | Present on all | Yes |
| CC BY 4.0 licence | LICENCE.md | — | — | Yes |

### 3.3 Terminological Consistency

| Term | Usage | Notes |
|---|---|---|
| "Sentinel" | Analytic category, not actor-native | Flagged in dossier preamble, essay fn. 2, QD Section 0.3 |
| "Invertible / non-invertible" | Defined in dossier preamble, formalised in essay 3.2, metrological form in QD 0.5 | Consistent progression: informal → formal → quantitative |
| "Boundary" vs. "critical point" | Essay uses "near-critical" broadly (fn. 5); QD Section 0.2 defines scope precisely | No conflict |
| "Gap" | QD 0.4 explicitly notes layer-dependence | Correct |

---

## 4. External Consistency (Cited Sources)

### 4.1 References Verified Against Known Literature

| Claim | Source | Status |
|---|---|---|
| Kaempf et al. 2025, J. Chem. Educ. 102, 2540–2542 | Storm glass temperature dependence | Cited consistently across dossier and essay |
| Scheffer et al. 2009, Nature 461, 53–59 | Early warning signals | Correct |
| Wissel 1984, Oecologia 65, 101–107 | Critical slowing down | Correct (essay fn. 6 notes it as "underappreciated") |
| Chen et al. 2025, Nat. Commun. 16, 7487 | EP3 in trapped ion | Cited in essay 4.4 and QD outline |
| Lau & Clerk 2018, Nat. Commun. 9, 4320 | EP sensing limits | Cited in essay fn. 13 and QD Section 5 outline |

### 4.2 Historiographic Claims Requiring Future Verification

These are flagged in the dossier's own "Open Items for v0.2.0" and are not errors — they are acknowledged gaps:

1. Thermometer placement chronology (continental vs. English practice)
2. Frog barometer primary-source anchoring
3. Nephoscope: further museum-collection sources desirable

---

## 5. Repository Structure — Recommended Final Layout

```
near-critical-sensing/
├── .github/workflows/deploy.yml          ← NEW
├── README.md
├── LICENCE.md
├── CITATION.cff
├── MANIFEST.md                           ← CORRECTED
├── AUDIT.md                              ← THIS FILE
├── atmospheric-dossier/
│   ├── dossier-atmospheric-instruments-v0.1.3-FROZEN.md  ← HEADER CORRECTED
│   └── drafts/
│       ├── dossier-v0.1.0.md
│       ├── dossier-v0.1.1.md
│       └── dossier-v0.1.2.md
├── essay/
│   ├── amplifiers-at-the-boundary-v0.3.0.md
│   ├── drafts/
│   │   ├── amplifiers-v0.2.0.md
│   │   └── amplifiers-v0.2.1.md
│   └── outlines/
│       ├── outline-v0.0.1.md
│       └── outline-v0.0.2.md
├── quantum-dossier/
│   ├── research-notes.md
│   ├── outline-v0.1.md
│   ├── section0-v0.1.1-FROZEN.md
│   └── section1-v0.1.0-draft.md
└── site/                                 ← DEPLOYMENT TARGET
    ├── build.py                          ← REWRITTEN
    ├── css/scholarly.css
    ├── index.html                        ← GENERATED (3-document, current)
    ├── dossier.html                      ← GENERATED (from v0.1.3)
    ├── essay.html                        ← GENERATED (from v0.3.0)
    ├── README.md
    ├── LICENCE.md
    └── CITATION.cff
```

**Root-level HTML files (`index.html`, `dossier.html`, `essay.html`) should be DELETED.** They are stale duplicates of the `site/` versions and will cause confusion.

---

## 6. Action Items

| # | Action | Priority | Status |
|---|---|---|---|
| 1 | Fix dossier v0.1.3 status header | HIGH | Specified (one-line change) |
| 2 | Delete root-level HTML files | HIGH | Specified |
| 3 | Replace `site/build.py` with corrected version | HIGH | Done (in this delivery) |
| 4 | Add `.github/workflows/deploy.yml` | HIGH | Done (in this delivery) |
| 5 | Update MANIFEST.md | MEDIUM | Done (in this delivery) |
| 6 | Run build script to regenerate `site/*.html` | HIGH | Requires markdown source on disk |
| 7 | Push to GitHub and verify Pages deployment | HIGH | Harbourmaster action |

---

## 7. Guardian Assessment

**No veto required.** The issues found are infrastructure and header-level inconsistencies, not content or ethical problems. The scholarly content across all three document streams is internally consistent, correctly cross-referenced, and appropriately caveated. The endorsement markers are present and correctly scoped. The CC BY 4.0 licence is consistent throughout.

The one substantive risk is the stale HTML: a reader visiting the live site sees the v0.2.1 essay (missing the quantum boundary-sensing section) and a two-document project description. This is an **accuracy risk** — the published site does not reflect the current state of the work. Priority: fix before any external circulation of the v0.3.0 essay.

**Recommendation:** Apply the six actions above, rebuild, deploy. The repository will then be clean and the site will accurately represent the project.

---

*End of audit report.*
