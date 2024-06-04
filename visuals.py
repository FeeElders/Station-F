import matplotlib
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


"""
De visualisatie van de opties

Alle stations weergeven op de nederlandse kaart aan de hand van coördinaten.
Aan de hand van de algoritmen worden er trajecten gevormd. 
Deze worden weergegeven door een lijn van station naar station. 
De lijn bevat 1 van de 7 kleuren per traject:
Rood, Oranje, Geel, Groen, Blauw, Roze, Paars. 
Wanneer een station wordt gebruit wordt het vakje zwart. 
"""

# bron die ik heb gebruikt voor het maken van de nederlandse kaart
# https://stackoverflow.com/questions/60340577/python-geographical-plot-with-imported-data-e-g-from-the-netherlands

# mapdf = gpd.read_file("https://stacks.stanford.edu/file/druid:st293bj4601/data.zip")
#
# # sorted the data on the province names
# mapdf = mapdf[mapdf["TYPE_1"] == "Provincie"]
# mapdf.sort_values("NAME_1", inplace=True)
# mapdf = mapdf.reset_index(drop=True)

#https://github.com/fpgmaas/map-nl?tab=readme-ov-file 
from map_nl import ChoroplethMapNL

df = pd.read_csv("https://raw.githubusercontent.com/fpgmaas/map-nl/main/data/woz-pc4.csv")

m = ChoroplethMapNL(geojson_simplify_tolerance=0.0001).plot(
    df, pc4_column_name="pc4", value_column_name="WOZ", legend_name="Average WOZ Value"
)
m.save("map.html")