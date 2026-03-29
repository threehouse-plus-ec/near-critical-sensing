# Near-Critical Sensing

**A project on the epistemology and physics of boundary-sensitive measurement**

U. Warring · Physikalisches Institut, Albert-Ludwigs-Universität Freiburg · 2026

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

---

## What this project is

This project examines sensing and measurement systems that operate near regime boundaries — from 19th-century weather glasses to quantum systems near exceptional points. It asks what kind of knowledge each device produces, and why some sensing modes persist while others are displaced.

The central finding is a distinction between **calibrated state instruments** (invertible: from the reading, one recovers the measured quantity) and **sentinel instruments** (non-invertible: the output amplifies proximity to a transition but cannot be read backwards to recover any single variable). That distinction, first developed historically, turns out to connect directly to modern physics: bifurcation theory, critical slowing down, early warning signals, and non-Hermitian quantum sensing near exceptional points.

## Documents

The project consists of three documents at different stages of completion:

### 1. Historical Dossier: *From Natural Signs to Measurement Networks* (v0.1.3, frozen)

A comprehensive historical survey of atmospheric instruments (15th–19th century) organised by epistemological function across six analytic layers: state, transport, integration, radiation, electrical, and sentinel. Includes primary-source citations, historiographic references, and a detailed timeline.

- **Role:** Coastline (maps the historical territory)
- **Status:** Source-hardened, editorially tightened, frozen
- **Length:** ~12,000 words

### 2. Essay: *Amplifiers at the Boundary* (v0.3.0, circulation-ready)

An interpretive essay arguing that the sentinel tradition was displaced because its devices were non-invertible, and that the question sentinels were trying to answer — *how close is a system to a qualitative change?* — is now central to modern science. Connects storm-glass physics to bifurcation theory, critical slowing down, early warning signals, and non-Hermitian quantum boundary sensing.

- **Role:** Sail (interprets and argues)
- **Status:** Polished, circulation-ready
- **Length:** ~6,500 words

### 3. Quantum Dossier: *Quantum Systems Near Critical Points* (in progress)

A trapped-ion-centred survey of quantum systems near structural, spectral, topological, and dissipative boundaries. Organised by boundary type, not by platform. Includes a dedicated treatment of the EP sensing controversy (signal enhancement vs. noise penalty).

- **Role:** Coastline (technical survey)
- **Status:** Section 0 (Preamble and Definitions) frozen; Section 1 (Structural Boundaries) drafted; Sections 2–8 pending
- **Projected length:** ~18,000 words

## How the documents relate

The **historical dossier** is documentary. It establishes facts, dates, attributions, and sources. Its categories are explicitly marked as analytic rather than actor-native.

The **essay** is argumentative. It takes the sentinel concept from the dossier and develops it into a physics argument about the relationship between sensitivity, invertibility, and proximity to regime boundaries. It is self-contained but references the dossier as a companion.

The **quantum dossier** is technical. It extends the boundary-sensing framework into quantum systems, using trapped ions as the anchor platform. It is standalone — it can be read without the other two documents.

## Repository structure

```
near-critical-sensing/
├── README.md
├── LICENCE.md
├── CITATION.cff
├── MANIFEST.md
├── atmospheric-dossier/
│   ├── dossier-atmospheric-instruments-v0.1.3-FROZEN.md
│   └── drafts/
├── essay/
│   ├── amplifiers-at-the-boundary-v0.3.0.md
│   ├── drafts/
│   └── outlines/
├── quantum-dossier/
│   ├── section0-v0.1.1-FROZEN.md
│   ├── section1-v0.1.0-draft.md
│   ├── outline-v0.1.md
│   └── research-notes.md
└── site/
    ├── index.html
    ├── dossier.html
    ├── essay.html
    ├── css/scholarly.css
    ├── build.py
    ├── README.md
    ├── LICENCE.md
    └── CITATION.cff
```

## How to cite

See `CITATION.cff` for machine-readable citation metadata.

**Historical dossier:**
> Warring, U. (2026). *From Natural Signs to Measurement Networks: A Historical Dossier on Atmospheric Instruments (15th–19th Century)*. Version 0.1.3. https://github.com/threehouse-plus-ec/near-critical-sensing

**Essay:**
> Warring, U. (2026). "Amplifiers at the Boundary: On the Epistemology of Near-Critical Sensing." Version 0.3.0. https://github.com/threehouse-plus-ec/near-critical-sensing

**Quantum dossier (in progress):**
> Warring, U. (2026). *Quantum Systems Near Critical Points: A Boundary-Sensing Taxonomy*. In progress. https://github.com/threehouse-plus-ec/near-critical-sensing

## Licence

This work is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

## Endorsement marker

All documents are local candidate frameworks within the Open-Science Harbour architecture. The taxonomies and analytic categories introduced in these texts do not claim parity with externally validated physical laws. No external endorsement is implied.
