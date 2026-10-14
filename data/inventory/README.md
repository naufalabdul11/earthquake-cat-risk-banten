# Residential inventory for Banten

`PROV BANTEN-fix.xlsx` is what the notebooks read: one sheet per regency or city, with the building rows, the total structural value, the structural period and `vs30`.

The original file was prepared by a teammate in QGIS and is not available, so `build_inventory.py` rebuilds it:

- **Building rows** for the eight regencies and cities come from the national residential inventory used in the course (`banten_residential.csv`). They match the original: the taxonomies the notebooks reported as having no vulnerability curve are identical for Kota Tangerang and Kabupaten Pandeglang.
- **Structural period** per taxonomy follows the course template.
- **Vs30** is a **placeholder**: 300 m/s (NEHRP site class D, stiff soil) for every regency, in `vs30_by_regency.csv`. Softer soil amplifies shaking, so the placeholder leans conservative.

To use real values, sample a Vs30 map (for example the USGS global Vs30 map) at each regency's coordinates in QGIS, enter them in `vs30_by_regency.csv`, and run `python build_inventory.py`.
