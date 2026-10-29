"""Sample the USGS Global Vs30 Mosaic at each city and regency office in Indonesia.

Input: vs30_indonesia.tif, the USGS Global Vs30 Mosaic (Heath et al., 2020) clipped in QGIS to
94.5-141.5 E and 11.5 S-6.5 N, with 30 arc-second cells and Vs30 in m/s. Water is filled with 600 m/s.
Office coordinates are the "Kantor DT2" points of the national residential inventory used in the
course, one per city or regency.
Output: vs30_indonesia_kabkota.csv with Vs30 and the site class used by the Atkinson-Boore (2003)
site terms in the notebooks. An office whose cell is water takes the median of the land cells
within one to three cells; Kepulauan Seribu keeps the 600 m/s water value.

Requires: pip install rasterio pandas numpy
"""
import numpy as np
import pandas as pd
import rasterio


def site_class(v):
    if v > 760:
        return "B, rock (>760)"
    if v > 360:
        return "C, very dense soil (360-760)"
    if v >= 180:
        return "D, stiff soil (180-360)"
    return "E, soft soil (<180)"


offices = pd.read_csv("vs30_indonesia_kabkota.csv")[["province", "regency", "code", "lat", "lon"]]
with rasterio.open("vs30_indonesia.tif") as r:
    grid = r.read(1)
    rows, cols = rasterio.transform.rowcol(r.transform, offices["lon"].values, offices["lat"].values)

values, notes = [], []
for i, j in zip(rows, cols):
    v, note = int(grid[i, j]), ""
    if v in (600, 0):
        for h in (1, 2, 3):
            w = grid[max(0, i - h):i + h + 1, max(0, j - h):j + h + 1]
            w = w[(w != 600) & (w != 0)]
            if w.size:
                v, note = int(np.median(w)), f"office cell is water in the USGS map; median of land cells within {h} cell(s)"
                break
        else:
            note = "office cell and its 3-cell surroundings are water in the USGS map; 600 m/s water default kept"
    values.append(v)
    notes.append(note)

offices["vs30"] = values
offices["site_class"] = offices["vs30"].map(site_class)
offices["note"] = notes
offices.to_csv("vs30_indonesia_kabkota.csv", index=False)
print(offices["site_class"].value_counts())
