# Residential inventory for Banten

`PROV BANTEN-fix.xlsx` is what the notebooks read: one sheet per regency or city, with the building rows, the total structural value, the structural period and `vs30`.

This is the team's original file, prepared in QGIS; `original/` holds the same file for all eleven provinces of the course. `build_inventory.py` rebuilds it from public inputs, and the rebuilt file matches the original row for row:

- **Building rows** for the eight regencies and cities come from the national residential inventory used in the course (`banten_residential.csv`). They match the original: the taxonomies the notebooks reported as having no vulnerability curve are identical for Kota Tangerang and Kabupaten Pandeglang.
- **Structural period** per taxonomy follows the course template.
- **Vs30** comes from the USGS Global Vs30 Mosaic (Heath et al., 2020), sampled at each regency office and stored in `vs30_by_regency.csv`: 469 m/s for Kabupaten Pandeglang (site class C, very dense soil) and 203 to 258 m/s for the other seven (site class D, stiff soil), including 218 m/s for Kota Tangerang. The raster and the values for all 514 cities and regencies in Indonesia are in `../vs30/`.

To change a value, edit `vs30_by_regency.csv` and run `python build_inventory.py`.
