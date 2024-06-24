from code.algoritmen import hillclimber as hc
from code.algoritmen import randomise as rd
from code import helpers
from code.visualisation import visuals 
from code.algoritmen.randomise import Random, NotSoRandom, NoVisitedConnections  

import pandas as pd
import matplotlib.pyplot as plt
import csv
import copy
import time
import pickle


from statistics import mean 
from datetime import datetime


def hillclimb(railway, traject_amount = 20, delete = 1, add = 1, iterations = 20, heuristic = hc.HillClimber):
    """
    Random hillclimber where a random traject is removed and a random new traject is made
    
    20 trajectories to start with and connections can be traveled multiple times
    """
    date = datetime.today().strftime('%d-%m-%Y')
    name = f"HillClimber_{date}"
    title = "Baseline"
    run_experiment(railway, traject_amount, name, heuristic, iterations, delete, add, title)

    
def hillclimb_4_2(railway, traject_amount = 20, delete = 4, add = 2, iterations = 20, heuristic = hc.HillClimber):
    """
    Experiment where 4 trajects are deleted and then 2 new ones are created
    
    20 trajectories to start with and connections can be traveled multiple times
    """
    date = datetime.today().strftime('%d-%m-%Y')
    name = f"HillClimber-4-2_{date}"
    title = "Delete 4 add 2"
    run_experiment(railway, traject_amount, name, heuristic, iterations, delete, add, title)
    
def hillclimb_noreturn(railway, traject_amount = 20, delete = 1, add = 1, iterations = 20, heuristic = hc.NoReturn):

    date = datetime.today().strftime('%d-%m-%Y')
    name = f"HillClimber-no_return_{date}"
    title = "No return"
    run_experiment(railway, traject_amount, name, heuristic, iterations, delete, add, title)
    
    

def hillclimb_smart_start(railway, traject_amount = 20, delete = 1, add = 1, iterations = 20, heuristic = hc.SmartStart):

    """
    Experiment where a start station is chosen where the possible connections is te lowest.
    
    New trajects can't do the connection twice, we start with 20 trajectories. 
    1 trajectory is replaced by one where connections can't be traveled twice
    and have a smart start staion
    """    
    date = datetime.today().strftime('%d-%m-%Y')
    name = f"HillClimber-smart_start_{date}"
    title = "Smart Start"
    run_experiment(railway, traject_amount, name, heuristic, iterations, delete, add, title)
    
def hillclimb_traject_amount(railway, traject_amount=20, delete = 1, add = 1, iterations = 20, heuristic = hc.HillClimber):
    """
    Experiment where a start station is chosen where the possible connections is te lowest.
    
    New trajects can't do the connection twice, we start with 20 trajectories. 
    1 trajectory is replaced by one where connections can't be traveled twice
    and have a smart start staion
    """    
    
    date = datetime.today().strftime('%d-%m-%Y')
    name = f"HillClimber-traject_amount_{date}"
    
    for _ in range(10):
        title = f"traject amount {traject_amount}"
        run_experiment(railway, traject_amount, name, heuristic, iterations, delete, add, title)
        traject_amount -= 1
    
        
    
def run_experiment(railway, traject_amount: int, name: str, heuristic, iterations: int, delete: int, add: int, title: str) -> None:
    """ Arg: Heuristic is a class from algorithms """  
    
    run_count = 0

    
    with open(f'output/hillclimber/{name}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['run_count','end_score'])
        
    while run_count < iterations:

        random = rd.Random(railway)
        random_railway = random.run(traject_amount)
        start = time.time()
        
        # create a new file
        with open(f'output/hillclimber/{name}_run_{run_count}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['iteration','score'])
                
        print("Setting up Hill Climber...")
        climber = heuristic(random_railway)

        print("Running Hill Climber...")
        climbing_railway = climber.run(run_count, name, delete, add, active=False)

        print(f"Value of the configuration after Hill Climber: "
              f"{climbing_railway.score()}")
        end = time.time()
        running_time = end - start      
         
        # Add end score to csv        
        with open(f'output/hillclimber/{name}.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([run_count, climber.railway.score()])

        climbing_railway.formatted_output(f"hillclimber/formatted_output_{name}_{run_count}.csv", running_time)    
        
        run_count += 1    
        
    # Functions to create plots
    climber.railway.formatted_output(f"hillclimber/formatted_output_{name}.csv", running_time)
    helpers.object_output(climber.railway, f"hillclimber/{name}")       
    railway_map(f"hillclimber/{name}", title)
    counts = hist_graph(name)
    line_graph(counts, title, name)
       
def line_graph(counts, title, name):  
    """
    Plotten van de score vs de iteraties in een histogram
    y as komt de score en op de x as het aantal pogingen
    """
    colors = ["black", "deeppink", "plum", "olive", "orange", "grey", "firebrick", "darksalmon", "lightgrey", "gold", "deepskyblue", "chartreuse", "green", "teal",  "blue", "indigo", "greenyellow", "crimson", "lemonchiffon", "darkmagenta", "azure", "bisque"]
    fig, ax = plt.subplots()
    ax.set_title(f'Hill Climber algoritme {title}')
    ax.set_xlabel('Iteraties')
    ax.set_ylabel('Score')
    
    minimum = []
    maximum = []
    total = []
    amount = []
    average = []
    iteration = []
    
    for run_count in range(counts):
        df = pd.read_csv(f'output/hillclimber/{name}_run_{run_count}.csv', delimiter=',')
        for i in df["iteration"]:
            if len(maximum)-1 < i:
                 maximum.append(df["score"][i])
            elif maximum[i] < df["score"][i]:
                maximum[i]=  df["score"][i]       
                
            if len(minimum)-1 < i:
                 minimum.append(df["score"][i])                
            elif minimum[i] > df["score"][i]:
                minimum[i]=  df["score"][i]
            
            if len(total)-1 < i:
                total.append(df["score"][i])
            else:
                total[i] = total[i] + df["score"][i]
            
            if len(amount)-1 < i:
                amount.append(1)
            else:
                amount[i] += 1
                
                
    for i in range(len(total)):
        average_value = total[i]/amount[i]  
        average.append(average_value)   
        iteration.append(i)       
           
      
    plt.plot(iteration, average, color="red", linestyle="-")
    ax.fill_between(x = iteration, y1 = minimum, y2 = maximum, color="lightgrey")    
        

    plt.show()
    fig.savefig(f"output/hillclimber/average_line_{name}_{title}.png")      
        
def hist_graph(name):
    """
    Plotten van de scores per algoritme in een hisogram
    y as komt het aantal pogingen en op de x as de score
    """
    
    fig, axs = plt.subplots()
    df = pd.read_csv(f'output/hillclimber/{name}.csv', delimiter=',')   

    run_count = df["run_count"]
    end_score = df["end_score"]
    
    print(end_score)

    count = len(df["end_score"])
    print(count)
    n_bins = 5

    axs.hist(end_score, bins=n_bins)

    axs.set_xlim(0, 8000)
   
    axs.set(xlabel='Score (K)', ylabel='Frequentie',
              title=f'Hill Climber {n_bins} bins {count} keer')
    plt.show()
    fig.savefig(f"output/hillclimber/histogram_{name}.png")
    
    return count
    

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
    plt.title(f'Hill climber {title} met een score van: {score}')
    

    plt.show()
    plt.savefig(f"output/hillclimber/visual_{title}_Hillclimber.png") 
     

    

    
        
        
