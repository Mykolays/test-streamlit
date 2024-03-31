import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df: pd.DataFrame = pd.read_excel("Data/Solar_index_data.xlsx", sheet_name=[4,3,2,1,0], header=0, usecols="A,D,E,F,G")

cycle_21: pd.DataFrame = df[4]
cycle_22: pd.DataFrame = df[3]
cycle_23: pd.DataFrame = df[2]
cycle_24: pd.DataFrame = df[1]
cycle_25: pd.DataFrame = df[0]
all_cycles = pd.concat(df.values(), ignore_index=True)
all_cycles = all_cycles.dropna()

all_cycles_daily: pd.DataFrame = all_cycles
all_cycles_monthly: pd.DataFrame = all_cycles.resample("ME", on='Data').mean()
