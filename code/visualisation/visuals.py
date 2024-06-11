import matplotlib
matplotlib.use("tkAgg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import csv



def line_graph(scores, fast_plot=False):
    """
    Plotten van de scores per algoritme in een lijn grafiek
    y as komt de score en op de x as het aantal pogingen
    """

    n_bins = 20

    # Generate a normal distributions
    dist1 = scores.values()

    fig, axs = plt.subplots(sharey=True, tight_layout=True)

    # We can set the number of bins with the *bins* keyword argument.
    axs.hist(dist1, bins=n_bins)
    axs.set_xlim(0, 10000)
    axs.set(xlabel='score (K)', ylabel='aantal keer',
               title='Random algoritme')

    plt.show()

    
def railway_map(station_csv, connections):
    """
    De visualisatie van de opties

    Alle stations weergeven op de nederlandse kaart aan de hand van coördinaten.
    Aan de hand van de algoritmen worden er trajecten gevormd. 
    Deze worden weergegeven door een lijn van station naar station. 
    De lijn bevat 1 van de 7 kleuren per traject:
    Rood, Oranje, Geel, Groen, Blauw, Roze, Paars. 
    Wanneer een station wordt gebruit wordt het vakje zwart. 
    """

    station_name = []
    x_values = []
    y_values = []
    
    # read csv files with station coÃ¶rdinates
    with open(station_csv) as file:
        reader = csv.reader(file)
    
        # skip the first line (header)
        next(reader)
        
        #Add x-as and y-as list
        for name, x, y in reader:
            station_name.append(name) 
            x_values.append(float(y)) 
            y_values.append(float(x))
            

    plt.figure(figsize = (6,9))
    plt.scatter(x_values, y_values) 
    plt.show()
    
    
    
    
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





