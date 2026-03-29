# Quantum Systems Near Critical Points

## Literature Survey and Dossier Outline (Phase 1 notes)

**Date:** 2026-03-29  
**Status:** Research notes — not a draft  
**Purpose:** Foundation for a standalone dossier on boundary sensing in quantum systems

---

## Organising Principle

Four-layer taxonomy by boundary type:
1. **Structural boundaries** — many-body phase transitions (crystalline ↔ liquid/disordered)
2. **Spectral boundaries** — exceptional points in non-Hermitian effective descriptions
3. **Topological boundaries** — non-Hermitian topology, point-gap, skin effects, directional amplification
4. **Dissipative boundaries** — Liouvillian EPs, dissipative phase transitions

Anchor platform: trapped ions, with systematic comparison to superconducting circuits, photonics, cold atoms, and acoustic/mechanical systems.

Cross-cutting themes:
- The noise question (does EP-enhanced sensitivity survive quantum noise?)
- The invertibility question (does amplified response degrade state recovery?)
- The control question (tuneable parameters, feedback, readout)

---

## Layer 1 — Structural Boundaries

### Core physics
Ion Coulomb crystals undergo structural phase transitions as trapping parameters are varied. The best-studied is the linear-to-zigzag transition, which is second-order (same universality class as mean-field ferromagnet ↔ paramagnet). Near the critical point, the zigzag soft mode frequency → 0, susceptibility diverges, and the system becomes sensitive to small perturbations.

**Key correction:** A Coulomb crystal is *already* a non-neutral plasma in a strongly coupled, ordered regime. The transition is from crystalline (solid-like) order to liquid-like or cloud-like states of the same non-neutral plasma — not from "crystal" to "plasma."

### Key trapped-ion literature

- **Quantum linear-zigzag transition:** npj Quantum Information 9, 68 (2023) — spectroscopic characterisation in ground-state-cooled arrays of up to 5 ions. Demonstrates stable critical point and majority ground-state occupation crossing the transition. Assesses feasibility for entangled-state interferometry near the critical point.

- **Structural transitions and melting in 2D:** PMC/Atoms 2025 — structural transitions and melting of 2D ion crystals in RF traps. Transitions from lattice arrangements to ring-like formations as temperature increases or trap symmetry changes.

- **Ion Coulomb crystals review:** arXiv:2508.07374 (2025) — comprehensive review of ICC from a condensed-matter perspective. Covers dynamical and thermodynamic properties in 1D, 2D, 3D, out-of-equilibrium behaviour. Includes Landau theory of the linear-zigzag transition.

- **Topological defects (kinks) at structural transitions:** Physica B (2015), Mielenz et al. PRL 110, 133004 (2013) — kink solitons created during non-adiabatic quenches across the zigzag transition. Kibble-Zurek mechanism tests.

- **Penning trap crystal control:** Mavadia et al., Nat. Commun. (2013) — first observation of linear-to-zigzag transition in a Penning trap.

- **AG Schätz context:** Landa et al., New J. Phys. 15, 093003 (2013) — structure, dynamics, and bifurcations of discrete solitons in trapped-ion crystals. Mielenz et al. (2013) — trapping of topological-structural defects. Nanofriction and Aubry-type transitions in self-organised ion crystals. Schätz group website: Coulomb crystal phases, nanofriction, Kibble-Zurek.

### Comparison platforms

- **Cold atoms (optical lattices):** Superfluid-Mott insulator transition. Well-characterised structural/quantum phase transition with tuneable parameters.
- **Rydberg atom arrays:** Structural ordering and phase transitions in programmable arrays.
- **Colloidal crystals / dusty plasmas:** Classical analogues of Coulomb crystal transitions.

---

## Layer 2 — Spectral Boundaries (Exceptional Points)

### Core physics
In open quantum systems with engineered gain/loss, the effective non-Hermitian Hamiltonian can exhibit exceptional points — spectral singularities where eigenvalues *and* eigenstates coalesce. Near an EP, eigenvalue splitting scales as ε^{1/n} for an nth-order EP, suggesting enhanced sensitivity to perturbations.

### EP sensing controversy
Central unresolved question: does the enhanced eigenvalue splitting translate to enhanced signal-to-noise ratio?

- **Pro-enhancement:** Wiersig PRL 112, 203901 (2014) — enhanced sensitivity for microcavity sensors. Hokmabadi et al. Nature 576, 70 (2019) — non-Hermitian ring laser gyroscope with enhanced Sagnac sensitivity.
- **Anti-enhancement / noise penalty:** Lau & Clerk, Nat. Commun. 9, 4320 (2018) — fundamental limits on non-Hermitian quantum sensing. Quantum noise increases near EP, potentially cancelling signal gain. Zhang et al. PRL 123, 180501 (2019) — quantum noise theory of EP sensors.
- **Nuanced position:** Recent work suggests useful sensing can occur near but not exactly at the EP. The optimal operating point balances amplification against noise.

### Key trapped-ion literature

- **EP3 in dissipative trapped ion:** Chen et al., Nat. Commun. 16, 7487 (2025) — quantum tomography of a third-order exceptional point in ¹⁷¹Yb⁺. PT symmetry breaking, non-Hermitian absorption spectroscopy, coalescence of three eigenstates observed.

- **Programmable higher-order EP simulation:** Li et al., Quantum Frontiers (2025), arXiv:2412.09776 — programmable multi-level control in a trapped-ion system. Coalescence of EP2s into EP4. 40Ca⁺ ion with controllable dissipation and coherent drives.

- **Liouvillian EP3 from quantum jumps:** Nat. Commun. (2026) — observation of third-order Liouvillian EPs emerging from quantum jumps in an ultracold two-level trapped-ion system.

- **Chiral/non-reciprocal state transfer near EPs:** Lu et al., Commun. Phys. 8, 91 (2025) — dynamical topology of chiral and nonreciprocal state transfers by encircling EPs in a trapped-ion system.

### Comparison platforms

- **Photonic systems:** Most mature EP platform. Coupled microring resonators, photonic crystals with engineered loss. Li et al. Nat. Nanotech. 18, 706 (2023) — review.
- **Superconducting qubits:** Decoherence-induced EPs (Chen et al. PRL 128, 2022). Naghiloo et al. Nat. Phys. 15, 1232 (2019) — quantum state tomography across EP.
- **Acoustic systems:** EP sensors with coupled SAW resonators (Microsyst. Nanoeng. 2025).
- **NV centres:** EP observation in single-spin system (Science 364, 878, 2019).
- **BEC:** Exceptional nexus observed (PRL 132, 253401, 2024).

### Key reviews

- Wu et al., "Non-Hermitian physics in the quantum regime," Natl. Sci. Rev. 12, nwaf144 (2025) — perspective covering EPs, topology, sensing across quantum platforms.
- Li et al., "Exceptional points and non-Hermitian photonics at the nanoscale," Nat. Nanotech. 18, 706 (2023) — comprehensive review of EP physics.
- El-Ganainy et al., "Non-Hermitian physics and PT symmetry," Nat. Phys. 14, 11 (2018) — foundational review.

---

## Layer 3 — Topological Boundaries

### Core physics
Non-Hermitian topology goes beyond EPs to include point-gap topology, non-Hermitian skin effects (NHSE), and topological amplification. The winding number of the non-Hermitian Hamiltonian in the complex energy plane determines the presence of skin modes and directional amplification.

### Key trapped-ion literature

- **Topological amplification in parametric ion arrays:** arXiv:2502.06960 (2025) — driven-dissipative trapped-ion chain with parametric modulation. Non-Hermitian point-gap topology. Directional amplification for weak-force sensing. Predicted sensitivities ~1 yN/√Hz for 2–30 ²⁵Mg⁺ ions.

- **Floquet engineering in 2D ion architecture:** Recent work (AG Schätz context) — local parametric modulations steering long-range interion couplings and Peierls phases.

### Comparison platforms

- **Photonic lattices:** Most experimental demonstrations of NHSE. Optical fibre loops, coupled microring resonators. Leefmans et al. — nonlinearity-driven NHSE in a laser cavity.
- **Electrical circuits:** Negative impedance converters. Widely used for classical NHSE demonstration.
- **Acoustic/mechanical systems:** Phononic crystals with external circuits.

### Key reviews

- Frontiers of Physics review on topological NHSE (2023) — pedagogical introduction covering modified bulk-boundary correspondence, spectral winding/graph topology, non-Hermitian criticality, dynamical NHSE.
- Ashida, Gong & Ueda, "Non-Hermitian physics," Adv. Phys. 69, 249 (2020) — comprehensive theoretical review.
- Bergholtz, Budich & Kunst, "Exceptional topology of non-Hermitian systems," Rev. Mod. Phys. 93, 015005 (2021).

---

## Layer 4 — Dissipative Boundaries

### Core physics
Dissipative phase transitions occur in driven-dissipative systems where the steady state changes qualitatively as a parameter is varied. The relevant spectral object is the Liouvillian (not the Hamiltonian). Liouvillian exceptional points (LEPs) arise when eigenvalues of the Liouvillian coalesce. Quantum jumps can generate LEPs even in systems whose Hamiltonian part is simple.

### Key trapped-ion literature

- **Liouvillian EP3 from quantum jumps:** Nat. Commun. (2026) — third-order LEPs in a two-level trapped-ion system. Combines decay with dephasing.
- **Quantum Mpemba effect connection:** The quantum Mpemba effect (anomalous relaxation ordering) has been linked to LEPs — Mpemba crossing occurs when the system passes through an LEP that reorganises the relaxation spectrum. Zhang et al. Nat. Commun. 16, 301 (2025) — quantum strong Mpemba effect. Chatterjee et al. PRA 110, 022213 (2024) — multiple quantum Mpemba effect at EPs.

### Comparison platforms

- **Circuit QED:** Driven-dissipative Bose-Hubbard systems. First-order dissipative phase transitions.
- **BEC:** Dissipative BEC in optical cavities. Exceptional nexus.
- **Superconducting qubits:** Decoherence-induced EPs. Quantum state tomography across LEPs.

### Key references

- Minganti et al., PRA 100, 062131 (2019) — quantum EPs of non-Hermitian Hamiltonians and Liouvillians.
- Emergent Liouvillian EPs from exact principles — Quantum journal (2025) — shows LEPs can arise from fundamental dynamics, not just master-equation approximations.

---

## The EP Sensing Controversy — Dedicated Section

This deserves its own treatment. Key structure:

1. **The promise:** ε^{1/n} splitting near nth-order EP → enhanced responsivity.
2. **The critique:** Quantum noise also grows near EP. Fundamental limits (Lau & Clerk 2018). The signal-to-noise ratio may not improve.
3. **The resolution attempts:** Near-EP rather than at-EP operation. Stochastic resonance at higher-order EPs (PRA 2024). Non-reciprocal approaches. Topological protection.
4. **Current status:** Useful non-Hermitian sensing occurs without requiring exact EP tuning. The optimal operating regime is near but not at the EP. The controversy is not fully resolved but the field has matured beyond simple pro/anti positions.

---

## Cross-Cutting Themes

### The invertibility question (from the essay)
Each layer exhibits the same trade-off: response amplified near boundary, interpretability degraded. Structural boundary: susceptibility diverges but mode identification becomes harder. Spectral boundary: eigenvalue splitting enhanced but eigenstates coalesce (loss of orthogonality). Topological: amplification is directional but signal origin may be obscured. Dissipative: relaxation dynamics carry information about proximity to LEP but are not invertible.

### The noise question
Layer 1: Thermal noise. Classical and quantum regimes behave differently near structural transitions. Ground-state cooling changes the character of fluctuations near the zigzag critical point.
Layer 2: Quantum noise fundamental limits (Lau & Clerk). Excess noise from non-orthogonal eigenstates (Petermann factor).
Layer 3: Noise propagation in directional amplifiers. Topological protection of signal-to-noise.
Layer 4: Quantum jump noise. Stochastic unravelling of Liouvillian dynamics.

### The control question
All four layers require control of the bifurcation distance. Trapped ions offer unusually high control: trapping frequencies (structural), engineered dissipation channels (spectral/dissipative), parametric modulation phases (topological).

---

## Proposed Dossier Structure

1. **Preamble** — what this dossier is, the four-layer taxonomy, relation to the atmospheric-instruments tradition (light), standalone status
2. **Layer 1: Structural boundaries** — Coulomb crystal physics, linear-zigzag, melting, kinks, KZM. Trapped-ion centred with optical-lattice comparison.
3. **Layer 2: Spectral boundaries (EPs)** — Non-Hermitian Hamiltonians, EP physics, trapped-ion EP experiments, comparison to photonic/superconducting platforms.
4. **Layer 3: Topological boundaries** — Point-gap topology, NHSE, topological amplification, trapped-ion parametric arrays, comparison to photonic/circuit platforms.
5. **Layer 4: Dissipative boundaries** — Liouvillian EPs, dissipative phase transitions, quantum Mpemba connection, comparison to circuit QED/BEC.
6. **The EP sensing controversy** — signal vs. noise, fundamental limits, near-EP operation, current status.
7. **Synthesis** — the boundary-sensing paradigm across layers, the invertibility/noise/control triad, what trapped ions offer uniquely.
8. **Source guide** — structured bibliography by layer.

**Estimated length:** 15,000–20,000 words  
**Register:** Technical-expository, no essayistic passages. Aimed at a physicist reader comfortable with open quantum systems.

---

## Key References (compiled, by layer)

### Layer 1 — Structural
- npj Quantum Information 9, 68 (2023) — quantum zigzag in ions
- arXiv:2508.07374 (2025) — ICC review (condensed-matter perspective)
- Mielenz et al. PRL 110, 133004 (2013) — topological defects in ion crystals
- Landa et al. NJP 15, 093003 (2013) — solitons in ion crystals
- Shimshoni, Morigi & Fishman PRL 106, 010401 (2011) — quantum zigzag
- Fishman et al. PRB 77, 064111 (2008) — structural transitions, phonon modes
- Kiethe et al. PRB 103, 104106 (2021) — dynamics near zigzag transition
- Mavadia et al. Nat. Commun. (2013) — Penning trap crystal control

### Layer 2 — Spectral (EPs)
- Chen et al. Nat. Commun. 16, 7487 (2025) — EP3 in ¹⁷¹Yb⁺
- Li et al. Quantum Frontiers (2025) arXiv:2412.09776 — programmable EP4 in 40Ca⁺
- Lu et al. Commun. Phys. 8, 91 (2025) — chiral state transfer near EPs in ions
- Wu et al. NSR 12, nwaf144 (2025) — perspective on non-Hermitian quantum regime
- Li et al. Nat. Nanotech. 18, 706 (2023) — EPs at nanoscale (review)
- El-Ganainy et al. Nat. Phys. 14, 11 (2018) — non-Hermitian physics and PT symmetry
- Wiersig PRL 112, 203901 (2014) — EP-enhanced sensing
- Lau & Clerk Nat. Commun. 9, 4320 (2018) — fundamental limits
- Zhang et al. PRL 123, 180501 (2019) — quantum noise theory of EP sensors

### Layer 3 — Topological
- arXiv:2502.06960 (2025) — topological parametric ion arrays
- Wanjura, Brunelli & Nunnenkamp Nat. Commun. 11, 3149 (2020) — topological directional amplification
- Wanjura et al. PRL 127, 213601 (2021) — directional amplification with disorder
- Ashida, Gong & Ueda Adv. Phys. 69, 249 (2020) — non-Hermitian physics review
- Bergholtz, Budich & Kunst Rev. Mod. Phys. 93, 015005 (2021) — exceptional topology

### Layer 4 — Dissipative
- Nat. Commun. (2026) — Liouvillian EP3 in trapped ion (quantum jumps)
- Minganti et al. PRA 100, 062131 (2019) — quantum EPs of Hamiltonians and Liouvillians
- Zhang et al. Nat. Commun. 16, 301 (2025) — quantum strong Mpemba effect
- Chatterjee et al. PRA 110, 022213 (2024) — quantum Mpemba at EPs
- Emergent Liouvillian EPs from exact principles — Quantum (2025)

### General / cross-cutting
- Leibfried et al. RMP 75, 281 (2003) — trapped-ion quantum dynamics
- Bruzewicz et al. Appl. Phys. Rev. 6, 021314 (2019) — trapped-ion QIP review
- Scheffer et al. Nature 461, 53 (2009) — EWS for critical transitions (bridge to essay)

---

*End of Phase 1 notes*
