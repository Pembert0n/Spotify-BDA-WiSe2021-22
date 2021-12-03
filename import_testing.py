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

#Wenn beide Befehle funktionieren hat das impotieren der CSV Dateien funktioniert! (Ladezeit normal etwas länger)
#MÜSSEN 2 TABELLEN SEIN AM ENDE!
print(pd.read_csv("Database_to_calculate_popularity.csv"))
print(pd.read_csv("Final_database.csv"))