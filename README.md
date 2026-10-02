![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Packer Test Permeability Calculator
 
*For geological engineers and hydrogeologists: enter test section length, borehole diameter, injection pressure, and flow rate to instantly compute Lugeon value, hydraulic conductivity, and permeability classification.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Geological Engineering
 
**Inputs (all user-provided):**
1. Test section length (L, meters) — float.
2. Borehole diameter (D, mm) — float.
3. Injection pressure (P, bars) — float.
4. Flow rate (Q, liters per minute) — float.
5. Test type: dropdown with options 'Constant head' or 'Falling head'.
6. (For falling head only) Standpipe inner diameter (d, mm) and initial/final water level change (Δh, m).

**Core calculation / logic:**
- Compute Lugeon value (Lu) = Q (L/min) / (L (m) × P (bar)). Standard: 1 Lu = 1 L/min/m/bar.
- Hydraulic conductivity K (m/s): For constant head: K = (Q / (2π L Δh)) × ln(r_e/r_w) where r_e = effective radius (typically 0.5 m if no other info), r_w = D/2000 (m). Δh = pressure head = P × 10.2 (m of water). For falling head: K = (a × L) / (A × t) × ln(h1/h2) where a = standpipe cross-sectional area (m²), A = borehole cross-sectional area (m²), t = elapsed time (s), h1 and h2 initial and final heads (m).
- Permeability classification: if K < 1e-7 m/s → 'Very low'; 1e-7 to 1e-5 → 'Low'; 1e-5 to 1e-3 → 'Moderate'; 1e-3 to 1e-1 → 'High'; > 1e-1 → 'Very high'. Also Lugeon interpretive classification: <1 → 'Tight'; 1-5 → 'Low'; 5-25 → 'Moderate'; >25 → 'High'.

**Gradio UI layout:**
- Top: title and brief instructions.
- Input section with labeled numeric fields and dropdown.
- A 'Calculate' button.
- Output area below: three values (Lugeon, K, permeability class) displayed as cards with units. A small table showing both Lugeon and permeability classifications. Optionally a simple horizontal color bar indicating class.
- No charts needed, but if falling head, show a simple plot of head vs time if multiple readings can be entered (optional: allow adding time-head data points as a textbox, then plot decay curve). To keep simple, just the basic case.

**Output:**
- Lugeon value (Lu) with one decimal.
- Hydraulic conductivity (m/s) in scientific notation.
- Permeability classification (text).
- Lugeon classification (text).
- No downloadable file unless user adds multiple measurements (optional).

**AI/ML component:** None. Pure calculation with classification thresholds.
 
## Run it
 
```bash
docker build -t packer-test-permeability-calculator .
docker run -p 7860:7860 packer-test-permeability-calculator
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-10-02.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
