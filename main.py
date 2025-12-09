import numpy as np
import pandas as pd

df = pd.read_csv("data/diapers.csv")

df = df[[
    'Timestamp', 'BRANCH', 'ZIP CODE', 'SIZE', '# PACKS', 'SIZE.1',
    '# PACKS.1', 'SIZE.2', '# PACKS.2', 'TOTAL'
]]

df = df[df['BRANCH'] == "WR"]

size_cols = ["SIZE", "SIZE.1", "SIZE.2"]
pack_cols = ["# PACKS", "# PACKS.1", "# PACKS.2"]

pieces = []

for i in range(3):  # force 3 iterations
  temp = df[["Timestamp", "BRANCH", "ZIP CODE", "TOTAL"]].copy()
  temp["SIZE"] = df[size_cols[i]]
  temp["# PACKS"] = df[pack_cols[i]]
  pieces.append(temp)

df_long = pd.concat(pieces, ignore_index=True)

print(len(df), "original rows")
print(len(df_long), "long rows")

print(df_long.head(10))
