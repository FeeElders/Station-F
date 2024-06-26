from code.algoritmen import randomise as rd
from code import helpers

import matplotlib.pyplot as plt
import pandas as pd

import csv
import copy
import time
import pickle

from statistics import mean 
from datetime import datetime


def baseline(railway: 'Railway', traject_amount=None, heuristic = rd.Random, iterations = 100000, interval = 20) -> None:
    """ Run baseline experiment. """
    name = "random_baseline"
    title = "Random baseline"
    random_run(railway, traject_amount, name, heuristic, iterations, interval, title)   
        

def max_traject(railway: 'Railway', traject_amount: int, heuristic = rd.Random, iterations = 100000, interval = 20) -> None:
    """ Run Random algorithm with maximum trajectories. """
    name = "random_max_traject"
    title = "random max traject"
    random_run(railway, traject_amount, name, heuristic, iterations, interval, title)

def no_visited_connections_max(railway: 'Railway', traject_amount: int, heuristic = rd.NoVisitedConnections, iterations = 100000, interval = 20) -> None:
    """ Run NoVisitedConnections algorithm with maximum amount of trajectories."""
    name = "no_visited_connections"
    title = "no_visited_connections"
    random_run(railway, traject_amount, name, heuristic, iterations, interval, title)
                
def no_visited_connections_random(railway: 'Railway', traject_amount= None, heuristic = rd.NoVisitedConnections, iterations = 100000, interval = 20) -> None:
    """ Run NoVisitedConnections algorithm with random amount of trajectories."""
    name = "no_visited_connections_random"
    title = "no visited connections random"
    random_run(railway, traject_amount, name, heuristic, iterations, interval, title)
    

def not_so_random(railway: 'Railway', traject_amount: int, heuristic = rd.NotSoRandom, iterations = 100000, interval = 20) -> None:
    """ Run NotSoRandom algorithm. """
    name = "not_so_random"
    title = "Not so random"
    random_run(railway, traject_amount, name, heuristic, iterations, interval, title)


def trajectory_amount(railway: 'Railway', traject_amount: int, heuristic = rd.Random, iterations = 10000, interval = 20):
    """ Run Random algorithm for different trajectory amounts. """
    date = datetime.today().strftime('%d-%m-%Y')
    traject_amount = traject_amount
    
    if railway._max_trains == 7:
        prefix= "NH_"
        number_range = 4
    if railway._max_trains == 20:
        prefix= "NL_"
        number_range = 12
        
    for _ in range(number_range):
        name = f"{prefix}Random-{traject_amount}_traject_amount_{date}"
        title = f"random {traject_amount} trains"

        random_run(railway, traject_amount, name, heuristic, iterations, interval, title)
        traject_amount -= 1


def notsorandom_trajectory_amount(railway: 'Railway', traject_amount: int, heuristic = rd.NotSoRandom, iterations = 10000, interval = 20):
    """ Run Random algorithm for different trajectory amounts. """
    date = datetime.today().strftime('%d-%m-%Y')
    traject_amount = traject_amount
    
    if railway._max_trains == 7:
        prefix= "NH_"
        number_range = 4
    if railway._max_trains == 20:
        prefix= "NL_"
        number_range = 12
        
    for _ in range(number_range):
        name = f"{prefix}NotSoRandom-{traject_amount}_traject_amount_{date}"
        title = f"NotSoRandom {traject_amount} trains"

        random_run(railway, traject_amount, name, heuristic, iterations, interval, title)
        traject_amount -= 1
        

def random_run(railway: 'Railway', traject_amount: int, name: str, heuristic: 'Random', iterations: int, interval: int, title: str):
    """ Run the Random algorithm N times.

    Args:
    railway: the railway to start with
    traject_amount (int): the amount of trajectories to use
    name (str): the name of the file
    heuristic ('Random'): the random heuristic/inherited class
    iterations (int): the number of iterations to execute the algorithm
    interval (int): the interval at which output is saved to CSV file
    title (str): the title for the graph

    side effects:
    One CSV file is created for all the end scores and their iterations
    One CSV file is created for formatted output of the best railway found
    One barchart is saved for the end scores
    One railway map is saved for the visualisation of the best railway found
    """
    count = 0
    scoreplot:dict[int:int] = {}
    best_random_railway: 'Railway' = None
    
    # create a new file
    with open(f'output/random/{name}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['iterations','score'])
    
    print(f"random trajectory in the making\n")

    while count < iterations:
        start = time.time()
        random = heuristic(railway)
        random_railway = random.run(traject_amount)
        end = time.time()
        running_time = end - start

        if helpers.best_score(random_railway, best_random_railway):
            best_random_railway = copy.copy(random_railway)
            best_random_railway.formatted_output(f"random/best_{name}_railway.csv", running_time)
            helpers.object_output(best_random_railway, f"random/{name}")  
        scoreplot[count]= random_railway.score()
    
        if count%interval == 0:
            # sla elke +-10 minuten de scores op in een bestand
            with open(f'output/random/{name}.csv', 'a', newline='') as file:
                writer_new = csv.writer(file)
                for score in scoreplot:
                    writer_new.writerow([score, scoreplot[score]])
            scoreplot = {}
        count += 1
        
    with open(f'output/random/{name}.csv', 'a', newline='') as file:
        writer_new = csv.writer(file)
        for score in scoreplot:
            writer_new.writerow([score, scoreplot[score]])
            
    railway_map(f"random/{name}", title)
    graph(name, title)
    
def graph(name, title):
    """ Plot the end scores of every run in a bar chart """
    df = pd.read_csv(f'output/random/{name}.csv', delimiter=',')   
    count = len(df["score"])

    n_bins = 200

    # Generate a normal distributions
    dist1 = df['score']
    # We can set the number of bins with the *bins* keyword argument.
    plt.hist(dist1, bins=n_bins)
    plt.xlim(0, 8000)

    plt.xlabel('Score (K)')
    plt.ylabel('Frequentie')
    plt.title(f'{title}, {n_bins} bins {count} keer')

    #plt.show()
    plt.savefig(f"output/random/{title}.png")
    plt.close()
   
def railway_map(filename, title):
    """ Visualize the whole railway with dots as stations and lines as connections. """
    with open(f'output/{filename}.pkl', 'rb') as file:
        railway = pickle.load(file)
    
        
    number_of_trajectories = 20
    stations_list = railway.get_all_stations()
    labels = []
    x_values = []
    y_values = []
    colors = ["black", "deeppink", "plum", "olive", "orange", "grey", "firebrick", "darksalmon", "gold", "deepskyblue", "chartreuse", "green", "teal",  "blue", "indigo", "greenyellow", "crimson", "lemonchiffon", "darkmagenta", "azure", "bisque", "lightgrey"]
        
    # Add x-as and y-as list of each station
    for station in stations_list:
        labels.append(station._name)
        x_values.append(float(station._y)) 
        y_values.append(float(station._x))   
    
    plt.figure(figsize = (6,9))    
    plt.scatter(x_values, y_values)
    
    
    # plot all available connections
    
    all_connections = railway.get_all_connections()
    for connection in all_connections:
        x_connection = []
        y_connection = []
        station1 = connection._station1
        station2 = connection._station2
        x_connection.append(float(station1._y))
        y_connection.append(float(station1._x))
        x_connection.append(float(station2._y))
        y_connection.append(float(station2._x))
        plt.plot(x_connection, y_connection, color="lightgrey", linestyle="--")

    # Collect trajectories from railway
    trajectory_dict = railway._trains

    for i,traject in enumerate(trajectory_dict):
        station_list = trajectory_dict[traject].get_trajectory()
        xline = []
        yline = []
        for station in station_list:
            xline.append(float(station._y))
            yline.append(float(station._x))
        plt.plot(xline, yline, color=colors[i], linestyle="-")
    
    score = railway.score()
    plt.title(f'{title} met een score van: {score}')
    
    
    # plt.show()
    plt.savefig(f"output/random/map_{title}.png") 
    plt.close()
    

 
