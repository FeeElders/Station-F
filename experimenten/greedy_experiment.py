from code.algoritmen import greedy as gr
from code import helpers
from code.visualisation import visuals

import matplotlib.pyplot as plt
import pandas as pd
import csv
import copy
import time

from statistics import mean 
from datetime import datetime

def greedy(railway: 'Railway') -> None:
    """ Run greedy N times with 15 trajectories. """
    date = datetime.today().strftime('%d-%m-%Y')
    name = f"Greedy_{date}"
    scoreplot:dict[int:int] = {}
    count = 0
    interval = 100
    
    # create a new file
    with open(f'output/greedy/{name}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['iterations','score'])

    start = time.time()
    while count < 1000:
        greedy = gr.Greedy(railway)
        greedy_railway = greedy.run(15)
        end = time.time()
        running_time = end-start

        greedy_railway.formatted_output(f"greedy/formatted_output_{name}_run_{count}.csv", running_time)
        scoreplot[count] = greedy_railway.score()
        
        if count%interval == 0:
            # print something to show that still running
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
            
    return name


def smart_greedy(railway: 'Railway') -> None:
    """ Run SmartStartStation greedy N times with 15 trajectories. """
    date = datetime.today().strftime('%d-%m-%Y')
    name = f"SmartGreedy_{date}"
    scoreplot:dict[int:int] = {}
    count = 0
    interval = 100
    
    # create a new file
    with open(f'output/greedy/{name}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['iterations','score'])

    start = time.time()
    while count < 1000:
        smart_greedy = gr.SmartStartStation(railway)
        smart_railway = smart_greedy.run(15)
        end = time.time()
        running_time = end-start

        smart_railway.formatted_output(f"greedy/formatted_output_{name}_run_{count}.csv", running_time)
        scoreplot[count] = smart_railway.score()
        
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
            
    return name


def random_greedy(railway: 'Railway') -> None:
    """ run experiment with random greedy through smart start """
    date = datetime.today().strftime('%d-%m-%Y')
    name = f"RandomGreedy_{date}"
    scoreplot:dict[int:int] = {}
    count = 0
    interval = 100
    
    # create a new file
    with open(f'output/greedy/{name}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['iterations','score'])

    start = time.time()
    while count < 1000:
        smart_greedy = gr.RandomGreedy(railway)
        smart_railway = smart_greedy.run(15)
        end = time.time()
        running_time = end-start

        smart_railway.formatted_output(f"greedy/formatted_output_{name}_run_{count}.csv", running_time)
        scoreplot[count] = smart_railway.score()
        
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
            
    return name


def trajectory_amount(railway: 'Railway') -> None:
    """ Run SmartStartStation greedy N times with 15 trajectories. """

    train_count = 20
    for _ in range(10):
        date = datetime.today().strftime('%d-%m-%Y')
        name = f"SmartGreedy_{date}_{train_count}_trains"
        scoreplot:dict[int:int] = {}
        count = 0
        interval = 100
    
        # create a new file
        with open(f'output/greedy/{name}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['iterations','score'])

        start = time.time()
        while count < 1000:
            smart_greedy = gr.SmartStartStation(railway)
            smart_railway = smart_greedy.run(train_count)
            end = time.time()
            running_time = end-start

            scoreplot[count] = smart_railway.score()
        
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
        train_count -= 1
        graph(name)


def railway_map(filename):
    """
    De visualisatie van de opties

    Alle stations weergeven op de nederlandse kaart aan de hand van coördinaten.
    Aan de hand van de algoritmen worden er trajecten gevormd. 
    Deze worden weergegeven door een lijn van station naar station. 
    De lijn bevat 1 van de 7 kleuren per traject:
    Rood, Oranje, Geel, Groen, Blauw, Roze, Paars. 
    Wanneer een station wordt gebruit wordt het vakje zwart. 
    """
    fig, ax = plt.subplots()
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
    plt.title(f'{filename} met een score van: {score}')
    

    #plt.show()
    fig.savefig(f"output/greedy/visual_baseline_greedy.png") 


def graph(name):
    """
    Plotten van de scores per experiment in een hisogram
    y as komt het aantal pogingen en op de x as de score
    """
    fig, ax = plt.subplots()
    df = pd.read_csv(f'output/greedy/{name}.csv', delimiter=',')   
    count = len(df["score"])

    print(f"dataframe: {df}")
    n_bins = 400

    # Generate a normal distributions
    dist1 = df['score']
    print(dist1)
    # We can set the number of bins with the *bins* keyword argument.
    ax.hist(dist1, bins=n_bins)
    ax.set_xlim(0, 10000)
    
    ax.set(xlabel='Score (K)', ylabel='Frequentie',
               title=f'{name} {n_bins} bins {count} keer')

    #plt.show()
    fig.savefig(f"output/greedy/{name}.png")
