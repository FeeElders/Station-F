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

#plotting data on map from https://matplotlib.org/basemap/stable/
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

class Basemap(object):
    def __init__(self, llcrnrlon=None, llcrnrlat=None,
                       urcrnrlon=None, urcrnrlat=None,
                       llcrnrx=None, llcrnry=None,
                       urcrnrx=None, urcrnry=None,
                       width=None, height=None,
                       projection='cyl', resolution='c',
                       area_thresh=None, rsphere=6370997.0,
                       ellps=None, lat_ts=None,
                       lat_1=None, lat_2=None,
                       lat_0=None, lon_0=None,
                       lon_1=None, lon_2=None,
                       o_lon_p=None, o_lat_p=None,
                       k_0=None,
                       no_rot=False,
                       suppress_ticks=True,
                       satellite_height=35786000,
                       boundinglat=None,
                       fix_aspect=True,
                       anchor='C',
                       celestial=False,
                       round=False,
                       epsg=None,
                       ax=None):

   

#https://matplotlib.org/basemap/stable/users/merc.html



# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
# are the lat/lon values of the lower left and upper right corners
# of the map.
# resolution = 'c' means use crude resolution coastlines.
m = Basemap(projection='cyl',llcrnrlat=-90,urcrnrlat=90,\
            llcrnrlon=-180,urcrnrlon=180,resolution='c')
m.drawcoastlines()
m.fillcontinents(color='coral',lake_color='aqua')
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,91.,30.))
m.drawmeridians(np.arange(-180.,181.,60.))
m.drawmapboundary(fill_color='aqua') 
plt.title("Equidistant Cylindrical Projection")
plt.show()


# andere bron:
# https://stackoverflow.com/questions/60340577/python-geographical-plot-with-imported-data-e-g-from-the-netherlands

# mapdf = gpd.read_file("https://stacks.stanford.edu/file/druid:st293bj4601/data.zip")
#
# # sorted the data on the province names
# mapdf = mapdf[mapdf["TYPE_1"] == "Provincie"]
# mapdf.sort_values("NAME_1", inplace=True)
# mapdf = mapdf.reset_index(drop=True)



# bron die ik heb gebruikt voor het maken van de nederlandse kaart
#https://github.com/fpgmaas/map-nl?tab=readme-ov-file 
# from map_nl import ChoroplethMapNL
#
# df = pd.read_csv("https://raw.githubusercontent.com/fpgmaas/map-nl/main/data/woz-pc4.csv")
#
# m = ChoroplethMapNL(geojson_simplify_tolerance=0.0001).plot(
#     df, pc4_column_name="pc4", value_column_name="WOZ", legend_name="Average WOZ Value"
# )
# m.save("map.html")