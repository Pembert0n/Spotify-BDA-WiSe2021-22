import numpy as np
import pandas as pd
"""
Da ich einfach nicht in der lage bin die CSV Datei in Github hochzuladen
würde ich bitten das das folgendermaßen erstmal gelöst wird:

1. Dateien von https://www.kaggle.com/pepepython/spotify-huge-database-daily-charts-over-3-years
herunterladen und entpacken.
Diese Datei kann direkt in das Projektverzeichniss rein und dort entpackt werden.

2. Die entpackten Dateien so umbenennen, dass alle Leerzeichen zu "_" (unterstrich werden).

Ich habe das Dateien Format .csv & .zip im .gitignore eingefügt, dasss es keine Probleme mit Commits und Pushes gibt.

Und weil Avram bestimmt fragen wird, Dateien die im .gitignore stehen werden nicht für Commits und Pushes berücksichtigt.

Wenn die Befehle unten funktionieren habt ihr alles richtig gemacht xdddd

~ LG Suphi
"""


"""
Das ist der Index mit allen Headern der Database_to_calculate_popularity.csv

Index(['Unnamed: 0', 'country', 'date', 'position', 'uri', 'track', 'title',
       'artist'],
      dtype='object')

df.loc[df["artist"] == "Ariana Grande"]
"""

#Wenn beide Befehle funktionieren hat das impotieren der CSV Dateien funktioniert! (Ladezeit normal etwas länger)
#MÜSSEN 2 TABELLEN SEIN AM ENDE!
#print(pd.read_csv("Database_to_calculate_popularity.csv"))
#df_csv = pd.read_csv("Final_database.csv")
df = pd.read_csv("Database_to_calculate_popularity.csv")
df["count"] = 1

df_count = df.groupby(["artist"]).count()["count"]
print(df_count.sort_values())



#print(df.groupby(["artist"]).mean().sort_values("position", ascending=False))