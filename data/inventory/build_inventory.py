"""Rebuild the Banten residential inventory used by the notebooks (PROV BANTEN-fix.xlsx).

The original file was prepared by a teammate in QGIS and is not available. This script recreates it:
- building rows for the eight regencies and cities of Banten come from the national residential
  inventory used in the course (banten_residential.csv);
- the structural period per taxonomy follows the course template (Papua Barat inventory);
- vs30 comes from vs30_by_regency.csv: the USGS Global Vs30 Mosaic (Heath et al., 2020) sampled at
  each regency office (see ../vs30/).
"""
import pandas as pd

ORDER = ['KAB. PANDEGLANG', 'KAB. LEBAK', 'KAB. TANGERANG', 'KAB. SERANG', 'KOTA TANGERANG', 'KOTA CILEGON', 'KOTA SERANG', 'KOTA TANGERANG SELATAN']
PERIOD = {'CR/LFINF+DUL/H:3': 0.3, 'CR/LFINF+DUL/H:4': 0.6, 'CR/LFINF+DUM/H:3': 0.3, 'CR/LFINF+DUM/H:4': 0.6, 'MCF/LWAL+DUL/H:1': 'PGA', 'MCF/LWAL+DUL/H:2': 0.3, 'MCF/LWAL+DUL/H:3': 0.3, 'MCF/LWAL+DUM/H:1': 'PGA', 'MCF/LWAL+DUM/H:2': 0.3, 'MCF/LWAL+DUM/H:3': 0.3, 'MUR/LWAL+DNO/H:1': 0.3, 'MUR/LWAL+DNO/H:2': 0.3, 'UNK/H:1': 0.3, 'W+WBB/LPB+DNO/H:1': 0.3, 'W+WLI/LWAL+DUL/H:1': 0.3, 'W+WO/LN/H:1': 0.3, 'W+WO/LN/H:1+HFAPP:1': 0.3, 'ME+MEO/LN/H:1': 0.3}

rows = pd.read_csv("banten_residential.csv")
vs30 = pd.read_csv("vs30_by_regency.csv").set_index("regency")["vs30_mps"]
with pd.ExcelWriter("PROV BANTEN-fix.xlsx") as xl:
    for regency in ORDER:
        sheet = rows[rows["id_1"] == regency].copy()
        sheet["vs30"] = float(vs30[regency])
        sheet["period"] = sheet["taxonomy"].map(PERIOD)
        missing = sheet.loc[sheet["period"].isna(), "taxonomy"].unique()
        if len(missing):
            raise ValueError(f"No structural period for {missing} in {regency}")
        sheet.to_excel(xl, sheet_name=regency, index=False)
print("Wrote PROV BANTEN-fix.xlsx with", len(ORDER), "sheets")
