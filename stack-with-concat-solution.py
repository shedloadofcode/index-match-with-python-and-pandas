import os
import glob
import pandas as pd
from pandas.core.reshape.concat import concat


csv_files = glob.glob("logs/*.csv")
dataframes = []

for filename in csv_files:
  df = pd.read_csv(filename, index_col=None, header=0)
  dataframes.append(df)

concatenated_df = pd.concat(dataframes, axis=0, ignore_index=True)

print(concatenated_df.shape)

concatenated_df.to_csv(f"logs/concatenated.csv", index=False)
