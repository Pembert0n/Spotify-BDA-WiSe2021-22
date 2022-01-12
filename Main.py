# @since: 2021-12-03
'''
Link zur Hausarbeit:
https://studhsheilbronnde-my.sharepoint.com/:w:/g/personal/spembe_stud_hs-heilbronn_de/EdtQ7nqM4p5MqvPq2Zoj30oBSpqMtPRbKED2AKkgTx8agA?e=9N16hW
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.options.mode.chained_assignment = None


#Einlesen der CSV


df1 = pd.read_csv("Database_to_calculate_popularity.csv")
df1["count"] = 1

df2 = pd.read_csv("Final_database.csv")
'''
Zeitunterteilung
'''
#2017
df2017 = df1
df2017['date'] = pd.to_datetime(df2017['date'])
start_date = '01/01/2017'
end_date = '01/01/2018'
mask = (df2017['date'] > start_date) & (df2017['date'] <= end_date) & (df2017['country'] == "Global")

#2018
df2018 = df1
df2018['date'] = pd.to_datetime(df2018['date'])
start_date = '01/01/2018'
end_date = '01/01/2019'
mask = (df2018['date'] > start_date) & (df2018['date'] <= end_date) & (df2018['country'] == "Global")

#2019
df2019 = df1
df2019['date'] = pd.to_datetime(df2019['date'])
start_date = '01/01/2019'
end_date = '01/01/2020'
mask = (df2019['date'] > start_date) & (df2019['date'] <= end_date) & (df2019['country'] == "Global")

#2020
df2020 = df1
df2020['date'] = pd.to_datetime(df2020['date'])
start_date = '01/01/2020'
end_date = '01/01/2021'
mask = (df2020['date'] > start_date) & (df2020['date'] <= end_date) & (df2020['country'] == "Global")


'''
Code für Abscnhitt 1 der Seminararbeit.


'''

df_k1 = df2020.loc[mask]

df_k1_countCountry = df_k1.groupby(["artist"]).count()["count"]
print(df_k1_countCountry.sort_values())


# Pre-Processing
print("NaNs?", df_k1.isnull().sum())

# Drop all NaNs
df_k1 = df_k1.dropna(axis=0)

df_k1h = df_k1.head(20)

# Visualization
Lsize = df_k1h.groupby(["artist"]).count()["count"]
LLables = df_k1h.groupby(["artist"]).count()["count"].index

# Figure
plt.figure(figsize=(7, 7))
plt.pie(Lsize, labels=LLables, autopct="%1.1f%%")
plt.title("")
plt.savefig("PieSpot.pdf")





list = df_k1h["artist"].tolist()
print(list)

filter = df_k1["artist"].isin(list)
df_k1f = df_k1.loc[filter]
#print(df_k1f["artist"].head(50))
df_k1f.drop_duplicates(subset="track", inplace=True, ignore_index=True)
#finde out tracks
print(df_k1f["track"].head(50))

#df1 & df2
df1_urilist = df_k1f["uri"].tolist()


duration_filter = df2["Uri"].isin(df1_urilist)
df2f = df2.loc[duration_filter]


df2f.drop_duplicates(subset="Uri", inplace=True, ignore_index=True)

df2o = df2f["duration_ms"]


print(df2o.mean())



# Just the End
print("Done")
