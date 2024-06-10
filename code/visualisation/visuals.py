import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

"""
Plotten van de scores per algoritme in een lijn grafiek
y as komt de score en op de x as het aantal pogingen
"""

def visualise(scores, fast_plot=False):
    
    # iteration = scores.keys()
#     score = scores.values()
#
#     x = iteration
#     y = score
#
#     fig, ax = plt.subplots()
#     ax.plot(x, y, 'o')
#
#     ax.set(xlabel='iteration', ylabel='score (K)',
#            title='Random algoritme')
#     ax.grid()
#
#     fig.savefig("random.png")
#     plt.show()
    
    n_bins = 20

    # Generate a normal distributions
    dist1 = scores.values()

    fig, axs = plt.subplots(sharey=True, tight_layout=True)

    # We can set the number of bins with the *bins* keyword argument.
    axs.hist(dist1, bins=n_bins)

    plt.show()
    
    





"""
De visualisatie van de opties

Alle stations weergeven op de nederlandse kaart aan de hand van coördinaten.
Aan de hand van de algoritmen worden er trajecten gevormd. 
Deze worden weergegeven door een lijn van station naar station. 
De lijn bevat 1 van de 7 kleuren per traject:
Rood, Oranje, Geel, Groen, Blauw, Roze, Paars. 
Wanneer een station wordt gebruit wordt het vakje zwart. 
"""
#https://matplotlib.org/basemap/stable/users/merc.html 

# from mpl_toolkits.basemap import Basemap
# import numpy as np
# import matplotlib.pyplot as plt
# # llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
# # are the lat/lon values of the lower left and upper right corners
# # of the map.
# # lat_ts is the latitude of true scale.
# # resolution = 'c' means use crude resolution coastlines.
# m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,\
#             llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')
# m.drawcoastlines()
# m.fillcontinents(color='coral',lake_color='aqua')
# # draw parallels and meridians.
# m.drawparallels(np.arange(-90.,91.,30.))
# m.drawmeridians(np.arange(-180.,181.,60.))
# m.drawmapboundary(fill_color='aqua')
# plt.title("Mercator Projection")
# plt.show()





