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
               title=f'Random algoritme 400 bins {count} keer')

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

# Lijst maken van de pogingen
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
    labels = []
    x_values = []
    y_values = []
    colors = ["black", "grey", "firebrick", "darksalmon", "lightgrey", "gold", "chartreuse", "green", "teal", "deepskyblue", "blue", "indigo", "deeppink", "plum", "olive", "orange", "greenyellow", "crimson", "lemonchiffon", "darkmagenta", "azure", "bisque"]
        
    # Add x-as and y-as list
    for station in stations_dict:
        value=(stations_dict[station])
        labels.append(value._name)
        x_values.append(float(value._y)) 
        y_values.append(float(value._x))   
        
    plt.figure(figsize = (6,9))
    plt.scatter(x_values, y_values) 
    # # Add labels using annotate()
 #    for i, label in enumerate(labels):
 #        plt.annotate(label, (x_values[i], y_values[i]))

    # Collect trajectories from railway
    trajectory_dict = best_random_railway._trains

    for i,traject in enumerate(trajectory_dict):
        station_list = trajectory_dict[traject].get_trajectory()
        xline = []
        yline = []
        for station in station_list:
            xline.append(float(station._y))
            yline.append(float(station._x))
        plt.plot(xline, yline, color=colors[i], linestyle="-")

    
    plt.show()
    
    
    






