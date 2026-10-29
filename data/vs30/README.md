# Vs30 for Indonesia

Vs30 is the average shear-wave velocity in the top 30 m of ground, in m/s. Softer ground (lower Vs30) amplifies earthquake shaking, so the notebooks use it in the site terms of the three ground-motion models.

## Files

- `vs30_indonesia.tif`: the USGS Global Vs30 Mosaic (Heath et al., 2020), clipped in QGIS to 94.5–141.5 E and 11.5 S–6.5 N. Cells are 30 arc-seconds (about 900 m), values are in m/s (180 to 900 over Indonesia, from the topographic-slope model), and water is filled with 600 m/s. Coordinates are WGS84 (EPSG:4326).
- `vs30_indonesia_kabkota.csv`: Vs30 at the office of each of the 514 cities and regencies in the national residential inventory used in the course, with the site class the notebooks use: 337 are class D (stiff soil, 180–360 m/s), 172 class C (very dense soil, 360–760 m/s) and 5 class B (rock, above 760 m/s).
- `sample_vs30.py`: reproduces the table from the raster.

## Coastal offices

Sixteen offices fall on a cell the USGS map treats as water. They take the median of the land cells within one to three cells, and the `note` column says so. Kepulauan Seribu's islands are too small for the 900 m cells, so it keeps the 600 m/s water value.

## Source

Heath, D. C., Wald, D. J., Worden, C. B., Thompson, E. M., and Smoczyk, G. M. (2020). A global hybrid VS30 map with a topographic slope–based default and regional map insets. *Earthquake Spectra*, 36(3), 1570–1584. Data from https://earthquake.usgs.gov/data/vs30/.
