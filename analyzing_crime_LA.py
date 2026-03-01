import pandas as pd

# -----------------------------
# Load dataset
# -----------------------------
crimes = pd.read_csv("crimes.csv")

# -----------------------------
# 1️⃣ Peak Crime Hour
# -----------------------------
crimes["HOUR"] = crimes["TIME OCC"].astype(str).str.zfill(4).str[:2].astype(int)

peak_crime_hour = crimes["HOUR"].mode()[0]

# -----------------------------
# 2️⃣ Nighttime Crime Hotspot
#    (10:00 PM – 3:59 AM)
# -----------------------------
night_crimes = crimes[(crimes["HOUR"] >= 22) | (crimes["HOUR"] < 4)]

peak_night_crime_location = (
    night_crimes["AREA NAME"]
    .value_counts()
    .idxmax()
)

# -----------------------------
# 3️⃣ Most Vulnerable Age Group
# -----------------------------
age_bins = [0, 17, 25, 34, 44, 54, 64, 150]
age_labels = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]

victim_age_groups = (
    crimes.groupby(
        pd.cut(crimes["Vict Age"], bins=age_bins, labels=age_labels)
    )["Vict Age"]
    .count()
)

most_vulnerable_group = victim_age_groups.idxmax()

# -----------------------------
# Results
# -----------------------------
print("Peak crime hour:", peak_crime_hour)
print("Nighttime hotspot area:", peak_night_crime_location)
print("Most vulnerable age group:", most_vulnerable_group)
