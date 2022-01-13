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
mask17 = (df2017['date'] > start_date) & (df2017['date'] <= end_date) & (df2017['country'] == "Global")

#2018
df2018 = df1
df2018['date'] = pd.to_datetime(df2018['date'])
start_date = '01/01/2018'
end_date = '01/01/2019'
mask18 = (df2018['date'] > start_date) & (df2018['date'] <= end_date) & (df2018['country'] == "Global")

#2019
df2019 = df1
df2019['date'] = pd.to_datetime(df2019['date'])
start_date = '01/01/2019'
end_date = '01/01/2020'
mask19 = (df2019['date'] > start_date) & (df2019['date'] <= end_date) & (df2019['country'] == "Global")

#2020
df2020 = df1
df2020['date'] = pd.to_datetime(df2020['date'])
start_date = '01/01/2020'
end_date = '01/01/2021'
mask = (df2020['date'] > start_date) & (df2020['date'] <= end_date) & (df2020['country'] == "Global")


'''
Code für Abscnhitt 1 der Seminararbeit.
Hier werden die Charts für ... erstellt

'''


#Top 20 Künstler in den Charts

df_k1 = df2020.loc[mask]
df_k1_countCountry = df_k1.groupby(["artist"]).count()["count"]

df_k2 = df2019.loc[mask]
df_k2_countCountry = df_k2.groupby(["artist"]).count()["count"]

df_k3 = df2018.loc[mask]
df_k3_countCountry = df_k3.groupby(["artist"]).count()["count"]

df_k4 = df2018.loc[mask]
df_k4_countCountry = df_k4.groupby(["artist"]).count()["count"]
#print(df_k1_countCountry.sort_values())


# Pre-Processing
#print("NaNs?", df_k1.isnull().sum())

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
plt.savefig("PieSpot2020.pdf")


#2019
df_k2 = df2019.loc[mask19]

df_k2_countCountry = df_k2.groupby(["artist"]).count()["count"]
#print(df_k1_countCountry.sort_values())


# Pre-Processing
#print("NaNs?", df_k1.isnull().sum())

# Drop all NaNs
df_k2 = df_k2.dropna(axis=0)

df_k2h = df_k2.head(20)

# Visualization
Lsize19 = df_k2h.groupby(["artist"]).count()["count"]
LLables19 = df_k2h.groupby(["artist"]).count()["count"].index

# Figure
plt.figure(figsize=(7, 7))
plt.pie(Lsize19, labels=LLables19, autopct="%1.1f%%")
plt.title("")
plt.savefig("PieSpot2019.pdf")



#2018
df_k3 = df2018.loc[mask18]

df_k3_countCountry = df_k3.groupby(["artist"]).count()["count"]
#print(df_k1_countCountry.sort_values())


# Pre-Processing
#print("NaNs?", df_k1.isnull().sum())

# Drop all NaNs
df_k3 = df_k3.dropna(axis=0)

df_k3h = df_k3.head(20)

# Visualization
Lsize18 = df_k3h.groupby(["artist"]).count()["count"]
LLables18 = df_k3h.groupby(["artist"]).count()["count"].index

# Figure
plt.figure(figsize=(7, 7))
plt.pie(Lsize18, labels=LLables18, autopct="%1.1f%%")
plt.title("")
plt.savefig("PieSpot2018.pdf")


#2017
df_k4 = df2017.loc[mask17]

df_k4_countCountry = df_k4.groupby(["artist"]).count()["count"]
#print(df_k1_countCountry.sort_values())


# Pre-Processing
#print("NaNs?", df_k1.isnull().sum())

# Drop all NaNs
df_k4 = df_k4.dropna(axis=0)

df_k4h = df_k4.head(20)

# Visualization
Lsize17 = df_k4h.groupby(["artist"]).count()["count"]
LLables17 = df_k4h.groupby(["artist"]).count()["count"].index

# Figure
plt.figure(figsize=(7, 7))
plt.pie(Lsize17, labels=LLables17, autopct="%1.1f%%")
plt.title("")
plt.savefig("PieSpot2017.pdf")



'''
Durchschnitt der Songlänge
'''

#Durchscnitslänge der songs
list = df_k1h["artist"].tolist()
#print(list)

filter = df_k1["artist"].isin(list)
df_k1f = df_k1.loc[filter]
#print(df_k1f["artist"].head(50))
df_k1f.drop_duplicates(subset="track", inplace=True, ignore_index=True)
#finde out tracks
#print(df_k1f["track"].head(50))

#df1 & df2
df1_urilist = df_k1f["uri"].tolist()


duration_filter = df2["Uri"].isin(df1_urilist)
df2f = df2.loc[duration_filter]


df2f.drop_duplicates(subset="Uri", inplace=True, ignore_index=True)

df2o = df2f["duration_ms"]
#print(df2o.mean())




'''
Worter im Titel check
'''
df_text = df_k1["title"]

df_k1.drop_duplicates(subset="title", inplace=True, ignore_index=True)

#print(df_k1[df_k1['title'].str.len() >= 4])
df_wordtitle = pd.Series(' '.join(df_k1['title']).lower().split()).value_counts()[: 142].head(20)
df_wordtitle.to_csv("WordTitle.csv")



# Just the End
print("Done")
