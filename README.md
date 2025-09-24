This project analyzes the crimes.csv dataset to answer three main questions:

Hour with the Highest Crime Frequency:

-Crimes were grouped by the hour of occurrence.

-The hour with the highest number of crimes was identified and stored in an integer variable called peak_crime_hour.

Area with the Most Night Crimes:

-Nighttime was defined as the period between 10:00 PM and 3:59 AM.

-Crimes committed during this time range were filtered and grouped by area.

-The area with the largest frequency of night crimes was identified and stored in a string variable called peak_night_crime_location.

Crimes by Victim Age Groups:

-Victim ages were categorized into the following groups:

0–17

18–25

26–34

35–44

45–54

55–64

65+

-The number of crimes in each age group was calculated.

-Results were stored as a pandas Series named victim_ages, with age group labels as the index and crime counts as the values.
