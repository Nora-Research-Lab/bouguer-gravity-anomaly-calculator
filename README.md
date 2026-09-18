![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Bouguer Gravity Anomaly Calculator
 
*For geophysicists and exploration geologists: enter latitude, elevation, observed gravity, and density to get theoretical gravity and free-air/Bouguer anomalies.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Geophysics
 
This tool calculates gravity corrections and anomalies for a single ground gravity station. The user provides five inputs: latitude in decimal degrees, station elevation above sea level in metres, observed gravity in mGal, reduction density in g/cm³ (default 2.67), and an optional terrain correction in mGal (default 0.0). The core logic is deterministic and follows standard gravity reduction steps. First, convert latitude to radians and compute theoretical sea-level gravity using the International Gravity Formula 1967: g_theory = 978031.846 * (1 + 0.005278895*sin²φ + 0.000023462*sin⁴φ), reported in mGal. Second, compute the free-air correction as 0.3086 * h mGal. Third, compute the free-air anomaly: FAA = observed_gravity - g_theory + free-air_correction. Fourth, compute the simple Bouguer correction as 0.04193 * density * h mGal. Fifth, compute the simple Bouguer anomaly: SBA = FAA - Bouguer_correction. Finally, if a terrain correction is supplied, compute the complete Bouguer anomaly: CBA = SBA + terrain_correction. The Gradio interface should be a single-column layout with five labelled Number inputs, a Calculate button, and a results DataFrame output showing each parameter and its value rounded to three decimal places: theoretical gravity, free-air correction, Bouguer correction, free-air anomaly, simple Bouguer anomaly, and complete Bouguer anomaly. All output values are in mGal. No AI/ML component is used; the tool is a clean geophysical calculation.
 
## Run it
 
```bash
docker build -t bouguer-gravity-anomaly-calculator .
docker run -p 7860:7860 bouguer-gravity-anomaly-calculator
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
 
Built 2026-09-18.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
