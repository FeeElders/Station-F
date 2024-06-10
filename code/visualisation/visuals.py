import matplotlib
import matplotlib.pyplot as plt

"""
Plotten van de scores per algoritme in een lijn grafiek
y as komt de score en op de x as het aantal pogingen
"""
import numpy as np


# Get the scores of the algorithm. 
    # scores = [node for node in graph.nodes.values()]
    # name = [node.id for node in regions]
    # cost = [node.value.value if node is not None else 0
    #         for node in regions]
    # colour = [node.value.colour.get_web() if node is not None else "grey"
    #           for node in regions]
    # transmitter = [node.value.name if node is not None else "None"
    #                for node in regions]
def visualise(scores, fast_plot=False):
    
    iteration = []
    score = []
    
    for row in scores:
        iteration.append(row.key())
        score.append(row.value()) 

    x = iteration
    y = score
   
    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.set(xlabel='iteration', ylabel='score (K)',
           title='Random algoritme')
    ax.grid()

    fig.savefig("random.png")
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





