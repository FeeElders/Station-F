from code.algoritmen import greedy as gr
from code import helpers
from code.visualisation import visuals

import matplotlib.pyplot as plt
import pandas as pd
import csv
import copy
import time
import pickle

from statistics import mean 
from datetime import datetime


def greedy(railway: 'Railway', traject_amount: int, heuristic = gr.Greedy, iterations = 1000, interval = 500) -> None:
    """ Run greedy N times with 15 trajectories. """
    date = datetime.today().strftime('%d-%m-%Y')
    name = f"Greedy_{date}"
    title = "Greedy baseline"
    greedy_run(railway, traject_amount, name, heuristic, iterations, interval, title)
    

def smart_trajectory_amount(railway: 'Railway', traject_amount: int, heuristic = gr.SmartStartStation, iterations = 100, interval = 20) -> None:
    """ Run SmartStartStation greedy N times with 15 trajectories. """
    date = datetime.today().strftime('%d-%m-%Y')
    traject_amount = traject_amount
    
    if railway._max_trains == 7:
        prefix = "NH_"
        number_range = 4
    if railway._max_trains == 20:
        prefix = "NL_"
        number_range = 12
        
    for _ in range(number_range):
        title = f"Smart Greedy {traject_amount} trains"
        name = f"{prefix}SmartGreedy-{traject_amount}_trains_{date}"
        greedy_run(railway, traject_amount, name, heuristic, iterations, interval, title)
        traject_amount -= 1

def trajectory_amount(railway: 'Railway', traject_amount: int, heuristic = gr.Greedy, iterations = 100, interval = 20) -> None:
    """ Run SmartStartStation greedy N times with 15 trajectories. """
    date = datetime.today().strftime('%d-%m-%Y')
    traject_amount = traject_amount
    
    if railway._max_trains == 7:
        prefix = "NH_"
        number_range = 4
    if railway._max_trains == 20:
        prefix = "NL_"
        number_range = 12
        
    for _ in range(number_range):
        title = f"Greedy {traject_amount} trains"
        name = f"{prefix}Greedy-{traject_amount}_trains_{date}"
        greedy_run(railway, traject_amount, name, heuristic, iterations, interval, title)
        traject_amount -= 1

def smart_greedy(railway: 'Railway', traject_amount: int, heuristic = gr.SmartStartStation, iterations = 1000, interval = 500) -> None:
    """ Run SmartStartStation greedy N times with 15 trajectories. """
    date = datetime.today().strftime('%d-%m-%Y')
    name = f"SmartGreedy_{date}"
    title = " Smart greedy"
    greedy_run(railway, traject_amount, name, heuristic, iterations, interval, title)
          

def random_greedy(railway: 'Railway', traject_amount: int, heuristic = gr.RandomGreedy, iterations = 1000, interval = 500) -> None:
    """ run experiment with random greedy through smart start """
    date = datetime.today().strftime('%d-%m-%Y')
    name = f"RandomGreedy_{date}"
    title = "Random greedy"
    greedy_run(railway, traject_amount, name, heuristic, iterations, interval, title)


def greedy_run(railway: 'Railway', traject_amount: int, name: str, heuristic, iterations: int, interval: int, title: str):
    scoreplot:dict[int:int] = {}
    count = 0
    best_greedy_railway: 'Railway' = None
        
    # create a new file
    with open(f'output/greedy/{name}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['iterations','score'])

    while count < iterations:
        start = time.time()
        greedy = heuristic(railway)
        railway = greedy.run(traject_amount)
        end = time.time()
        running_time = end-start


        if helpers.best_score(railway, best_greedy_railway) and railway.trains() > 0:
            best_greedy_railway = copy.copy(railway)
            print(best_greedy_railway)
            best_greedy_railway.formatted_output(f"best_{name}_railway.csv", running_time)
            helpers.object_output(best_greedy_railway, f"greedy/{name}")
        scoreplot[count] = railway.score()
        
        if count%interval == 0:
            #Print something to show that still running
            print(f"run {count}, downloading to csv")
            # sla elke +-10 minuten de scores op in een bestand
            with open(f'output/greedy/{name}.csv', 'a', newline='') as file:
                writer_new = csv.writer(file)
                for score in scoreplot:
                    writer_new.writerow([score, scoreplot[score]])
            scoreplot= {}
        count += 1  
    with open(f'output/greedy/{name}.csv', 'a', newline='') as file:
        writer_new = csv.writer(file)
        for score in scoreplot:
            writer_new.writerow([score, scoreplot[score]])
            
    helpers.object_output(railway, f"greedy/{name}")       
    railway_map(f"greedy/{name}", title)
    graph(name, title)

def railway_map(filename, title):
    """
    De visualisatie van de opties

    Alle stations weergeven op de nederlandse kaart aan de hand van coördinaten.
    Aan de hand van de algoritmen worden er trajecten gevormd. 
    Deze worden weergegeven door een lijn van station naar station. 
    De lijn bevat 1 van de 7 kleuren per traject:
    Rood, Oranje, Geel, Groen, Blauw, Roze, Paars. 
    Wanneer een station wordt gebruit wordt het vakje zwart. 
    """
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
    plt.savefig(f"output/greedy/{title}.png") 
    plt.close()


def graph(name, title):
    """
    Plotten van de scores per experiment in een hisogram
    y as komt het aantal pogingen en op de x as de score
    """
    df = pd.read_csv(f'output/greedy/{name}.csv', delimiter=',')   
    count = len(df["score"])

    n_bins = 1

    # Generate a normal distributions
    dist1 = df['score']

    # We can set the number of bins with the *bins* keyword argument.
    plt.hist(dist1, bins=n_bins)
    plt.xlim(0, 8000)
    
    plt.xlabel('Score (K)')
    plt.ylabel('Frequentie')
    plt.title(f'{title}, {n_bins} bins {count} keer')

    # plt.show()
    plt.savefig(f"output/greedy/{title}.png")
    plt.close()
