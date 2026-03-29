# From Natural Signs to Measurement Networks

## A Historical Dossier on Atmospheric Instruments (15th–19th Century)

**Version:** 0.1.1  
**Date:** 2026-03-28  
**Status:** Draft — source-hardened, not frozen  
**Endorsement Marker:** Local candidate framework. The six-layer taxonomy (state / transport / integration / radiation / electrical / sentinel) is an analytic category introduced in this dossier to compare instruments by epistemological function. It does not claim parity with externally validated physical laws. No external endorsement is implied.

---

## Preamble

This dossier traces how atmospheric phenomena transitioned from qualitative observation to quantified state variables between roughly 1600 and 1900. It organises instruments not chronologically but by *epistemological function*: what kind of knowledge does each device produce?

The resulting taxonomy — state, transport, integration, radiation, electrical field, and sentinel — reveals that a proto-meteorological observing system existed in hardware well before the mathematical framework (thermodynamics, fluid dynamics, radiative transfer) was in place to interpret it.

**A note on categories.** The categories used here are *analytic* rather than *actor-native*; they are introduced to compare instruments by epistemic function rather than by the terminology used by their inventors or operators. No 19th-century observer would have called a storm glass a "sentinel" or grouped a rain gauge with a sunshine recorder under "integration." These groupings are retrospective and interpretive. Their justification lies in the structural parallels they reveal, not in historical self-description.

A particular focus is placed on *sentinel* instruments: devices that do not measure a calibrated quantity but instead amplify regime changes through nonlinear, high-dimensional system responses. Four such devices are identified and treated in detail.

---

## Part I — Calibrated State Instruments

These instruments measure thermodynamic state variables of the atmosphere: pressure, temperature, and humidity. They share a common epistemological signature — a reproducible, monotonic transfer function between a physical quantity and a readable output — which makes them *invertible*: from the reading, one can recover the state.

### I.1 — The Barometer: Pressure as an Ordering Quantity

**Context:** The vacuum debate and hydrostatics in early 17th-century Italy.

**Key dates and figures:**

- **1643** — Evangelista Torricelli inverts a mercury-filled glass tube in a basin, observing the column stabilise at ~760 mm. He interprets this as evidence that the atmosphere exerts a measurable weight. This is also the first reliably maintained vacuum.
- **1644** — Torricelli communicates his results to Michelangelo Ricci in Florence; the experiment circulates among Italian natural philosophers.
- **1648** — Blaise Pascal convinces his brother-in-law Florin Périer to carry a mercury barometer up the Puy-de-Dôme. The column shortens with altitude, confirming that the mercury is supported by atmospheric pressure, not *horror vacui*. A second barometer monitored at the mountain's base by a local monk provides calibration against ambient pressure fluctuations.
- **~1664** — Robert Hooke develops the wheel barometer, magnifying small pressure changes into needle movement on a dial (each division = 1/100 inch Hg).
- **~1664** — René Descartes applies a graduated scale to the Torricellian tube.
- **1778** — Blondeau develops an iron-tube barometer using narrow-bore musket barrels, producing a durable instrument suited for maritime use.
- **1844** — Lucien Vidie invents the aneroid barometer (sealed metal capsule — later known as the Vidie capsule — deforming under pressure), enabling portable, mercury-free instruments for maritime and field use. The Vidie capsule remains the sensitive element of many modern barometers.

**Epistemological contribution:** The barometer establishes atmospheric pressure as a *state variable* — a single number characterising the local atmosphere at a given moment. This is the first robust link between a local measurement and large-scale atmospheric circulation.

**Adoption trajectory:** Rapid uptake in learned societies (1640s–1660s). By the 18th century, standard equipment for observatories and educated observers. Barometers were among the first instruments to receive printed correction tables for temperature, capillarity, and scale. With the aneroid, accessible to mariners and the public in the 19th century.

**Persistence:** Unbroken to the present day (modern: electronic pressure sensors, MEMS transducers). The mercury column remains a unit of measurement in medicine (mmHg).

**Primary sources:**

- Torricelli, E. (1644). Letter to Michelangelo Ricci, 11 June 1644.
- Pascal, B. (1648). *Récit de la grande expérience de l'équilibre des liqueurs*.

**Historiographic references:**

- Middleton, W. E. K. (1964). *The History of the Barometer*. Johns Hopkins University Press.
- Middleton, W. E. K. (1969). *Invention of the Meteorological Instruments*. Johns Hopkins University Press. Ch. 1.

---

### I.2 — The Thermometer: Temperature as a Universal Scale

**Context:** Experimental natural philosophy in 16th–17th century Italy; the long struggle over standardisation of scales.

**Key dates and figures:**

- **~1593–1612** — Multiple claimants for the air thermoscope: Galileo Galilei, Santorio Santorio, Bartolomeo Telioux (described 1611). Attribution remains contested in the historiography; these dates should be understood as exemplary rather than strictly priority-establishing. These unsealed devices respond to both temperature and pressure, making them qualitative indicators rather than calibrated instruments.
- **Late 17th c.** — Ole Rømer develops a mercury-in-glass thermometer with fixed reference points (brine freezing, body temperature).
- **1714–1724** — Daniel Gabriel Fahrenheit refines the mercury thermometer with a standardised scale (32°F = ice point, 212°F = steam point at standard pressure). His instruments achieve unprecedented reproducibility.
- **1742** — Anders Celsius proposes the centigrade scale (initially inverted: 100° = freezing, 0° = boiling; later reversed, probably by Linnaeus or Strömer).
- **18th c.** — Debate over thermometer placement for representative air-temperature measurement. Continental European observers converge relatively early on north-wall mounting to avoid solar exposure and heat reflection from structures. English practice was less consistent; Henry Cavendish (1776) describes the Royal Society's thermometer hanging from a north-facing window as the best position "the house afforded." (This chronology follows the Jefferson weather-records literature; precise dating would benefit from further verification against Middleton's *History of the Thermometer*.)

**Epistemological contribution:** Introduction of temperature as a *universal, reproducible state variable* T. The thermometer is foundational not merely for meteorology but for the entire edifice of thermodynamics. Virtually every other instrument's reading requires temperature correction.

**Adoption trajectory:** Widely available in science and commerce by the 18th century; standardised scales enable inter-station comparison for the first time. By the late 18th century, precision instruments of high quality were obtainable by those with means, though access remained uneven. When Jefferson urged James Madison to start a weather journal in 1784, Madison replied that he could not begin immediately because he lacked "both a Thermometer and Barometer."

**Persistence:** Unbroken (modern: platinum resistance thermometers, semiconductor sensors, thermocouples).

**Primary sources:**

- Santorio, S. (1612). *Commentaria in artem medicinalem Galeni* (description of clinical thermoscope).
- Fahrenheit, D. G. (1724). "Experimenta & Observationes de Congelatione aquae in vacuo factae," *Philosophical Transactions*, 33, 78–84.

**Historiographic references:**

- Middleton, W. E. K. (1966). *A History of the Thermometer and Its Use in Meteorology*. Johns Hopkins University Press.
- Chang, H. (2004). *Inventing Temperature: Measurement and Scientific Progress*. Oxford University Press.

---

### I.3 — The Hygrometer: Water Vapour as a Second Axis

**Context:** Understanding the role of water in the atmosphere — evaporation, condensation, cloud formation, human physiology.

**Key dates and figures:**

- **Pre-instrumental era** — Folk methods: salt deliquescence, wood swelling, atmospheric visibility changes used as qualitative humidity indicators.
- **17th c.** — René Descartes postulates the presence of water molecules as vapour in air, providing a conceptual framework.
- **~1664** — Robert Hooke designs the first practical mechanical hygrometer.
- **Late 18th c.** — Jean André Deluc uses whalebone (baleen) as a hygroscopic element. Horace-Bénédict de Saussure (~1780–1783) develops the hair hygrometer — a human hair under tension, scaled 0 (very dry) to 100 (saturated). Simple, cheap, portable; it became the standard in weather networks for decades.
- **Late 18th – early 19th c.** — Development of psychrometric methods (wet-bulb / dry-bulb thermometer pairs) for physically grounded humidity measurement via evaporative cooling. The sling psychrometer, in which the thermometer pair is whirled through the air to ensure ventilation, emerges in this period. (Specific attributions for the earliest psychrometers vary in the literature and should be treated with caution.)
- **19th c.** — John Frederic Daniell (1820) and Henri Victor Regnault develop dew-point hygrometers, offering a direct measure of the temperature at which condensation occurs.

**Epistemological contribution:** Adds a *second thermodynamic axis* (humidity, or equivalently vapour pressure / dew point) to the atmospheric state description. Opens access to phase transitions of water — condensation, cloud formation, precipitation — the most energetically important processes in the atmosphere.

**Adoption trajectory:** Saussure's hair hygrometer was widely deployed in 18th–19th century networks. The psychrometer gradually gained preference for its physical transparency (direct connection to latent heat of evaporation). Both coexisted well into the 20th century.

**Persistence:** High. Modern sensors: capacitive thin-film hygrometers, chilled-mirror dew-point sensors, optical absorption hygrometers.

**Primary sources:**

- Saussure, H.-B. de (1783). *Essais sur l'hygrométrie*. Neuchâtel.
- Daniell, J. F. (1820). "On a new register-hygrometer," *Quarterly Journal of Science*, 8, 280–290.

**Historiographic references:**

- Middleton, W. E. K. (1969). *Invention of the Meteorological Instruments*. Ch. 3 (Humidity).
- Golinski, J. (2007). *British Weather and the Climate of Enlightenment*. University of Chicago Press.

---

## Part II — Transport and Dynamics Instruments

These instruments measure *fluxes* — the movement of air and clouds — rather than local state variables.

### II.1 — Wind Vane and Anemometer

**Context:** Wind knowledge is essential for agriculture, navigation, and military operations; it is among the oldest meteorological observations.

**Key dates and figures:**

- **~1450** — Leone Battista Alberti proposes an improved wind vane with a swinging plate to estimate wind force from deflection angle.
- **~1664** — Robert Hooke develops an anemometer measuring both wind direction and force.
- **1806** — Francis Beaufort introduces his scale for classifying wind speeds based on observable sea-state effects — a qualitative-to-semi-quantitative bridge that provided a universal language for maritime observers lacking instruments.
- **1846** — Thomas Romney Robinson introduces the cup anemometer (hemispherical cups on horizontal arms rotating around a vertical axis), providing a mechanical integration of wind speed. This design dominates for over a century.

**Epistemological contribution:** Quantification of atmospheric *transport*: how fast and in which direction air (and with it, heat, moisture, and momentum) moves. Wind data is the kinematic complement to the thermodynamic state.

**Adoption trajectory:** Wind vanes are ancient; cup anemometers became standard in the 19th century.

**Persistence:** Continuous. Modern: ultrasonic anemometers, Doppler lidar, satellite-derived winds.

**Historiographic references:**

- Middleton, W. E. K. (1969). *Invention of the Meteorological Instruments*. Ch. 5 (Wind).

---

### II.2 — Nephoscope: Cloud Motion and Height

**Context:** Clouds are visible tracers of upper-air flow, but their altitude and speed are difficult to determine without triangulation.

**Key dates and figures:**

- **1862–1880s** — Various mirror-based nephoscopes developed for determining cloud direction, speed, and (by triangulation) altitude.
- **1886** — Carl Gotfried Fineman designs a widely used mirror nephoscope with a compass ring, allowing the observer to track a cloud's reflection and determine its azimuth and apparent angular velocity. Described in *Zeitschrift für Instrumentenkunde*, 6 (1886), 206–208. An unsigned example was transferred from the U.S. Weather Bureau to the Smithsonian in 1904.
- **1890s** — Charles F. Marvin develops the comb nephoscope for the U.S. Weather Bureau: a row of vertical rods through which the observer tracks cloud motion against the sky. Paired observers can triangulate altitude.
- **1896** — The International Cloud Year: photogrammetric methods (paired cloud cameras on alt-azimuth mounts) developed for systematic cloud observation, leading toward the *International Cloud Atlas* (first edition 1896).

**Epistemological contribution:** Access to upper-air dynamics *before* the radiosonde era. The nephoscope is a remarkable example of using a naked-eye observation (cloud position) combined with a calibrated instrument to extract quantitative transport data.

**Adoption trajectory:** Standard in late-19th-century observatories. The experimental/demonstration status of many nephoscopes should be noted: they were typically deployed at well-staffed observatories, not at routine weather stations.

**Persistence:** Effectively extinct as an operational tool. Replaced by remote sensing (satellite cloud tracking, Doppler radar, lidar).

**Historiographic references:**

- Middleton, W. E. K. (1969). *Invention of the Meteorological Instruments*. Ch. 8 (Upper Winds and Clouds), pp. 271 ff.
- Fineman, C. G. (1886). *Zeitschrift für Instrumentenkunde*, 6, 206–208.
- WMO (2017). *International Cloud Atlas* (revised edition). — For the broader context of cloud classification and observation.

---

## Part III — Integrative / Result Instruments

These instruments measure *accumulated outcomes* — precipitation, evaporation, sunshine duration — rather than instantaneous state or flux.

### III.1 — Rain Gauge (Pluviometer)

**Context:** Rainfall is the most agriculturally consequential atmospheric quantity. Its measurement has very ancient roots.

**Key dates and figures:**

- **1441–1442** — Joseon Dynasty Korea (King Sejong): the *ch'ŭgugi* (측우기), calibrated bronze rain gauges, are distributed to provincial offices across the kingdom. The term appears in the *Veritable Records of the Joseon Dynasty* from 1442. This represents arguably the first national, standardised precipitation observation network, predating European equivalents by centuries.
- **1662** — Christopher Wren designs a tipping-bucket rain gauge in England.
- **18th–19th c.** — Standardised cylindrical gauges with graduated collection vessels become the norm in European and American networks.

**Note on attribution:** For early rain gauges, as for thermoscopes and water barometers, attribution and priority remain contested in the historiography. The Korean *ch'ŭgugi* system is well documented in the Veritable Records, but claims about earlier or parallel developments elsewhere should be treated as exemplary rather than exhaustive.

**Epistemological contribution:** The rain gauge integrates a complex atmospheric process (condensation, coalescence, fallout) into a single result quantity: depth of water per unit area per unit time.

**Adoption trajectory:** Ancient in concept; standardised in the 18th–19th century.

**Persistence:** Continuous. Modern: tipping-bucket (automated), weighing gauges, disdrometers (drop-size distribution), and weather radar for spatial coverage.

**Primary source:**

- *Veritable Records of the Joseon Dynasty* (*Joseon Wangjo Sillok*), entries from 1442 referencing *ch'ŭgugi*.

**Historiographic references:**

- See the entry on *Ch'ŭgugi* in Korean meteorological historiography for synthesis of the Joseon rain-gauge programme.

---

### III.2 — Atmometer (Evaporimeter)

**Context:** Evaporation is the atmospheric water cycle's return leg — crucial for agriculture, hydrology, and understanding the surface energy balance.

**Key figures:** Various designs from the 18th century onward; standardised "pan evaporation" measurements emerge in the 19th century.

**Epistemological contribution:** Measures the rate of water loss to the atmosphere, a quantity determined jointly by temperature, humidity, wind, and radiation — making it a de facto *compound* indicator.

**Persistence:** Standard in agricultural meteorology and hydrology (Class A evaporation pan); declining in operational use as Penman–Monteith calculations from state variables replace direct measurement.

**Historiographic references:**

- Middleton, W. E. K. (1969). *Invention of the Meteorological Instruments*. Ch. 4 (Rain Gauge and Atmometer).

---

### III.3 — Sunshine Recorder (Campbell–Stokes)

**Context:** The desire to quantify solar radiation duration for agriculture, climatology, and the emerging interest in the atmospheric energy budget.

**Key dates and figures:**

- **1853** — John Francis Campbell (Scottish scholar, Secretary to the Lighthouse Commission) invents the sunshine recorder: a water-filled glass sphere focusing sunlight onto a surface, charring it during bright sunshine.
- **1879** — Sir George Gabriel Stokes (Cambridge physicist) refines the design: solid glass sphere (~10 cm diameter, refractive index ~1.52), metal housing, standardised curved recording cards (three overlapping sets for seasonal adjustment). The Campbell–Stokes recorder enters routine meteorological use.
- **Operational from 1880s** — Continuous records at sites including Blue Hill Observatory (Massachusetts, from 1886) and Kew Observatory (London). Some stations have maintained parallel Campbell–Stokes records for over 120 years.

**Epistemological contribution:** The first routine measurement of a *radiative* quantity — sunshine duration. While not a direct irradiance measurement (it records only whether direct beam exceeds ~120 W/m²), it provides a binary proxy for the atmospheric radiation budget. It partially closes the "missing axis" in a purely thermodynamic observing system: the energetic driving side.

**Operational vs. experimental status:** The Campbell–Stokes recorder clearly entered long-term routine operation at hundreds of stations worldwide, unlike several sentinel devices which remained experimental or one-off constructions.

**Adoption trajectory:** Rapidly adopted worldwide from the 1880s. WMO standardisation followed; the Interim Reference Sunshine Recorder (a standardised Campbell–Stokes variant) serves as a benchmark.

**Persistence:** Still in use at heritage stations for record continuity and homogenisation studies. Gradually supplemented and replaced by electronic pyranometers, pyrheliometers, and purpose-built sunshine-duration sensors.

**Primary source context:**

- Campbell's 1853 design is documented in museum and encyclopaedia accounts (Royal Museums Greenwich collection, object 10932). Stokes's 1879 refinement is described in period literature and subsequent WMO publications.

**Historiographic references:**

- Stanhill, G. (2003). "Through a glass brightly: Some new light on the Campbell–Stokes sunshine recorder," *Weather*, 58, 3–11.
- Middleton, W. E. K. (1969). *Invention of the Meteorological Instruments*. Ch. 6 (Sunshine).

---

## Part IV — Radiation Instruments

This category addresses the "missing axis" from a purely thermodynamic instrument set: the *energetic driving side* of atmospheric processes.

### IV.1 — Pyrheliometer and Actinometer

**Context:** Quantifying the Sun's energy input to the Earth — essential for understanding the atmospheric heat engine.

**Key dates and figures:**

- **~1837–1838** — Claude Pouillet designs an early pyrheliometer and uses it to estimate the solar constant (~1228 W/m², subsequently revised upward). This is one of the first quantitative estimates of solar irradiance at the top of the atmosphere.
- **1893** — Knut Ångström develops the electrical compensation pyrheliometer: a blackened strip absorbs solar radiation; the temperature rise is matched by electrically heating an adjacent strip. The balancing current gives a direct measure of irradiance in physical units. This design becomes the reference standard for solar radiation measurement.
- **Late 19th c.** — Pyranometers (hemispherical irradiance, both direct and diffuse) and pyrgeometers (longwave infrared) gradually enter the observational repertoire.

**Epistemological contribution:** Direct quantification of the atmospheric energy input in physical units (W/m²). This completes the thermodynamic picture: state (T, p, RH), transport (wind), result (rain), and now *forcing* (radiation).

**Adoption trajectory:** Specialist instruments in the late 19th century; operational networks from the early 20th century (e.g., International Radiation Commission).

**Persistence:** Foundational. Modern solar radiation networks (BSRN) use thermopile pyrheliometers and pyranometers traceable to Ångström's design.

**Historiographic references:**

- Pouillet's work is cited in later histories of solar radiation instruments; see Middleton (1969), Ch. 6 for context.

---

## Part V — Atmospheric Electricity Instruments

An entire measurement axis sitting *outside* the thermodynamic state variables, reflecting the atmosphere's electrical structure.

### V.1 — Electroscope, Electrometer, and Lightning Detection

**Context:** The 18th-century discovery that the atmosphere is electrically charged, and the identification of lightning as an electrical discharge.

**Key dates and figures:**

- **1746–1752** — Benjamin Franklin's systematic experiments. He observes by 1749 that lightning possesses nearly all properties observable in electrical machines. In July 1750, he hypothesises that electricity can be drawn from clouds via a tall, sharp-pointed metal aerial.
- **1752** — Thomas-François Dalibard erects a 12-metre iron rod at Marly-la-Ville near Paris, drawing sparks from a passing cloud — confirming Franklin's hypothesis before Franklin's own kite experiment later that year.
- **1753** — Georg Wilhelm Richmann killed in St Petersburg while experimenting with an electroscope during a thunderstorm — a vivid and tragic demonstration of the phenomenon's reality.
- **Mid-18th c.** — Jean-Antoine Nollet and others build electroscopes (pith-ball, gold-leaf) to detect atmospheric charge. Fair-weather electricity discovered independently by Le Monnier, Canton, and Beccaria — establishing that the atmosphere carries charge even in the absence of storms.
- **~1810 onward** — Francis Ronalds begins continuous automated recording of atmospheric potential gradient and air–earth currents, first privately, then as inaugural Honorary Director of Kew Observatory (1840s). Kew produces the first extended and comprehensive dataset of electrical and meteorological parameters, and Ronalds supplies equipment to facilities worldwide.
- **1860s** — Lord Kelvin (William Thomson) introduces the water-dropper collector and divided-ring electrometer at Kew Observatory, enabling precision measurements of the fair-weather electric field. Atmospheric electricity remains a speciality of Kew until its closure.
- **1895** — Alexander Stepanovich Popov devises a lightning detector using a coherer receiver (based on Édouard Branly's 1890 design), installed at the meteorological observatory of the Forest Institute in St Petersburg. This is an early precursor to radio-based remote sensing.

**Epistemological contribution:** Opens a non-thermodynamic window onto atmospheric processes. Atmospheric electricity is linked to thunderstorm activity, aerosol content, cosmic ray flux, and fair-weather global circulation (the "Carnegie curve" of diurnal potential-gradient variation). FitzRoy himself attributed part of the storm glass's response to "electrical tension" — a hypothesis not supported by modern evidence, but one reflecting the period's active interest in this measurement axis.

**Adoption trajectory:** Specialist research instrument in the 18th–19th century; atmospheric electricity never became a routine element of standard meteorological stations in the way T, p, and RH did. Lightning detection networks became operational only in the mid-to-late 20th century.

**Persistence:** Research-active but operationally niche. Modern: field mills, point-discharge sensors, satellite-based lightning mappers (GLM on GOES-16/17), ground-based networks (NLDN, EUCLID).

**Primary sources:**

- Franklin, B. (1751). *Experiments and Observations on Electricity*. London.
- Ronalds, F. (various, 1810s–1860s). Papers and reports from Kew Observatory.

**Historiographic references:**

- Harrison, R. G. (2004). "The global atmospheric electrical circuit and climate," *Surveys in Geophysics*, 25, 441–484.
- Harrison, R. G. (2011). "Fair weather atmospheric electricity," *Journal of Physics: Conference Series*, 301, 012001.

---

## Part VI — Sentinel Instruments: Nonlinear Amplifiers of Regime Change

This is the most analytically distinctive category in this dossier. It is *not* a historical actor-category — no 19th-century instrument-maker would have used the term "sentinel." It is introduced here to group devices that share three defining characteristics:

1. **Nonlinear response:** The output is not proportional to any single input variable; it exhibits thresholds, bifurcations, or phase transitions.
2. **High-dimensional integration:** The device responds to a *bundle* of environmental variables (temperature, temperature history, pressure, humidity, nucleation conditions, biological state) simultaneously, without separating their contributions.
3. **Non-invertibility:** From the output (crystal pattern, bell strike, frog position), one cannot uniquely reconstruct the atmospheric state. The transfer function is many-to-one.

What sentinels *do* provide is sensitivity to *regime transitions* — an early-warning capacity that linear, calibrated instruments, precisely because they are designed for smooth monotonic response, may underemphasise.

Four historical sentinels are identified below, ordered from most mechanistic (Goethe barometer) to most biologically complex (frog barometer).

---

### VI.1 — The Goethe Barometer (Donderglas / Thunder Glass / Water Barometer)

**Type:** Qualitative pressure indicator with temperature contamination.

**Context:** An early weather-glass predating the widespread dominance of the Torricellian mercury barometer.

**History:**

- **Origins:** The water barometer (a sealed glass body with an open spout, half-filled with water) dates to the 16th–17th century. Attribution is contested: some sources credit Torricelli or his circle; others point to the Dutch nobleman Gheijsbrecht de Donckere. The Dutch version was known as the *Donderglas* (thunder glass). It should be noted that while this device responds to atmospheric pressure, it is not a fully equivalent predecessor of the mercury barometer in the strict metrological sense — it provides only qualitative indication of pressure *changes*, not absolute measurements.
- **Goethe connection:** When Johann Wolfgang von Goethe died in Weimar in 1832, a water-filled glass vessel was found on his bedroom wall. His well-known interest in natural science led to the assumption — incorrect — that he had invented it. The name "Goethe barometer" stuck, despite being based on a misattribution. Goethe likely encountered the device during his travels and popularised it in German-speaking regions. Museum sources support the view that the later Goethe attribution is culturally amplified rather than inventorially secure.
- **American variant:** The Pilgrims probably brought the thunder glass to America in the 1620s, where it became known as a *Cape Cod weather glass* or *thunder bottle*. It was popular with fishermen and farmers through the 19th century.

**Operating principle:** A sealed glass body contains trapped air; a narrow spout open to the atmosphere extends from below the waterline. Changes in atmospheric pressure shift the water level in the spout: falling pressure raises the water (potentially overflowing = storm warning); rising pressure pushes it down. However, the trapped air also expands and contracts with temperature, introducing a systematic confound. The device gives only qualitative indication of pressure *changes* — no absolute reading, no numbers.

**Epistemological role:** The Goethe barometer sits at the boundary between instrument and sentinel. It responds to a real physical variable (pressure), but its temperature sensitivity and lack of calibration make its signal ambiguous. It is the *least* nonlinear of the sentinels — its transfer function is in principle monotonic for pressure — but the temperature contamination breaks the invertibility condition, preventing unique reconstruction of either T or p from the water level alone.

**Persistence:** Displaced by mercury and aneroid barometers for any serious purpose. Survives today as a decorative and educational object.

---

### VI.2 — The FitzRoy Storm Glass (Chemical Weather Glass)

**Type:** Nonlinear crystallisation amplifier near the solubility limit.

**Context:** Maritime practice and the search for simple visual storm warnings.

This section separates three claims that are often compressed in popular accounts:

**(a) Historical popularity.** The storm glass existed before FitzRoy — variants with camphor-based solutions appeared in Italy, France, and Germany from at least the 1830s or 1840s. But it was FitzRoy who promoted it systematically:

- **1831–1836** — Robert FitzRoy, as captain of HMS *Beagle* (with Charles Darwin aboard), reportedly observed storm glasses during the voyage.
- **1859** — The Royal Charter storm (25–26 October 1859) kills over 800 people at sea. This catastrophe motivates FitzRoy's storm-warning system, of which the storm glass is one element.
- **1860s** — FitzRoy, now head of the Meteorological Department of the Board of Trade (forerunner of the Met Office), actively distributes storm glasses to fishing communities along the British coast. He publishes detailed interpretation charts in *The Weather Book* (1863):
  - Clear liquid → clear weather
  - Cloudy liquid → cloudy skies, possible rain
  - Small dots → fog or humidity
  - Cloudy with small stars → thunderstorms
  - Large flakes → overcast or snow (winter)
- **Late 19th c.** — Scientific scepticism grows. FitzRoy is under pressure; he dies in 1865. Storm glasses are gradually displaced by affordable mercury barometers.

**(b) Modern physical interpretation.** Recent experimental work, notably a 2025 paper in the *Journal of Chemical Education* (Hiroshima University), supports the view that storm-glass behaviour is strongly temperature-linked: camphor solubility in ethanol–water mixtures is strongly temperature-dependent, and the crystallisation/dissolution cycle tracks temperature changes with pronounced hysteresis. The device behaves primarily as a crude, thermally driven crystallisation indicator.

**(c) Remaining underdetermination.** The 2025 paper addresses simplified storm-glass formulations under controlled conditions. Historical storm-glass mixtures were multi-component (camphor, potassium nitrate, ammonium chloride in ethanol–water), not always standardised, and subject to ageing, mechanical disturbance, and thermal-gradient effects within the glass. FitzRoy himself attributed part of the response to "electrical tension" in the atmosphere — a claim without modern support, but one that reflects the period's interest in atmospheric electricity (cf. Part V). A fully settled account of all historical formulations of FitzRoy-style glasses would require broader experimental work than is currently available.

**Composition (typical):** Distilled water, ethanol, potassium nitrate (KNO₃), ammonium chloride (NH₄Cl), and camphor (C₁₀H₁₆O) — a multi-component solution near its saturation limit.

**Operating principle:** As temperature drops, camphor solubility in the ethanol–water mixture decreases, driving the solution past saturation. Crystallisation nucleates and grows, producing visually striking patterns (needles, ferns, stars). Warming redissolves the crystals. The system operates near a *metastable phase boundary* — small environmental changes can trigger large visible responses. However, the response depends on the full thermal history (hysteresis), mechanical disturbance, and surface nucleation conditions.

**Epistemological role:** The storm glass is a *system-response indicator*, not a state-variable meter. It amplifies — but also mixes — multiple inputs (temperature, rate of temperature change, thermal gradients across the glass, possibly convective currents within the liquid). The signal cannot be inverted to recover any single atmospheric quantity. This makes it scientifically intractable but perceptually compelling: it *shows* that something is changing, even if it cannot say what.

**Persistence:** Scientifically displaced by the late 19th century. Survives as a decorative object and educational demonstration of supersaturation/nucleation phenomena.

**Primary source:**

- FitzRoy, R. (1863). *The Weather Book: A Manual of Practical Meteorology*. London: Longman.

**Modern scientific analysis:**

- Kaempf, N. et al. (2025). "The Storm Glass Thermometer: Temperature Dependence of Camphor Crystal Formation in Ethanol," *Journal of Chemical Education*, 102(6), 2540–2542.

---

### VI.3 — The Tempest Prognosticator (Leech Barometer)

**Type:** Biological sentinel using animal behaviour as a storm detector.

**Context:** Victorian natural philosophy and the belief that animal instinct could be harnessed for scientific purposes.

**History:**

- **1850** — George Merryweather, physician and honorary curator of the Whitby Literary and Philosophical Society museum, builds the Tempest Prognosticator. He is inspired by Edward Jenner's poem *Signs of Rain*: "The leech disturbed is newly risen / Quite to the summit of his prison."
- **Design:** Twelve glass bottles, each containing a single medicinal leech in rainwater, are arranged in a circle around an ornate stand of polished French mahogany, brass, silver, and glass. The circular arrangement is both aesthetic and, Merryweather claims, humane: "in order that the leeches might see one another and not endure the affliction of solitary confinement." Each bottle neck contains a piece of whalebone linked by wire to a mechanism: when a leech climbs to the top, it dislodges the whalebone, triggering a small hammer that strikes a central bell. The more leeches that climb simultaneously, the more bells ring — a *majority-vote* forecasting system. Merryweather refers to the leeches as his "jury of philosophical councillors."
- **1850** — Merryweather spends the year testing the device, sending advance storm warnings by letter to Henry Belcher, president of the Whitby Philosophical Society. He claims 28 successful predictions, including the severe storm of October 1850, communicated 51.5 hours in advance.
- **1851** — The Tempest Prognosticator is displayed at the Great Exhibition in the Crystal Palace, London. Its ornate Indian-temple-like design was reportedly inspired by the Crystal Palace itself.
- **Proposed extension (never implemented):** Merryweather petitions the Admiralty to install devices along the British coast as a storm-warning network. He proposes wiring the bell mechanism to an electrical telegraph — "I could cause a little leech, governed by its instinct, to ring Saint Paul's great bell in London as a signal for an approaching storm." This would have constituted an early networked sensor array. However, the proposal was rejected as impractical (the leeches needed monthly feeding and water changes every five days), and no variation on this was ever implemented. The distinction matters: the exhibited device was a *mechanical* bell-ringing instrument; the telegraph link was a proposal, not an operational feature.
- **Fate:** The original device was lost after the Great Exhibition. Several replicas have been constructed; a notable working reconstruction by Phillip Collins was formerly housed at Barometer World in Devon; a replica exists at Whitby Museum.

**Operating principle (modern interpretation):** Leeches breathe through their body walls by absorbing dissolved oxygen. When atmospheric pressure drops, slightly less oxygen dissolves in the water. Leeches respond by moving toward the surface, where the water is more oxygen-rich. The device is thus, in effect, a biological barometer — but one whose transfer function is stochastic, subject to individual leech temperament (Merryweather noted that some were "prophetic" and others "absolutely stupid"), and modulated by feeding state, health, and habituation.

**Epistemological role:** The most elaborate of the sentinels: it converts atmospheric pressure change into animal behaviour, then into a mechanical signal (bell). The majority-vote architecture is a remarkable anticipation of ensemble methods. But the signal-to-noise ratio is poor, the system is high-maintenance, and it cannot be calibrated.

**Operational vs. experimental status:** The Tempest Prognosticator was an exhibition piece and experimental device, never integrated into a routine observation network. The coastal network Merryweather envisaged remained entirely unrealised.

**Primary source:**

- Merryweather, G. (1851). *An essay, explanatory, of the tempest prognosticator, in the building of the great exhibition for the works of industry of all nations*. Read before the Whitby Philosophical Society, 27 February 1851.

**Modern accounts:**

- Frost, N. (2017). "The Rise and Fall of the Leeches Who Could Predict the Weather," *Atlas Obscura*.
- Whitby Museum: description and images of the replica Tempest Prognosticator.

---

### VI.4 — The Frog Barometer (*Laubfrosch-Barometer*)

**Type:** Biological sentinel using amphibian behaviour as a weather indicator.

**Context:** Folk meteorology, mainly in German-speaking and French regions, 18th–19th century.

**History:**

- A European tree frog (*Hyla arborea*, German: *Laubfrosch*, literally "leaf frog") is placed in a glass jar with some water at the bottom and a small wooden ladder. The folk belief holds that if the frog climbs the ladder, the weather will improve; if it descends, rain is coming.
- The practice was widespread enough to generate cultural references in German (the *Laubfrosch* as weather prophet is a common idiom) and appears in English-language advertisements as late as the 1880s (e.g., *The Coffee Public-House News and Temperance Hotel Journal*, December 1886, marketing frog barometers as novelties).
- The underlying observation has a kernel of truth: European tree frogs are more active and vocal before rain (possibly responding to pressure drops, humidity changes, or insect availability). Pacific chorus frogs (*Pseudacris regilla*) in British Columbia are observed to call reliably hours before rain. But the ladder-climbing behaviour in a jar is far too noisy and context-dependent to be useful as a predictive instrument.

**Epistemological role:** The frog barometer is the most loosely coupled of the sentinels — the "instrument" is an entire organism whose behaviour integrates countless environmental and internal variables. It represents the folk-meteorological tradition at its most intuitive and its least tractable. Sources emphasise cultural diffusion rather than scientific validation.

**Persistence:** Displaced in any serious context by the 19th century. Survives as a cultural reference and occasional novelty item.

---

### Sentinel Comparison Table

| Device | Era | Physical basis | Signal type | Transfer function | Calibratable? | Invertible? | Persistence |
|---|---|---|---|---|---|---|---|
| Goethe barometer | 16th–17th c. | Pressure (+ temperature confound) | Water level | Approximately monotonic but contaminated | Crude | No (ambiguous) | Decorative |
| FitzRoy storm glass | 1830s–1860s | Solubility / nucleation (T-driven) | Crystal morphology | Nonlinear, hysteretic | No | No | Decorative / didactic |
| Tempest Prognosticator | 1850–1851 | Dissolved O₂ / leech physiology | Bell strikes (majority vote) | Stochastic, biological | No | No | Museum replicas |
| Frog barometer | 18th–19th c. | Multi-variate (pressure, humidity, insects?) | Frog position on ladder | Stochastic, biological | No | No | Cultural relic |

**Common signature:** All four sentinels are united by high-dimensional integration (response to bundled environmental variables), non-invertibility (output cannot uniquely reconstruct input), and sensitivity to regime transitions. They were displaced not because they were insensitive — most are, if anything, too sensitive — but because they could not support the inversion step required by the quantitative programme of meteorology.

---

## Part VII — Synthesis: Taxonomy of a Proto-Meteorological System

By the late 19th century, the following measurement layers existed — an implicit hardware model of the atmosphere:

| Layer | Instruments | Character | What it measures |
|---|---|---|---|
| **State** | Thermometer, barometer, hygrometer | Linear, calibrated, invertible | Local thermodynamic state (T, p, RH) |
| **Transport** | Anemometer, wind vane, nephoscope | Kinematic, directional | Movement of air and clouds |
| **Integration** | Rain gauge, atmometer | Accumulative, time-integrated | Outcomes of atmospheric processes |
| **Radiation** | Campbell–Stokes recorder, pyrheliometer | Energy flux | Solar forcing and its modulation |
| **Electrical** | Electroscope, electrometer, field mill | Non-thermodynamic, field-based | Atmospheric charge and discharge |
| **Sentinel** | Storm glass, Goethe barometer, leech barometer, frog barometer | Nonlinear, qualitative, non-invertible | Regime transitions and instabilities |

**Interpretation:** The state + transport + integration layers constitute a *reduced weather model in hardware*: (T, p, RH) determine the local state; wind and clouds transport; precipitation integrates. The radiation layer (arriving late, ~1850s–1880s) closes the energy budget. The electrical layer opens a non-thermodynamic window. And the sentinel layer — the most epistemologically distinctive — detects *transitions* that the calibrated instruments, precisely because they are designed for smooth, monotonic response, may underemphasise.

This "proto-meteorological system in hardware" is a descriptive observation, not a claim that 19th-century actors consciously designed or perceived it as a system. The coherence is retrospective and structural.

---

## Part VIII — Persistence and Displacement

### Long-term stable (operational to the present day)

- Mercury / aneroid / electronic barometer
- Liquid-in-glass / electronic thermometer
- Hair / capacitive / dew-point hygrometer
- Cup / ultrasonic anemometer
- Tipping-bucket / weighing rain gauge
- Campbell–Stokes recorder (at heritage sites)
- Pyrheliometer / pyranometer

### Transitional / superseded by remote sensing

- Nephoscope → satellite cloud tracking, Doppler radar
- Atmometer → Penman–Monteith calculation from state variables
- Pilot balloon → GPS radiosonde, wind profiler

### Displaced (no operational role)

- FitzRoy storm glass — lack of calibrability, non-invertible signal
- Goethe barometer — temperature contamination, no absolute scale
- Tempest Prognosticator — impractical (biological maintenance), stochastic
- Frog barometer — uncontrolled, anecdotal

### The displacement mechanism

In every case, the sentinel was displaced not because it was *insensitive* — most sentinels are, if anything, too sensitive — but because it was **not invertible**. The scientific programme of meteorology required instruments whose output could be mapped back to a unique atmospheric state. Sentinels amplify, but they mix; they detect, but they do not diagnose.

This displacement thesis is itself a falsifiable claim: it predicts that where invertibility is *not* required — in early warning systems, critical-transition detection, or qualitative hazard communication — sentinel-type approaches should persist or re-emerge. Modern early-warning-signal research (Part IX.3) suggests this prediction is borne out.

---

## Part IX — Critical Assessment

### 1. Quantification vs. Anschaulichkeit (intuitive clarity)

The triumph of calibrated instruments correlates with the ability to standardise, compare across stations, and feed observations into mathematical models. This was an enormous epistemic gain. But it came at the cost of *perceptual immediacy*: a barometer reading of 1003 hPa does not communicate the same visceral sense of "something is changing" as a storm glass sprouting crystals.

### 2. Underdetermination and the sentinel problem

The fundamental limitation of sentinels is *underdetermination*: the output is consistent with multiple input histories. A storm glass's crystal pattern depends on temperature, temperature rate, thermal history, nucleation sites, and possibly convective currents within the liquid. There is no unique inversion. This is not a failure of the device — it is a consequence of operating near a critical point, where small perturbations in any of several variables can trigger the same qualitative response.

### 3. Modern resonance

The sentinel concept is not obsolete — it has been *internalised* into modern complex-systems science under different names:

- **Early warning signals** (EWS) for critical transitions: increased variance, autocorrelation, and flickering near tipping points (Scheffer et al., 2009; Dakos et al., 2012).
- **Excitable systems**: devices intentionally placed near a bifurcation point to amplify weak signals (e.g., superconducting quantum interference devices, neuromorphic sensors).
- **Indicator species** in ecology: organisms whose behaviour or population dynamics signal ecosystem-scale regime shifts — a direct descendant of the frog barometer concept, now with quantitative monitoring frameworks.

The difference is that modern sentinels operate with *known parameters*, *controlled bifurcation distances*, and *statistical frameworks* for interpreting their output. The 19th-century sentinels had the right intuition — amplification near criticality — but lacked the mathematical language to make the output tractable.

---

## Part X — Annotated Source Guide

### A. Primary Sources (by instrument)

| Instrument | Source | Date |
|---|---|---|
| Barometer | Torricelli, letter to Ricci | 1644 |
| Barometer | Pascal, *Récit de la grande expérience* | 1648 |
| Thermometer (scale) | Fahrenheit, *Phil. Trans.* 33, 78–84 | 1724 |
| Hygrometer (hair) | Saussure, *Essais sur l'hygrométrie* | 1783 |
| Hygrometer (dew-point) | Daniell, *Quart. J. Sci.* 8, 280–290 | 1820 |
| Rain gauge (*ch'ŭgugi*) | *Veritable Records of the Joseon Dynasty*, entries from 1442 | 1442 |
| Rain gauge (tipping-bucket) | Wren, rain gauge design | 1662 |
| Wind (scale) | Beaufort, wind-speed scale proposal | 1806 |
| Sunshine | Campbell, original sunshine recorder | 1853 |
| Pyrheliometer | Pouillet, solar constant estimate | 1837–38 |
| Atmospheric electricity | Franklin, *Experiments and Observations on Electricity* | 1751 |
| Atmospheric electricity | Ronalds, Kew Observatory papers | 1810s–1860s |
| Storm glass | FitzRoy, *The Weather Book* | 1863 |
| Leech barometer | Merryweather, *Essay on the Tempest Prognosticator* | 1851 |

### B. Standard Instrument Histories

- **Middleton, W. E. K.** (1964). *The History of the Barometer*. Johns Hopkins University Press.
- **Middleton, W. E. K.** (1966). *A History of the Thermometer and Its Use in Meteorology*. Johns Hopkins University Press.
- **Middleton, W. E. K.** (1969). *Invention of the Meteorological Instruments*. Johns Hopkins University Press. — The standard survey; 10 chapters covering barometer, thermometer, hygrometer, rain gauge, atmometer, wind, sunshine, meteorographs, upper-air instruments, and telemeteorography.
- **Middleton, W. E. K. & Spilhaus, A. F.** (1953/1960). *Meteorological Instruments*. University of Toronto Press. 3rd ed. — Operational focus.
- **Multhauf, R. P.** (n.d.). *The Introduction of Self-Registering Meteorological Instruments*. Smithsonian Institution (Gutenberg text 32482). — Traces the transition from manual to self-recording instruments, 17th–19th century.

### C. Historiographic and Contextual Works

- **Chang, H.** (2004). *Inventing Temperature: Measurement and Scientific Progress*. Oxford University Press. — Philosophy of measurement; the thermometer as a case study in circularity and bootstrapping.
- **Feldman, T.** (1990). "Late Enlightenment Meteorology." In *The Quantifying Spirit in the 18th Century*, ed. T. Frangsmyr et al. University of California Press, 143–177.
- **Frisinger, H. H.** (1977). *The History of Meteorology to 1800*. Science History Publications, New York.
- **Golinski, J.** (2007). *British Weather and the Climate of Enlightenment*. University of Chicago Press.
- **Wolf, A.** (1935/1952). *A History of Science, Technology and Philosophy in the 16th/17th/18th Century*. 2 vols. New York: Peter Smith.

### D. Modern Reinterpretations and Scientific Analyses

- **Harrison, R. G.** (2004). "The global atmospheric electrical circuit and climate," *Surveys in Geophysics*, 25, 441–484.
- **Kaempf, N.** et al. (2025). "The Storm Glass Thermometer: Temperature Dependence of Camphor Crystal Formation in Ethanol," *J. Chem. Educ.*, 102, 2540–2542.
- **Scheffer, M.** et al. (2009). "Early-warning signals for critical transitions," *Nature*, 461, 53–59.
- **Dakos, V.** et al. (2012). "Methods for detecting early warnings of critical transitions in time series illustrated using simulated ecological data," *PLoS ONE*, 7, e41010.
- **Stanhill, G.** (2003). "Through a glass brightly: Some new light on the Campbell–Stokes sunshine recorder," *Weather*, 58, 3–11.
- **Sanchez-Romero, A.** et al. (2015). "Using digital image processing to characterise the Campbell–Stokes sunshine recorder," *Atmos. Meas. Tech.*, 8, 183–194.

---

## Appendix A — Timeline of Key Dates

| Year | Event |
|---|---|
| ~1450 | Alberti's wind vane with deflection plate |
| 1441–42 | Joseon *ch'ŭgugi* rain gauges distributed nationally |
| ~1593–1612 | Thermoscope (Galileo, Santorio, Telioux — contested priority) |
| 1643 | Torricelli's mercury barometer |
| 1648 | Pascal / Périer: pressure decreases with altitude (Puy-de-Dôme) |
| ~1664 | Hooke: wheel barometer, anemometer, hygrometer |
| 1662 | Wren: tipping-bucket rain gauge |
| ~1700s | Goethe barometer / Donderglas in wide use |
| 1714–1724 | Fahrenheit: standardised mercury thermometer |
| 1742 | Celsius: centigrade scale |
| Late 18th c. | Psychrometric methods emerge |
| 1751–1752 | Franklin / Dalibard: atmospheric electricity experiments |
| ~1780 | Saussure: hair hygrometer |
| 1806 | Beaufort: wind-speed scale |
| ~1810 | Ronalds: automated atmospheric electricity recording |
| 1820 | Daniell: dew-point hygrometer |
| ~1837–38 | Pouillet: pyrheliometer, first solar constant estimate |
| 1844 | Vidie: aneroid barometer |
| 1846 | Robinson: cup anemometer |
| 1850–1851 | Merryweather: Tempest Prognosticator (Great Exhibition) |
| 1853 | Campbell: sunshine recorder |
| ~1860s | FitzRoy promotes the storm glass |
| 1863 | FitzRoy: *The Weather Book* |
| 1860s | Kelvin: water-dropper electrometer at Kew |
| 1879 | Stokes: refined Campbell–Stokes recorder |
| 1886 | Fineman: nephoscope |
| 1893 | Ångström: electrical compensation pyrheliometer |
| 1895 | Popov: lightning detector (coherer receiver) |
| 1896 | International Cloud Year; first *International Cloud Atlas* |

---

## Open Items for v0.2.0

1. **Thermometer placement chronology** (I.2): The claim about continental vs. English practice requires verification against Middleton's *History of the Thermometer*. Currently marked with a caveat in the text.
2. **Psychrometer attribution** (I.3): Specific early attributions softened; further verification needed before restoring named attributions.
3. **Nephoscope sourcing** (II.2): Fineman 1886 now cited explicitly. Further museum-collection or atlas-history sources would strengthen this section.
4. **Frog barometer** (VI.4): Primary-source anchoring remains weak (cultural-press references only). A systematic survey of German/French folk-meteorology literature would improve this section.
5. **Breakwater Ledger entry** for the displacement thesis (Part VIII): The claim that sentinels were displaced by non-invertibility, not insensitivity, is falsifiable and could be formalised as a Ledger entry (CL-candidate). Deferred pending sharper discriminant conditions.
6. **Modern Sentinel Synthesis** essay: Connecting Part IX.3 to contemporary IoT, neuromorphic sensors, and complex-systems early-warning theory. Identified as a potential Sail document for the Harbour.
7. **Tier labelling**: Mapping the six-layer taxonomy to the Harbour's Temporal Frameworks Architecture (T0/T1b). Deferred to avoid overloading a primarily historical document.

---

*End of dossier v0.1.1*
