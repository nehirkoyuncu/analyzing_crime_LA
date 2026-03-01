📂 Analyzing Crime in Los Angeles
This project performs a comprehensive data analysis on the crimes.csv dataset to identify patterns in criminal activities across Los Angeles.

🔍 Key Research Questions
Peak Crime Hour: Identifying the specific hour of the day when crime frequency is at its highest (Stored in peak_crime_hour).

Night Crime Hotspots: Determining which city area experiences the most criminal activity during nighttime (10:00 PM – 3:59 AM) (Stored in peak_night_crime_location).

Victim Demographics: Categorizing crime data by victim age groups to understand which age brackets are most affected.

🛠️ Tech Stack
Language: Python

Libraries: Pandas, NumPy, Matplotlib, Seaborn

📊 Methodology
Time Analysis: Extracted the hour from the TIME OCC column to find daily peaks.

Geospatial Filtering: Filtered crimes occurring between 22:00 and 04:00 to isolate nighttime incidents by AREA NAME.

Age Binning: Used pd.cut to segment Vict Age into defined ranges (0-17, 18-25, etc.) to analyze demographic trends.

💡 Key Insights
Peak Hour: The analysis revealed that criminal activity reaches its daily high at 12:00 PM (noon).

Night Safety: Central area was identified as the hotspot for nighttime incidents between 10 PM and 4 AM.

Vulnerable Groups: Citizens in the 26-34 age bracket were found to be the most affected demographic in the dataset.
Age Binning: Used pd.cut to segment Vict Age into defined ranges: 0-17, 18-25, 26-34, 35-44, 45-54, 55-64, and 65+.
