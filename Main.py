# @since: 2021-12-03
'''
Link zur Hausarbeit:
https://studhsheilbronnde-my.sharepoint.com/:w:/g/personal/spembe_stud_hs-heilbronn_de/EdtQ7nqM4p5MqvPq2Zoj30oBSpqMtPRbKED2AKkgTx8agA?e=9N16hW
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Einlesen der CSV
#df2 = pd.read_csv("Final_database.csv")

df1 = pd.read_csv("Database_to_calculate_popularity.csv")
df1["count"] = 1

#Zum zählen der Zeilen und Spalten von df1
#print('Number of colums in Dataframe : ', len(df1.columns)) #Number of colums in Dataframe :  9
#print('Number of rows in Dataframe : ', len(df1.index))#Number of rows in Dataframe :  9807001

#Anzeigeoptionen zurücksetzen
#pd.reset_option('display.max_colwidth')
#pd.reset_option('display.max_rows')
#pd.reset_option('display.max_columns')
#pd.reset_option('display.width')


df1_countArtist = df1.groupby(["artist"]).count()["count"]
print(df1_countArtist.sort_values().tail(20))#teil für die anzahl die man sehen will
print(df1.info)


# Dimensionality of the DataFrame
#print(df.shape)

# Get Info
#print(df.info())

# Pre-Processing
print("NaNs?", df.isnull().sum())

# Drop all NaNs
df = df.dropna(axis=0)
print("After NaNs Drop", df.isnull().sum())

# Visualization
Lsize = df["artist"].value_counts()
LLables = df["artist"].value_counts().index

# Figure
plt.figure(figsize=(7, 7))
plt.pie(Lsize, labels=LLables, autopct="%1.1f%%")
plt.title("Traks nach Land")
plt.savefig("PieSpot.pdf")

# Just the End
print("Done")
