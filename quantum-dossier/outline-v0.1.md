# Quantum Systems Near Critical Points

## Detailed Dossier Outline (Phase 2)

**Version:** outline-0.1  
**Date:** 2026-03-29  
**Status:** Structural outline — ready for drafting decisions  
**Endorsement Marker:** Local candidate framework (Coastline). The four-layer taxonomy groups physically distinct phenomena by a shared operational feature, not by a unified mechanism. No parity with established theory implied.

---

## Proposed Title

*Quantum Systems Near Critical Points: A Boundary-Sensing Taxonomy*

**Subtitle:** *Structural, spectral, topological, and dissipative boundaries in trapped-ion and comparison platforms*

---

## Register and Audience

- **Register:** Technical-expository throughout. No essayistic passages. Sentinel/perception framing confined to a short synthesis section only.
- **Audience:** Physicist comfortable with open quantum systems, familiar with trapped ions or willing to learn. Comparable to a Physical Review X colloquium or a Rev. Mod. Phys. tutorial section.
- **Relation to other documents:** Standalone. Light reference to the atmospheric-instruments essay ("Amplifiers at the Boundary") in the synthesis section only. Self-contained.

---

## Section 0 — Preamble and Definitions

**~1500 words**

### 0.1 What this dossier is

A trapped-ion-centred survey of quantum systems near structural, spectral, topological, and dissipative boundaries, organised by the type of boundary response being exploited. Not a review of non-Hermitian physics (those exist). Not a review of trapped-ion technology (those exist). A *cross-layer* mapping organised by the shared operational feature: amplified response near a boundary in parameter space.

### 0.2 What counts as "critical" (scope and exclusions)

**Included:** Systems where a control parameter approaches a value at which the system's response to perturbations diverges, a spectral gap closes, or a qualitative change in steady-state structure occurs.

**Excluded:** Generic amplification not tied to a boundary (e.g., simple parametric amplification far from instability). Also excluded: purely Hermitian critical phenomena without an open-system or sensing context (covered by standard quantum phase transition reviews).

### 0.3 The non-equivalence statement

*The four layers are not equivalent physical mechanisms. They are grouped here because they share a common operational feature: amplified response near a boundary in parameter space. Structural transitions involve thermodynamic/many-body physics. Exceptional points concern spectral degeneracies of non-Hermitian effective operators. Topological boundaries involve global spectral invariants (winding numbers, point-gap topology). Dissipative boundaries concern the Liouvillian spectrum and steady-state structure. These are distinct physics, with distinct mathematics, distinct noise properties, and distinct experimental signatures.*

### 0.4 Metrological backbone — key figures of merit

Introduce once, use throughout:

| Concept | Symbol/quantity | Role |
|---|---|---|
| Susceptibility | χ = ∂⟨O⟩/∂λ | Response of observable to parameter change |
| Quantum Fisher information | F_Q(λ) | Ultimate bound on parameter estimation precision (QCRB) |
| Condition number | κ of the parameter-to-observable map | Ratio of sensitivity to noise amplification |
| Petermann factor | K = ⟨ψ_L|ψ_L⟩⟨ψ_R|ψ_R⟩/|⟨ψ_L|ψ_R⟩|² | Excess noise from non-orthogonal eigenmodes (non-Hermitian) |
| Spectral gap | Δ (Hamiltonian or Liouvillian) | Distance to boundary; controls recovery rate |
| Critical slowing down | τ_relax ~ 1/Δ | Divergent relaxation time as gap → 0 |

**The gap-closing table** (unifying axis across layers):

| Layer | Gap that closes | What diverges | Physical mechanism |
|---|---|---|---|
| Structural | Soft mode frequency ω_zigzag → 0 | Susceptibility, fluctuation amplitude | Many-body instability |
| Spectral (EP) | Eigenvalue splitting → 0 (+ eigenvector coalescence) | Eigenvalue response to perturbation (ε^{1/n}) | Non-Hermitian spectral singularity |
| Topological | Spectral gap / winding number change | Directional amplification gain | Point-gap topology, NHSE |
| Dissipative | Liouvillian gap → 0 | Relaxation time, steady-state susceptibility | Dissipative/dynamical phase transition |

### 0.5 Invertibility and condition number

Formal definition: an instrument/sensor mapping f: parameter space → observable space is *operationally invertible* if the condition number κ of the Jacobian ∂f/∂λ is bounded. Near a boundary, κ → ∞: the mapping amplifies both signal and noise. The Petermann factor K quantifies this for non-Hermitian spectral problems; the fidelity susceptibility quantifies it for structural/quantum phase transitions.

*This is the formal version of the "sentinel problem" from the essay — the trade-off between sensitivity and recoverability. Here it is stated in metrological language.*

---

## Section 1 — Structural Boundaries

**~3000 words**

### 1.1 Ion Coulomb crystal phases

Overview of Coulomb crystal configurations in linear Paul traps and Penning traps. Phase diagram: linear → zigzag → helix → shells → 2D/3D crystals. Control parameters: trap anisotropy (aspect ratio α = ω_radial/ω_axial), ion number N, temperature/coupling parameter Γ.

**Key correction maintained:** A Coulomb crystal is already a non-neutral plasma in a strongly coupled, ordered regime. The transitions are within the non-neutral plasma phase diagram (crystalline → liquid-like → cloud-like), not from "crystal" to "plasma."

### 1.2 The linear-zigzag transition as a worked example

The first and best-studied structural transition in ion Coulomb crystals.
- Second-order phase transition (Landau universality class: mean-field ferromagnet ↔ paramagnet)
- Order parameter: transverse displacement of ions from the trap axis
- Soft mode: zigzag mode frequency ω_zz → 0 as α → α_c
- Quantum regime: ground-state-cooled arrays, quantum fluctuations of the soft mode (npj QI 2023)

**Boundary-sensing angle:** Near the critical point, the soft mode susceptibility diverges → the crystal becomes a "sentinel" for perturbations that couple to the transverse degree of freedom. A force that would be negligible deep in the linear phase produces a large structural response near α_c.

**Information-theoretic measures:** Brief mention of fidelity susceptibility, entanglement entropy peaking near the quantum critical point (primarily studied in spin models but applicable in principle to ion chains).

### 1.3 Topological defects and Kibble-Zurek dynamics

Kink solitons created during non-adiabatic quenches across the zigzag transition.
- Kibble-Zurek mechanism: defect density scales with quench rate
- Trapped ions as a test platform for KZM (Mielenz et al. 2013, Ulm et al. 2013)
- Nanofriction and Aubry-type transitions in 2D crystals

### 1.4 Melting and thermal boundaries

Structural transitions driven by temperature rather than confinement:
- Melting of 2D ion crystals (Blinov group, 2025)
- Coupling parameter Γ as the "distance to boundary"
- Intermediate liquid-like states

### 1.5 Comparison: optical lattices and other platforms

- Superfluid–Mott insulator transition in cold atoms: the canonical quantum phase transition with tuneable parameters
- Rydberg atom arrays: structural ordering
- Dusty plasmas / colloidal crystals: classical analogues

### 1.6 Early warning signals in structural transitions

**Bridge to EWS literature:** Can ecological-style early warning signals (rising variance, autocorrelation) be observed in a controlled quantum system approaching the zigzag critical point? This is a natural experimental proposal that connects the dossier to the essay's EWS discussion.

**Key references for Section 1:**
- npj QI 9, 68 (2023) — quantum zigzag
- arXiv:2508.07374 (2025) — ICC review
- Shimshoni, Morigi & Fishman PRL 106, 010401 (2011) — quantum zigzag theory
- Fishman et al. PRB 77, 064111 (2008) — phonon modes
- Kiethe et al. PRB 103, 104106 (2021) — dynamics near transition
- Mielenz et al. PRL 110, 133004 (2013) — topological defects
- Landa et al. NJP 15, 093003 (2013) — solitons
- Mavadia et al. Nat. Commun. (2013) — Penning trap crystals
- Blinov group 2D melting (2025)

---

## Section 2 — Spectral Boundaries (Exceptional Points)

**~3000 words**

### 2.1 Non-Hermitian Hamiltonians and exceptional points

- Open quantum systems → effective non-Hermitian description
- EP definition: eigenvalues AND eigenstates coalesce
- EP vs. diabolic point: eigenstates coalesce at EP, not at DP
- Higher-order EPs: EP3, EP4, …
- PT symmetry and its breaking as a route to EPs

### 2.2 Trapped-ion EP experiments

- **EP3 in dissipative ¹⁷¹Yb⁺:** Chen et al. Nat. Commun. 16, 7487 (2025). Three-level system with engineered loss channels. Non-Hermitian absorption spectroscopy. Quantum state tomography across EP3. Both PT and anti-PT symmetries protect the EP3 within 1D parameter space.
- **Programmable EP4 in ⁴⁰Ca⁺:** Li et al. Quantum Frontiers (2025). Multi-level control with controllable dissipation. Coalescence of EP2s into EP4.
- **Chiral/non-reciprocal state transfer:** Lu et al. Commun. Phys. 8, 91 (2025). Topological state transfers by encircling EPs. Robustness to perturbations demonstrated.

### 2.3 Comparison platforms

- **Photonic systems:** Most mature. Coupled microring resonators, photonic crystals with engineered loss. Enhanced Sagnac sensitivity (Hokmabadi et al. Nature 2019).
- **Superconducting qubits:** Decoherence-induced EPs (Chen et al. PRL 2022). Quantum state tomography across EP (Naghiloo et al. Nat. Phys. 2019).
- **NV centres:** EP in single-spin system (Science 2019).
- **BEC:** Exceptional nexus (PRL 2024).
- **Acoustic/SAW systems:** EP-based gas sensor (Microsyst. Nanoeng. 2025).

### 2.4 What EPs are and are not (for sensing)

**Critical clarification:** The ε^{1/n} scaling refers to *eigenvalue response*, not directly to experimentally accessible observables. Mapping eigenvalue splitting to measured quantities (intensities, frequencies, quadratures) introduces additional noise and readout constraints.

**Key references for Section 2:**
- Wu et al. NSR 12, nwaf144 (2025) — perspective
- Li et al. Nat. Nanotech. 18, 706 (2023) — review
- El-Ganainy et al. Nat. Phys. 14, 11 (2018) — foundational review
- Chen et al. Nat. Commun. 16, 7487 (2025) — EP3 in ions
- Li et al. arXiv:2412.09776 (2025) — EP4 in ions
- Lu et al. Commun. Phys. 8, 91 (2025) — chiral state transfer

---

## Section 3 — Topological Boundaries

**~2500 words**

### 3.1 Non-Hermitian topology beyond EPs

- Point-gap topology: spectral winding number in complex energy plane
- Non-Hermitian skin effect (NHSE): boundary-condition sensitivity, bulk-mode localisation
- Distinction from EP physics: topological properties are *global* spectral features, not local degeneracies

### 3.2 Directional amplification as a qualitatively distinct sensing mode

**Key claim:** Topological systems are not just sensitive — they are *directionally selective* amplifiers. This is qualitatively different from:
- Structural criticality (isotropic susceptibility)
- EP-enhanced response (degenerate, non-directional)

The spectral winding that produces NHSE also fixes the gain and added noise of a topological amplifier (Wanjura, Brunelli & Nunnenkamp framework).

### 3.3 Trapped-ion topological amplifier proposal

arXiv:2502.06960 (2025): parametric ion array with linearly varying modulation phase. Non-Hermitian point-gap topology. Directional amplification of vibrational excitations. Predicted yoctonewton-level force sensitivity for 2–30 ²⁵Mg⁺ ions.

### 3.4 Comparison platforms

- **Photonic lattices:** Most experimental demonstrations of NHSE (optical fibre loops, coupled microring resonators, nonlinearity-driven NHSE in mode-locked lasers)
- **Electrical circuits:** Negative impedance converters
- **Acoustic/mechanical:** Phononic crystals with external circuits

### 3.5 Bridge to Layer 4

The relation between non-Hermitian topology (Hamiltonian spectrum) and Liouvillian topology. Modified bulk-boundary correspondence under decoherence or weak measurement. This is a connection point, not a developed argument — flagged as an active research frontier.

**Key references for Section 3:**
- arXiv:2502.06960 (2025) — parametric ion arrays
- Wanjura et al. Nat. Commun. 11, 3149 (2020) — topological directional amplification
- Wanjura et al. PRL 127, 213601 (2021) — directional amplification with disorder
- Ashida, Gong & Ueda Adv. Phys. 69, 249 (2020) — non-Hermitian physics review
- Bergholtz, Budich & Kunst RMP 93, 015005 (2021) — exceptional topology
- Okuma et al. PRL 124, 086801 (2020) — topological origin of skin effects

---

## Section 4 — Dissipative and Dynamical Boundaries

**~2500 words**

### 4.1 Liouvillian exceptional points

- Liouvillian spectrum: eigenvalues of L in dρ/dt = L[ρ]
- Liouvillian gap: smallest nonzero real part of Liouvillian eigenvalue → controls relaxation rate
- LEPs: spectral degeneracies of the Liouvillian (distinct from Hamiltonian EPs)

**Critical clarification:** Liouvillian exceptional points and dissipative phase transitions are related but distinct. LEPs concern spectral degeneracies; dissipative phase transitions concern qualitative changes in steady-state structure. They can coincide but need not.

### 4.2 Trapped-ion LEP experiments

- **LEP3 from quantum jumps:** Nat. Commun. (2026) — third-order LEPs in a two-level trapped-ion system. Combining decay with dephasing. Quantum jumps generate LEPs even in simple systems.

### 4.3 Quantum Mpemba connection

The quantum Mpemba effect (anomalous relaxation ordering) has been linked to LEPs:
- Mpemba crossing occurs when the relaxation spectrum is reorganised by an LEP
- Zhang et al. Nat. Commun. 16, 301 (2025) — quantum strong Mpemba effect
- Chatterjee et al. PRA 110, 022213 (2024) — multiple quantum Mpemba effect at EPs

**Observable framing:** Non-monotonic relaxation times as a function of initial condition or parameter are a signature that the relaxation spectrum has been reorganised, often via an LEP.

### 4.4 Measurement-induced and trajectory-level transitions

Extending the layer beyond steady-state Liouvillian physics:
- Measurement-induced phase transitions: competition between unitary dynamics and projective measurement drives entanglement phase transitions
- Quantum Zeno-like criticality under continuous monitoring
- Trajectory phase transitions (large-deviation formalism)
- Measurement backaction as a control parameter

### 4.5 Comparison platforms

- **Circuit QED:** Driven-dissipative Bose-Hubbard systems, dissipative phase transitions
- **Cavity BEC:** Dissipative phase transitions in optical cavities
- **Superconducting qubits:** Measurement-induced transitions

**Key references for Section 4:**
- Nat. Commun. (2026) — LEP3 in trapped ion
- Minganti et al. PRA 100, 062131 (2019) — quantum EPs of Hamiltonians and Liouvillians
- Zhang et al. Nat. Commun. 16, 301 (2025) — quantum strong Mpemba
- Chatterjee et al. PRA 110, 022213 (2024) — Mpemba at EPs
- Emergent LEPs from exact principles — Quantum (2025)
- PRX Quantum 4, 030317 (2023) — quantum criticality under decoherence/measurement

---

## Section 5 — The EP Sensing Controversy

**~2000 words**

### 5.1 The promise: enhanced eigenvalue response

- ε^{1/n} splitting near nth-order EP
- Microcavity sensor proposals (Wiersig 2014)
- Enhanced Sagnac sensitivity (Hokmabadi et al. 2019)

### 5.2 The critique: noise penalty

- Lau & Clerk Nat. Commun. 2018: fundamental limits on non-Hermitian quantum sensing
- Quantum noise increases near EP due to non-orthogonal eigenmodes (Petermann factor K → ∞)
- The signal-to-noise ratio may not improve
- Zhang et al. PRL 2019: quantum noise theory of EP sensors
- General sensitivity bounds in QFI/QCRB language

### 5.3 Resolution and current status

- Near-EP operation (not at-EP): balancing amplification against noise
- EP-in-readout architecture: EP implemented in auxiliary control unit, physical sensor left Hermitian. Existence proof that useful sensitivity gains are achievable (Science Advances 2024).
- Non-reciprocity as the genuinely powerful resource (Lau & Clerk)
- Stochastic resonance at higher-order EPs (PRA 2024)
- Current consensus: useful non-Hermitian sensing occurs without requiring exact EP tuning. The field has moved beyond simple pro/anti positions.

### 5.4 What this means for the boundary-sensing framework

The controversy is not about whether boundaries amplify — they do. It is about whether the amplification survives realistic noise and measurement. The answer is nuanced: it depends on the control architecture, the noise model, and whether non-reciprocity is available.

**Key references for Section 5:**
- Wiersig PRL 112, 203901 (2014)
- Hokmabadi et al. Nature 576, 70 (2019)
- Lau & Clerk Nat. Commun. 9, 4320 (2018)
- Zhang et al. PRL 123, 180501 (2019)
- EP-in-readout architecture: Science Advances (2024)
- PRA 22, 054063 (2024) — stochastic resonance at higher-order EPs

---

## Section 6 — Synthesis

**~2000 words**

### 6.1 The boundary-sensing paradigm across layers

Recap the gap-closing table. Each layer is a different physical mechanism producing the same operational signature: amplified response as a gap closes, with attendant degradation of information recoverability.

### 6.2 The invertibility/noise/control triad

Formally:
- **Information recoverability:** condition number κ of the parameter-to-observable map. At boundary: κ → ∞.
- **Fundamental and technical fluctuations:** per-layer identification of fundamental (quantum noise, measurement backaction, FDT constraints) vs. engineering (technical noise, drift).
- **Distance-to-boundary tuning:** per-layer control parameters, tuning range, comparative advantage of trapped ions.

### 6.3 What trapped ions offer uniquely

No other platform offers simultaneous access to all four boundary types with the same level of control:
- Trapping frequencies → structural boundaries
- Engineered dissipation channels → spectral/EP boundaries
- Parametric modulation phases → topological boundaries
- Measurement/monitoring protocols → dissipative/dynamical boundaries

### 6.4 Limitations of boundary sensing

- Finite-size effects (small ion numbers ≠ thermodynamic limit)
- Noise floors (fundamental and technical)
- Hysteresis and irreversibility near first-order boundaries
- Scaling of advantages with system size

### 6.5 Connection to the sentinel framework (brief, ~300 words)

Light reference to the atmospheric-instruments essay. The sentinel concept — amplified response at a boundary with degraded state recovery — finds its quantum analogue in each layer of this dossier. But the quantum setting adds control parameters, statistical readout frameworks, and in some cases topological protection that the 19th-century sentinels lacked.

---

## Section 7 — Metrological Benchmarks Table

**~500 words + table**

| Layer | Susceptibility scaling near boundary | Dominant noise | Known no-go bounds | Experimental SNR demonstration? |
|---|---|---|---|---|
| Structural | χ ~ |λ - λ_c|^{-γ} (mean-field: γ = 1) | Thermal/quantum fluctuations | Standard critical exponent bounds | Quantum zigzag: spectroscopy demonstrated (2023) |
| Spectral (EP) | δE ~ ε^{1/n} (eigenvalue) | Petermann excess noise; K → ∞ at EP | Lau & Clerk (2018): SNR bounds without non-reciprocity | Photonic EP sensors; trapped-ion EP3 spectroscopy |
| Topological | Directional gain ~ exp(N) possible | Added noise fixed by spectral winding | Wanjura framework bounds | Photonic NHSE demonstrations; ion proposal at theory stage |
| Dissipative | τ_relax ~ 1/Δ_L → ∞ | Quantum jump noise, measurement backaction | Under investigation | LEP3 in ions demonstrated (2026); metrology application open |

**Status:** To be populated more fully during drafting. Gaps flagged.

---

## Section 8 — Source Guide

**Annotated bibliography, ~1000 words**

Structured by layer, with 1–2 word tags per entry for navigability:
- [EP sensing bounds], [structural transition], [NHSE perspective], [LEP–Mpemba link], [critical metrology], [topological amplification], [quantum zigzag], [ion EP experiment], …

---

## Word Budget

| Section | Words |
|---|---|
| 0. Preamble and definitions | ~1500 |
| 1. Structural boundaries | ~3000 |
| 2. Spectral boundaries (EPs) | ~3000 |
| 3. Topological boundaries | ~2500 |
| 4. Dissipative and dynamical boundaries | ~2500 |
| 5. EP sensing controversy | ~2000 |
| 6. Synthesis | ~2000 |
| 7. Metrological benchmarks | ~500 |
| 8. Source guide | ~1000 |
| **Total** | **~18,000** |

---

## Open Questions for Drafting

1. **How deep into QFI/QCRB formalism?** The metrological backbone could be a paragraph or a subsection. The audience determines this.
2. **Measurement-induced transitions (Section 4.4):** How much space? This is the newest and least trapped-ion-specific part.
3. **Should the dossier include any original analysis?** E.g., a simple worked calculation of condition number divergence near the zigzag critical point. This would elevate it from survey to something with a research contribution, but also changes the document type.
4. **AG Schätz connection:** How explicit should the link to your group's work be? The Mielenz/Landa papers on topological defects and solitons are directly relevant to Layer 1. The Mpemba programme (with Colla) connects to Layer 4.

---

*End of Phase 2 outline v0.1*
