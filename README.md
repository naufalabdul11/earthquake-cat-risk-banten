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
data/inventory/                      the team's residential inventory for Banten (original/ holds all eleven provinces)
data/hazard/segments/                outlines of the 16 megathrust segments (M01 to M16)
data/vs30/                           USGS Vs30 raster for Indonesia and Vs30 for all 514 cities and regencies
```

## About the inventory
`data/inventory/PROV BANTEN-fix.xlsx` is the team's original inventory, prepared in QGIS, and `data/inventory/original/` holds the same file for all eleven provinces the course covered. Its Vs30 values match the USGS Global Vs30 Mosaic sampled at each regency office (`data/vs30/`) to the nearest m/s. The Monte Carlo magnitudes are unseeded, so no two runs of the notebooks match exactly.

## National extension
The interactive version on my portfolio (naufalabdul11.github.io, Models → Earthquake catastrophe model) extends the method to all 514 cities and regencies and the 16 megathrust segments. `data/hazard/catalog_indonesia_M4.5_1973-2023.csv` is the USGS catalog for 90–142 E and 12 S–13 N from magnitude 4.5; the outline in `data/hazard/segments/Longlat_M07.csv` selects exactly the 480 events of magnitude 4.5 and above in `DATA M7.csv`. Each city or regency uses its nearest segment by default, with buildings from the course's national residential inventory and Vs30 from `data/vs30/`.

## Run it
```bash
pip install -r requirements.txt     # rpy2 needs R with the POT package: install.packages("POT")
jupyter notebook notebooks/M7_kota_tangerang.ipynb
```
The province boundary shapefile used for the maps (GADM `IDN_adm1`, 26 MB) is not included; download it from gadm.org if you want to redraw them.

Credit: built with my Introduction to Disaster Insurance project team at ITS. Portfolio: https://naufalabdul11.github.io
