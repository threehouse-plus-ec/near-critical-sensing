# Quantum Systems Near Critical Points

## A Boundary-Sensing Taxonomy

**Version:** 0.1.1 (Section 0, precision-edited, frozen)  
**Date:** 2026-03-29  
**Status:** Section 0 frozen. Sections 1–8 to follow.  
**Endorsement Marker:** Local candidate framework (Coastline). The four-layer taxonomy groups physically distinct phenomena by a shared operational feature, not by a unified mechanism. No parity with established theory implied.

---

## 0. Preamble and Definitions

### 0.1 What this dossier is

This dossier surveys quantum systems that exhibit amplified response near a boundary in parameter space. It organises these systems not by experimental platform or by theoretical formalism, but by the *type of boundary* being approached and the *response channel that becomes unusually large*.

The survey identifies four layers of boundary physics:

1. **Structural boundaries** — many-body phase transitions in which a spatial or configurational order changes (crystalline → liquid-like, linear → zigzag).
2. **Spectral boundaries** — exceptional points (EPs) of non-Hermitian effective operators, where eigenvalues and eigenstates coalesce.
3. **Topological boundaries** — non-Hermitian topological phases characterised by point-gap invariants, spectral winding, and the non-Hermitian skin effect (NHSE).
4. **Dissipative and dynamical boundaries** — Liouvillian spectral degeneracies, dissipative phase transitions, and measurement-induced criticality.

Trapped-ion systems serve as the anchor platform throughout. They appear in all four layers — as Coulomb crystals near structural instabilities, as engineered non-Hermitian systems near exceptional points, as parametrically driven arrays with topological amplification, and as open quantum systems near Liouvillian degeneracies. Other platforms (photonic, superconducting, cold-atom, acoustic) are treated as systematic comparison points.

This is not a review of non-Hermitian physics (those exist: Ashida, Gong & Ueda 2020; Bergholtz, Budich & Kunst 2021; El-Ganainy et al. 2018). It is not a review of trapped-ion technology (those exist: Leibfried et al. 2003; Bruzewicz et al. 2019). It is a *cross-layer* mapping organised by the operational feature that these otherwise distinct systems share: amplified response near a boundary, often accompanied by the closing or reorganisation of a relevant spectral or dynamical gap.

### 0.2 What counts as "critical" — scope and exclusions

**Included:** Systems where a control parameter approaches a value at which

- a spectral gap closes (soft mode frequency → 0, eigenvalue splitting → 0, Liouvillian gap → 0),
- a spectral topology changes (winding number, point-gap invariant),
- or a qualitative change occurs in the steady-state structure of a driven-dissipative system,

and where this approach produces amplified response to external perturbations with relevance to sensing, metrology, or controlled state preparation.

**Excluded:**

- Generic amplification not tied to a boundary (e.g., parametric amplification far from instability, simple gain in a linear amplifier chain).
- Purely Hermitian quantum critical phenomena treated without an open-system, sensing, or control context. These are covered by the extensive quantum phase transition literature and are not the subject of this dossier.
- General quantum critical metrology. There is a substantial body of work on quantum Fisher information (QFI) and entanglement scaling at quantum critical points in spin models and lattice systems. This dossier draws on that work selectively — for its metrological language and for specific results on the effects of decoherence on critical scaling — but does not attempt to review it. The inclusion criterion here is boundary-linked response with experimental control and readout relevance, not exhaustive coverage of critical many-body estimation theory.

### 0.3 The non-equivalence statement

The four layers are **not equivalent physical mechanisms**. They are grouped here because they share a common operational feature: amplified response near a boundary in parameter space. Specifically:

- **Structural transitions** involve thermodynamic or many-body instabilities. The relevant physics is the softening of a collective mode as a phase boundary is approached. The underlying description is typically Hermitian (or becomes non-Hermitian only through coupling to a thermal bath or measurement apparatus).

- **Exceptional points** concern spectral degeneracies of non-Hermitian effective operators — typically arising from an open-system description in which dissipation, gain, or non-reciprocal coupling is present. At an EP, both eigenvalues *and* eigenstates coalesce, producing a defective (non-diagonalisable) operator. This is a fundamentally different mathematical object from a Hermitian degeneracy (diabolic point), where eigenvalues may coincide but eigenstates remain orthogonal.

- **Topological boundaries** involve global properties of the non-Hermitian spectrum — specifically, the winding of eigenvalues in the complex energy plane (point-gap topology) and the associated boundary-condition sensitivity (NHSE). These are not local spectral degeneracies but topological invariants that characterise the entire band structure.

- **Dissipative and dynamical boundaries** concern the Liouvillian superoperator that governs the full density-matrix dynamics of an open quantum system, including quantum jumps and decoherence. Liouvillian exceptional points (LEPs) are spectral degeneracies of L (not of H_eff), and dissipative phase transitions are qualitative changes in the steady-state structure. These are related to but distinct from Hamiltonian EPs.

These distinctions matter.

A structural soft mode is not an exceptional point. An exceptional point is not a topological phase boundary. A Liouvillian gap closing is not the same as a Hamiltonian gap closing. The taxonomy groups these by operational signature, not by underlying mechanism. When we say "boundary sensing," we mean: the system is near a boundary; the response is amplified; the recoverability of the input signal is degraded. That triad is the common thread. The physics within each layer is distinct.

### 0.4 Metrological backbone — key figures of merit

To compare boundary-sensing performance across layers, the following quantities are used throughout the dossier. They are introduced here and applied consistently in Sections 1–6.

**Susceptibility.** The response of an observable ⟨O⟩ to a change in a control parameter λ:

χ = ∂⟨O⟩/∂λ

Near an ideal continuous boundary, χ may diverge; in finite systems or crossover regimes it typically exhibits a pronounced peak. This growth is the definition of "amplified response." For structural transitions, χ is typically the static susceptibility of the order parameter. For spectral problems, it is the derivative of an eigenvalue or output quadrature with respect to a perturbation. For dissipative boundaries, it is the response of a steady-state observable to a parameter change.

**Quantum Fisher information (QFI).** The fundamental bound on parameter estimation precision via the quantum Cramér–Rao bound (QCRB):

Var(λ̂) ≥ 1 / (N · F_Q(λ))

where N is the number of measurements and F_Q is the QFI. Near a boundary, F_Q can diverge, suggesting enhanced metrological capacity — but this must be assessed alongside noise and practical readout constraints. In the presence of local decoherence, critical scaling of F_Q can revert to standard-quantum-limit behaviour in generic universality classes. This is a clean example of the broader theme of the dossier: boundary-enhanced responsivity does not by itself guarantee a metrological gain once realistic noise is included.

**Condition number.** The conditioning of the parameter-to-observable map f: λ → ⟨O⟩ quantifies how much observational errors are amplified when the parameter is inferred from the measurement. In the multivariate setting, the local conditioning is given by the Jacobian of the map; poor conditioning corresponds to large amplification of observational noise in the inferred parameter. Near a boundary, the conditioning can become very poor — the mapping amplifies both signal and noise. This is the formal version of the "invertibility problem" — the trade-off between sensitivity and recoverability that appears in all four layers.

**Petermann factor.** For non-Hermitian systems with non-orthogonal eigenstates |ψ_R⟩ and ⟨ψ_L|:

K = (⟨ψ_L|ψ_L⟩ · ⟨ψ_R|ψ_R⟩) / |⟨ψ_L|ψ_R⟩|²

K quantifies the excess noise arising from eigenstate non-orthogonality. At an exceptional point, K → ∞ because the left and right eigenstates become parallel (eigenvector coalescence). The Petermann factor is the spectral-boundary analogue of the condition number: it tells you how much noise is amplified alongside the signal. It is most directly relevant in Layers 2 and 3. In Layer 1 (Hermitian structural transitions), related notions of critical sensitivity are captured instead by quantities such as fidelity susceptibility and soft-mode gap suppression.

**Spectral gap.** The gap whose closing defines the boundary. This is a *platform-dependent, layer-dependent* quantity — "gap" is used here as an operational concept, not as a single mathematically identical object across all layers:

| Layer | Gap quantity | What it controls |
|---|---|---|
| Structural | Soft mode frequency ω → 0 | Susceptibility, fluctuation timescale |
| Spectral (EP) | Eigenvalue splitting → 0 (with eigenvector coalescence) | Responsivity to perturbation |
| Topological | Point gap closes or winding number changes | Boundary-mode reorganisation, directional gain |
| Dissipative | Liouvillian gap Δ_L → 0 (smallest nonzero Re(λ_L)) | Relaxation time, steady-state susceptibility |

**Critical slowing down.** The divergence of relaxation time as the gap closes:

τ_relax ~ 1/Δ

This is generic across all four layers (with appropriate definition of Δ) and is the dynamical signature that links boundary sensing to the early-warning-signal literature in complex-systems science. It is also the most experimentally accessible proxy for "distance to the boundary" in many platforms.

**Observable mapping.** The abstract quantities above must be connected to what is actually measured. The mapping is layer- and platform-dependent:

| Layer | Typical trapped-ion observable |
|---|---|
| Structural | Soft-mode quadratures (fluorescence imaging of ion positions), order parameter (transverse displacement) |
| Spectral (EP) | Ramsey-type phase measurement, absorption/emission spectra, quantum state tomography |
| Topological | Displacement amplitude of detector ion (fluorescence at sub-µm resolution) |
| Dissipative | Relaxation curves (fluorescence time traces), steady-state populations |

### 0.5 Invertibility and the boundary-sensing trade-off

A central theme of this dossier is the trade-off between sensitivity and recoverability at a boundary. We formalise this as follows.

A sensing protocol maps a parameter of interest λ onto an observable output O(λ). The protocol is *operationally invertible* if, given a measurement of O with realistic noise, the parameter λ can be recovered with bounded uncertainty. Near a boundary:

- The *sensitivity* ∂O/∂λ diverges (this is the point of boundary sensing).
- The *noise* in O also grows — through the Petermann factor (non-Hermitian), through critical fluctuations (structural), or through quantum measurement backaction (dissipative).
- The *condition number* of the map O(λ) → λ̂ can become very large and may diverge in the idealised critical limit, meaning that the inversion from observed output back to parameter value becomes ill-posed.

This tension formalises the ill-conditioning familiar in numerical linear algebra: a matrix with large singular values may exhibit extreme sensitivity to input perturbations, yielding high responsivity to the quantity of interest while also amplifying noise in the solution. The same structure appears in all four layers:

| Layer | What amplifies sensitivity | What amplifies noise | Why inversion degrades |
|---|---|---|---|
| Structural | Soft mode susceptibility → ∞ | Critical fluctuations, thermal/quantum noise | Multiple input channels (T, geometry, ...) produce similar structural response |
| Spectral (EP) | Eigenvalue response ~ ε^{1/n} | Petermann factor K → ∞; non-orthogonal modes amplify quantum noise | Eigenstates coalesce → output loses directional information |
| Topological | Directional gain ~ exp(N) | Added noise fixed by spectral winding (Wanjura bounds) | Amplification is directional but signal origin may be spatially ambiguous |
| Dissipative | τ_relax → ∞; steady-state susceptibility → ∞ | Quantum jump noise, measurement backaction | Relaxation dynamics carry proximity information but are not uniquely invertible |

An important nuance: the ε^{1/n} eigenvalue response near an nth-order EP refers to *eigenvalue splitting*, not directly to experimentally accessible observables. Mapping eigenvalue response to measured quantities (intensities, frequencies, quadratures) introduces additional noise and readout constraints. Whether the enhanced eigenvalue splitting translates to enhanced signal-to-noise ratio is the subject of an ongoing controversy treated in detail in Section 5.

A further subtlety arises from *spectral instability* in non-Hermitian systems. The pseudospectrum — the set of complex numbers that are ε-pseudoeigenvalues — can be much larger than the ε-neighbourhood of the true spectrum when eigenstates are highly non-orthogonal. This means that infinitesimal perturbations can cause order-one shifts in eigenvalues, a phenomenon partly quantified by the Petermann factor but whose implications for sensing generally require analysis beyond simple eigenvalue perturbation theory. This point is developed further in Section 2.

### 0.6 The role of trapped ions

Trapped-ion systems appear in this dossier not as the only platform for boundary sensing, but as a uniquely versatile anchor. They are among the few platforms that offer unusually direct experimental access to all four boundary classes within a broadly unified control architecture:

- **Structural boundaries:** Coulomb crystal configurations are controlled by trap frequencies (anisotropy ratio α = ω_radial/ω_axial), ion number, and temperature/coupling parameter Γ. The linear-zigzag transition has been characterised in both the classical and quantum regimes.

- **Spectral boundaries (EPs):** Non-Hermitian effective Hamiltonians are implemented through engineered dissipation channels (optical pumping to auxiliary levels with controlled decay rates) and coherent microwave/laser drives. EP3 and higher-order EPs have been observed and characterised via quantum state tomography.

- **Topological boundaries:** Parametric modulation of trapping potentials with spatially varying phase breaks time-reversal symmetry and induces non-Hermitian point-gap topology. Directional amplification of vibrational excitations has been predicted with yoctonewton-level force sensitivity.

- **Dissipative and dynamical boundaries:** Liouvillian exceptional points arise from the interplay of decay and dephasing channels. Quantum jump dynamics generate LEPs even in simple two-level systems. Measurement-induced and monitoring-driven transitions are, at least in principle, accessible in trapped-ion architectures with high-fidelity mid-circuit measurement and feedback.

Other platforms have specific advantages: photonic systems offer faster operation and more mature NHSE demonstrations; superconducting circuits provide stronger nonlinearities and rapid quench capabilities; cold-atom systems offer large particle numbers and continuous tunability. These comparative strengths are noted throughout the dossier, particularly where a result has been demonstrated on another platform but not yet on ions, or where the comparison illuminates the physics.

What trapped ions offer uniquely is the combination of *single-particle-level control and readout* with *tunability across all four boundary types* in a single experimental architecture. This makes them a natural test platform for the cross-layer questions that motivate this dossier: how does boundary-sensing performance compare across different types of boundaries? Do the noise penalties differ? Can topological protection improve recoverability where spectral sensitivity alone cannot?

---

*End of Section 0 (draft). Sections 1–8 to follow.*

---

### Section 0 — Internal checklist (author notes, not for publication)

- [x] Define "boundary" operationally
- [x] Define "gap" carefully, with explicit layer-dependence
- [x] Define "invertibility" in metrological language (condition number)
- [x] State inclusion and exclusion criteria (including: not a general quantum critical metrology review)
- [x] State non-equivalence of layers (with specific examples of what is NOT the same)
- [x] Preview the role of trapped ions without overselling
- [x] Introduce Petermann factor, QFI, susceptibility, critical slowing down
- [x] Connect each figure of merit to a canonical observable
- [x] Flag pseudospectrum/spectral instability for development in Section 2
- [x] Flag decoherence restoring SQL as example of fundamental noise limit
- [x] Flag ε^{1/n} eigenvalue vs. observable distinction for Section 5
- [x] Topological row: "point gap closes or winding number changes" (not conventional gap)
