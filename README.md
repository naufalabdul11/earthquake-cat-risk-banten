# Earthquake catastrophe risk and financial loss in Tangerang and Pandeglang, Banten

Introduction to Disaster Insurance course project, Actuarial Science ITS (November–December 2024), team project.

The project estimates residential losses from earthquakes on the Megathrust-7 (M7) subduction segment for Kota Tangerang and Kabupaten Pandeglang, following the hazard, inventory and vulnerability modules of a catastrophe model:

1. **Hazard:** earthquakes on the Megathrust-7 segment are selected from the catalogue in QGIS. After declustering, 303 mainshocks remain; their magnitude exceedances are fitted with a generalised Pareto distribution and checked with the Cramér–von Mises test. Event locations are smoothed with a Gaussian kernel density.
2. **Ground motion:** shaking at each building location is estimated with three attenuation functions (Atkinson–Boore 2003, Zhao 2006 and BCH 2012), adjusted for site conditions through Vs30.
3. **Vulnerability:** damage ratios come from vulnerability curves for each building taxonomy (reinforced concrete, confined masonry, unreinforced masonry, steel and wood).
4. **Loss:** damage ratios times building values give the expected residential loss for return periods such as 50 and 100 years.

## Structure
```
notebooks/M7_kota_tangerang.ipynb    full model for Kota Tangerang, with outputs
notebooks/M7_kab_pandeglang.ipynb    full model for Kabupaten Pandeglang, with outputs
data/hazard/Data_gempa.csv           earthquake catalogue
data/hazard/DATA M7.csv              events selected on the Megathrust-7 segment in QGIS
data/gmpe/                           attenuation coefficients
data/vulnerability/                  vulnerability curves by building taxonomy
data/inventory/                      rebuilt residential inventory for Banten and the script that builds it
```

## About the inventory
The saved notebook outputs come from the original inventory prepared by a teammate. That file is not available, so `data/inventory/` holds a rebuilt version: the same building rows and structural periods, but Vs30 is a placeholder of 300 m/s for every regency. Rerunning the notebooks therefore gives somewhat different losses; the Monte Carlo magnitudes are also unseeded, so no two runs match exactly. See `data/inventory/README.md` to put in real Vs30 values.

## Run it
```bash
pip install -r requirements.txt     # rpy2 needs R with the POT package: install.packages("POT")
jupyter notebook notebooks/M7_kota_tangerang.ipynb
```
The province boundary shapefile used for the maps (GADM `IDN_adm1`, 26 MB) is not included; download it from gadm.org if you want to redraw them.

Credit: built with my Introduction to Disaster Insurance project team at ITS. Portfolio: https://naufalabdul11.github.io
