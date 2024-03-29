# @since: 2021-12-03
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.options.mode.chained_assignment = None


'''
Einlesen der CSV Dateien
'''

df1 = pd.read_csv("Database_to_calculate_popularity.csv")
df1["count"] = 1

df2 = pd.read_csv("Final_database.csv")
df2["count"] = 1


'''
Zeitunterteilung für den fogelnden abschnitt
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
Hier werden die Charts der best 20 Künstelr der Jahre 2017 - 2020 gefiltert
'''


#Top 20 Künstler in den Charts
#Fügt die Filter zu den jeweiligen Dataframes hinzu und zählt die Artist im jewiligen Dataframe
df_k1 = df2020.loc[mask]
df_k1_countCountry = df_k1.groupby(["artist"]).count()["count"]

df_k2 = df2019.loc[mask19]
df_k2_countCountry = df_k2.groupby(["artist"]).count()["count"]

df_k3 = df2018.loc[mask18]
df_k3_countCountry = df_k3.groupby(["artist"]).count()["count"]

df_k4 = df2017.loc[mask17]
df_k4_countCountry = df_k4.groupby(["artist"]).count()["count"]


#2020
# entferne alle NaNs
df_k1 = df_k1.dropna(axis=0)

df_k1h = df_k1.head(20)

# Visualization
Lsize = df_k1h.groupby(["artist"]).count()["count"]
LLables = df_k1h.groupby(["artist"]).count()["count"].index

# Figure
plt.figure(figsize=(10, 10))
plt.pie(Lsize, labels=LLables, autopct="%1.1f%%")
plt.tight_layout()
plt.title("")
plt.savefig("PieSpot2020.png")


#2019
#Entfernt all NaNs
df_k2 = df_k2.dropna(axis=0)

#Gibt die top 20 wieder
df_k2h = df_k2.head(20)

# Visualization
Lsize19 = df_k2h.groupby(["artist"]).count()["count"]
LLables19 = df_k2h.groupby(["artist"]).count()["count"].index

# Figure
plt.figure(figsize=(10, 10))
plt.pie(Lsize19, labels=LLables19, autopct="%1.1f%%")
plt.tight_layout()
plt.title("")
plt.savefig("PieSpot2019.png")



#2018
# Entferne all NaNs
df_k3 = df_k3.dropna(axis=0)

#Filtert die top 20 heraus
df_k3h = df_k3.head(20)

# Visualisierungsparameter
Lsize18 = df_k3h.groupby(["artist"]).count()["count"]
LLables18 = df_k3h.groupby(["artist"]).count()["count"].index

# Figur
plt.figure(figsize=(10, 10))
plt.pie(Lsize18, labels=LLables18, autopct="%1.1f%%")
plt.tight_layout()
plt.title("")
plt.savefig("PieSpot2018.png")


#2017
# Entferne alle NaNs
df_k4 = df_k4.dropna(axis=0)

#wähle die top 20 aus
df_k4h = df_k4.head(20)

# Visualisierungsparameter
Lsize17 = df_k4h.groupby(["artist"]).count()["count"]
LLables17 = df_k4h.groupby(["artist"]).count()["count"].index

# Figur
plt.figure(figsize=(10, 10))
plt.pie(Lsize17, labels=LLables17, autopct="%1.1f%%")
plt.tight_layout()
plt.title("")
plt.savefig("PieSpot2017.png")



'''
Durchschnitt der Songlänge
'''

#Fügt alle künstler vom Dataframe1 zu einer liste hinzu
list = df_k1h["artist"].tolist()

#generiert den Filter mithilöfe der list
filter = df_k1["artist"].isin(list)
df_k1f = df_k1.loc[filter]
#entfernt Duplikate in df1
df_k1f.drop_duplicates(subset="track", inplace=True, ignore_index=True)

#fügt alle uri von df1 zu einer liste hinzu
df1_urilist = df_k1f["uri"].tolist()

#erstellt filter und filter direkt df2 nach den passenden Tracks
duration_filter = df2["Uri"].isin(df1_urilist)
df2f = df2.loc[duration_filter]

#entfernt Duplikate in df2
df2f.drop_duplicates(subset="Uri", inplace=True, ignore_index=True)

#gibt Durchschnitslänge als String aus
lengh_string = df2f["duration_ms"].mean()
print("Länge: " + str(lengh_string))




'''
Worter im Titel check
'''
#filter und fügt den text alls variable hinzu
df_text = df_k1["title"]

#entfernt Duplicate
df_k1.drop_duplicates(subset="title", inplace=True, ignore_index=True)

#zählt die am häufigst genutzentn wörter und fügt sie zu einer .CSV Datei hinzu
df_wordtitle = pd.Series(' '.join(df_k1['title']).lower().split()).value_counts()[: 142].head(20)
df_wordtitle.to_csv("WordTitle.csv")


'''
Genre der Tracks der beliebtesten 20 Künstler
'''

# Visualisierung von Genre
# Hier werden die Genre aus df2 gezählt sowie auch ihre Namen als Index gespeicheirt
LsizeGenre = df2f.groupby(["Genre"]).count()["count"]
LLablesGenre = df2f.groupby(["Genre"]).count()["count"].index

# kuchendiegram wird erstellt und gepeichert
plt.figure(figsize=(10, 10))
plt.tight_layout()
plt.pie(LsizeGenre, labels=LLablesGenre, autopct="%1.1f%%")
plt.title("")
plt.savefig("Genre.png")


'''
Explicit
'''

# Visualisierung von Explicit
# Hier werden die Explicit aus df2 gezählt sowie auch ihre Namen als Index gespeicheirt
LsizeGenre = df2f.groupby(["Explicit"]).count()["count"]
LLablesGenre = df2f.groupby(["Explicit"]).count()["count"].index

# Figure
plt.figure(figsize=(10, 10))
plt.pie(LsizeGenre, labels=LLablesGenre, autopct="%1.1f%%")
plt.tight_layout()
plt.title("")
plt.savefig("Explicit.png")


'''
Danceability
'''
#berechnet den durchschintt der deancability
d2f2dance_string = df2f["danceability"].mean()
print("Danceability: " + str(d2f2dance_string))


'''
Loudness
'''
#berechnet die durchscnittliche loudness
df2floud_string = df2f["loudness"].mean()
print("Loudness: " + str(df2floud_string))

'''
Speechiness
'''
#berechnet die durchscnittliche speechiness
df2fspeech_string = df2f["speechiness"].mean()
print("Speechiness: " + str(df2fspeech_string))

'''
Aucustics
'''
#berechnet die durchscnittlichen Aucustics
df2facoust_string = df2f["acoustics"].mean()
print("Aucustics: " + str(df2facoust_string))

'''
Tempo
'''
#berechnet das durchscnittliche Tempo
df2ftempo_string = df2f["tempo"].mean()
print("Tempo: " + str(df2ftempo_string))


# Just the End
print("Done")

