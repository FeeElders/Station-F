from code.algoritmen import randomise as rd
from code import helpers
from code.visualisation import visuals 

import matplotlib.pyplot as plt
import pandas as pd

import csv
import copy
import time

from statistics import mean 


def baseline(railway):
    count = 0
    scoreplot:dict[int:int] = {}
    best_random_railway: 'Railway' = None
    name = "nh_random_baseline"
    interval = 20
    
    # create a new file
    with open(f'output/random/{name}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['iterations','score'])
    
    start = time.time()
    while count < 10000:
      random = rd.Random(railway)
      random_railway = random.run()
      end = time.time()
      running_time = end - start

      if helpers.best_score(random_railway, best_random_railway):
          best_random_railway = copy.copy(random_railway)
          best_random_railway.formatted_output(f"best_{name}_railway.csv", running_time)
      scoreplot[count]= random_railway.score()
      
      if count%interval == 0:
            # sla elke +-10 minuten de scores op in een bestand
            with open(f'output/random/{name}.csv', 'a', newline='') as file:
                writer_new = csv.writer(file)
                for score in scoreplot:
                    writer_new.writerow([score, scoreplot[score]])
            scoreplot= {}
      count += 1  
    with open(f'output/random/{name}.csv', 'a', newline='') as file:
        writer_new = csv.writer(file)
        for score in scoreplot:
            writer_new.writerow([score, scoreplot[score]])
            
    return name
        
      
def max_traject(railway, max_trajectories):
    count = 0
    scoreplot:dict[int:int] = {}
    best_random_railway: 'Railway' = None
    name = "nh_random_max_traject"
    interval = 20
    
    # create a new file
    with open(f'output/random/{name}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['iterations','score'])
    
    start = time.time()
    while count < 10000:
        random = rd.Random(railway)
        random_railway = random.run(max_trajectories)
        end = time.time()
        running_time = end - start
        

        if helpers.best_score(random_railway, best_random_railway):
            best_random_railway = copy.copy(random_railway)
            best_random_railway.formatted_output(f"best_{name}_railway.csv", running_time)
        scoreplot[count]= random_railway.score()
        
        if count%interval == 0:
            # sla elke +-10 minuten de scores op in een bestand
            with open(f'output/random/{name}.csv', 'a', newline='') as file:
                writer_new = csv.writer(file)
                for score in scoreplot:
                    writer_new.writerow([score, scoreplot[score]])
            scoreplot= {}
        count += 1
    with open(f'output/random/{name}.csv', 'a', newline='') as file:
        writer_new = csv.writer(file)
        for score in scoreplot:
            writer_new.writerow([score, scoreplot[score]])
    
    return name 

def no_visited_connections_max(railway, max_trajectories):
    """
    Also with max traject
    """
    count = 0
    scoreplot:dict[int:int] = {}
    best_random_railway: 'Railway' = None
    name = "nh_no_visited_connections"
    interval = 20
    
    # create a new file
    with open(f'output/random/{name}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['iterations','score'])    
    
    start = time.time()
    while count < 10000:
        nvc_random = rd.NoVisitedConnections(railway)
        random_railway = nvc_random.run(max_trajectories)
        end = time.time()
        running_time = end - start
        
        if helpers.best_score(random_railway, best_random_railway):
            best_random_railway = copy.copy(random_railway)
            best_random_railway.formatted_output(f"best_{name}_railway.csv", running_time)
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
    
    return name    
            
def no_visited_connections_random(railway, max_trajectories):
    """
    Also with max traject
    """
    count = 0
    scoreplot:dict[int:int] = {}
    best_random_railway: 'Railway' = None
    name = "nh_no_visited_connections"
    interval = 20
    
    # create a new file
    with open(f'output/random/{name}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['iterations','score'])    
    
    start = time.time()
    while count < 10000:
        nvc_random = rd.NoVisitedConnections(railway)
        random_railway = nvc_random.run()
        end = time.time()
        running_time = end - start
        
        if helpers.best_score(random_railway, best_random_railway):
            best_random_railway = copy.copy(random_railway)
            best_random_railway.formatted_output(f"best_{name}_railway.csv", running_time)
        scoreplot[count]= random_railway.score()
        
        if count%interval == 0:
            # sla elke +-10 minuten de scores op in een bestand
            with open(f'output/random/{name}.csv', 'a', newline='') as file:
                writer_new = csv.writer(file)
                for score in scoreplot:
                    writer_new.writerow([score, scoreplot[score]])
            scoreplot= {}
        count += 1 
    with open(f'output/random/{name}.csv', 'a', newline='') as file:
        writer_new = csv.writer(file)
        for score in scoreplot:
            writer_new.writerow([score, scoreplot[score]]) 

    return name
            
def not_so_random(railway, max_trajectories):
    """
    Gestuurde start staion en gestuurde connection
    
    begin station dat nog niet is geweest en een verbinding die nog niet is geweest. beide tenzij het niet anders kan
    """
    count = 0
    scoreplot:dict[int:int] = {}
    best_random_railway: 'Railway' = None
    name = "nh_not_so_random"
    interval = 20
    
    # create a new file
    with open(f'output/random/{name}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['iterations','score'])
    
    print(f"not so random trajectories in the making\n")
    start = time.time()
    while count < 10000:
        ns_random = rd.NotSoRandom(railway)
        random_railway = ns_random.run(max_trajectories)
        end = time.time()
        running_time = end - start

        if helpers.best_score(random_railway, best_random_railway):
            best_random_railway = copy.copy(random_railway)
            best_random_railway.formatted_output(f"best_{name}_railway.csv", running_time)
        scoreplot[count]= random_railway.score()
        
        if count%interval == 0:
            # sla elke +-10 minuten de scores op in een bestand
            with open(f'output/random/{name}.csv', 'a', newline='') as file:
                writer_new = csv.writer(file)
                for score in scoreplot:
                    writer_new.writerow([score, scoreplot[score]])
            scoreplot= {}
        count += 1
    with open(f'output/random/{name}.csv', 'a', newline='') as file:
        writer_new = csv.writer(file)
        for score in scoreplot:
            writer_new.writerow([score, scoreplot[score]])
    
    return name


def trajectory_amount(railway):

    train_count = 20
    for _ in range(10):
        count = 0
        scoreplot:dict[int:int] = {}
        best_random_railway: 'Railway' = None
        name = f"nh_not_so_random_{train_count}_trains"
        interval = 20
        
        # create a new file
        with open(f'output/random/{name}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['iterations','score'])
        
        print(f"not so random trajectory {train_count} in the making\n")

        while count < 1000:
            start = time.time()
            ns_random = rd.NotSoRandom(railway)
            random_railway = ns_random.run(train_count)
            end = time.time()
            running_time = end - start

            if helpers.best_score(random_railway, best_random_railway):
                best_random_railway = copy.copy(random_railway)
                best_random_railway.formatted_output(f"best_{name}_railway.csv", running_time)
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
        train_count -= 1
        graph(name)
    return name    
    
def graph(name):
    """
    Plotten van de scores per experiment in een hisogram
    y as komt het aantal pogingen en op de x as de score
    """
    fig, ax = plt.subplots()
    df = pd.read_csv(f'output/random/{name}.csv', delimiter=',')   
    count = len(df["score"])
   
    n_bins = 400

    # Generate a normal distributions
    dist1 = df['score']
    print(df['score'])

    # We can set the number of bins with the *bins* keyword argument.
    ax.hist(dist1, bins=n_bins)
    ax.set_xlim(0, 8000)
    
    ax.set(xlabel='Score (K)', ylabel='Frequentie',
               title=f'{name} 400 bins {count} keer')

#    plt.show()
    fig.savefig(f"output/random/{name}.png")
   
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
    

    plt.show()
    fig.savefig(f"output/random/visual_baseline_random.png") 

 
