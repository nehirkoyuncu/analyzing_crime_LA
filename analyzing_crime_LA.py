import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

crimes = pd.read_csv("crimes.csv", dtype={"TIME OCC": str})
crimes.head()


peak_crime_hour = crimes["TIME OCC"].str[:2].astype(int).value_counts().idxmax()


crimes_time = crimes["TIME OCC"].str[:2].astype(int)

night_crimes = crimes[(crimes_time >= 22) | (crimes_time < 4)]

peak_night_crime_location = night_crimes["AREA NAME"].value_counts().idxmax()


age_labels = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]

victim_ages = crimes.groupby(pd.cut(crimes["Vict Age"], bins=age_bins, labels=age_labels, right=True)).size()

print(f"Peak crime hour: {peak_crime_hour}")
print(f"Peak night crime location: {peak_night_crime_location}")
print("\nCrimes by victim age:")
print(victim_ages)