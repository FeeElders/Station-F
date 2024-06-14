import matplotlib
matplotlib.use("tkAgg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import csv



def line_graph(scores, count, fast_plot=False):
    """
    Plotten van de scores per algoritme in een hisogram
    y as komt het aantal pogingen en op de x as de score
    """

    n_bins = 400

    # Generate a normal distributions
    dist1 = scores.values()

    fig, axs = plt.subplots(sharey=True, tight_layout=True)

    # We can set the number of bins with the *bins* keyword argument.
    axs.hist(dist1, bins=n_bins)
    axs.set_xlim(0, 10000)
    axs.set(xlabel='score (K)', ylabel='aantal keer',
               title=f'Random algoritme 400 bins {iterations} keer')

    plt.show()

# def hillclimber_graph(scores, count, fast_plot=False):
#     """
#     Plotten van de score vs de iteraties in een histogram
#     y as komt de score en op de x as het aantal pogingen
#     """
#
#     n_bins = 400
#
#     # Generate a normal distributions
#     dist1 = scores.values()
#     iterations = [0:count]
#
#     fig, axs = plt.subplots(sharey=True, tight_layout=True)
#
#     # We can set the number of bins with the *bins* keyword argument.
#     axs.hist(iterations, dist1, bins=n_bins)
#     axs.set_xlim(0, count)
#     axs.set(xlabel='iteraties', ylabel='score',
#                title=f'Hill Climber algoritme 400 bins {iterations} keer')
#
#     plt.show()

    
def railway_map(best_random_railway):
    """
    De visualisatie van de opties

    Alle stations weergeven op de nederlandse kaart aan de hand van coördinaten.
    Aan de hand van de algoritmen worden er trajecten gevormd. 
    Deze worden weergegeven door een lijn van station naar station. 
    De lijn bevat 1 van de 7 kleuren per traject:
    Rood, Oranje, Geel, Groen, Blauw, Roze, Paars. 
    Wanneer een station wordt gebruit wordt het vakje zwart. 
    """
    stations_dict = best_random_railway._stations
    x_values = []
    y_values = []
        
    # Add x-as and y-as list
    for station in stations_dict:
        value=(stations_dict[station])
        x_values.append(float(value._y)) 
        y_values.append(float(value._x))   
        
    plt.figure(figsize = (6,9))
    plt.scatter(x_values, y_values) 
        
    # Collect trajectories from railway      
    trajectory_dict = best_random_railway._trains  
    my_colors = plt.rcParams['axes.prop_cycle']() 
    
    for traject in trajectory_dict:
        print(trajectory_dict[traject])
        station_list = trajectory_dict[traject]
        print(station_list)
        xline = []
        yline = []
        for station in station_list:
            print(station)
            xline.append(float(station._y))
            yline.append(float(station._x))
        plt.plot(xline, yline, linestyle="--") # **next(my_colors),

    
    plt.show()
    
    
    
    # To create line segments between two points in matplotlib, we can take the following steps
#
#     Set the figure size and adjust the padding between and around the subplots.
#     To make two points, create two lists.
#     Extract x and y values from point1 and point2.
#     Plot x and y values using plot() method.
#     Place text for both the points.
#     To display the figure, use show() method.
#     Example
#     import matplotlib.pyplot as plt
#     plt.rcParams["figure.figsize"] = [7.50, 3.50]
#     plt.rcParams["figure.autolayout"] = True
#     point1 = [1, 2]
#     point2 = [3, 4]
#     x_values = [point1[0], point2[0]]
#     y_values = [point1[1], point2[1]]
#     plt.plot(x_values, y_values, 'bo', linestyle="--")
#     plt.text(point1[0]-0.015, point1[1]+0.25, "Point1")
#     plt.text(point2[0]-0.050, point2[1]-0.25, "Point2")
#     plt.show()
    
    
    
    
    
    
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





