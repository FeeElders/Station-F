from code.algoritmen import hillclimber as hc
from code.algoritmen import randomise as rd
from code import helpers
from code.algoritmen.randomise import Random, NotSoRandom, NoVisitedConnections  

import pandas as pd
import matplotlib.pyplot as plt
import csv
import copy
import time
import pickle


from statistics import mean 
from datetime import datetime


def hillclimb(railway: 'Railway', traject_amount: int, delete = 1, add = 1, iterations = 100, heuristic = hc.HillClimber) -> None:
    """ Basic Hillclimber where a random trajectory is removed and a random new traject is created."""
    date = datetime.today().strftime('%d-%m-%Y')
    name = f"HillClimber_{date}"
    title = "Baseline"
    run_experiment(railway, traject_amount, name, heuristic, iterations, delete, add, title)

    
def hillclimb_4_2(railway: 'Railway', traject_amount: int, delete = 4, add = 2, iterations = 100, heuristic = hc.HillClimber) -> None:
    """ Basic hillclimber where 4 trajectories are deleted and 2 new random ones are created."""
    date = datetime.today().strftime('%d-%m-%Y')
    name = f"HillClimber-4-2_{date}"
    title = "Delete 4 add 2"
    run_experiment(railway, traject_amount, name, heuristic, iterations, delete, add, title)
    
def hillclimb_noreturn(railway, traject_amount: int, delete = 1, add = 1, iterations = 100, heuristic = hc.NoReturn) -> None:
    """ Hillclimber where connections can't be used more than once. """
    date = datetime.today().strftime('%d-%m-%Y')
    name = f"HillClimber-no_return_{date}"
    title = "No return"
    run_experiment(railway, traject_amount, name, heuristic, iterations, delete, add, title)
    

def hillclimb_smart_start(railway: 'Railway', traject_amount: int, delete = 1, add = 1, iterations = 100, heuristic = hc.SmartStart) -> None:
    """ Hillclimber with a start station that has the lowest amount of connections,
    and connections can't be used more than once.
    """
    date = datetime.today().strftime('%d-%m-%Y')
    name = f"HillClimber-smart_start_{date}"
    title = "Smart Start"
    run_experiment(railway, traject_amount, name, heuristic, iterations, delete, add, title)


def smart_remove(railway: 'Railway', traject_amount: int, delete = 1, add = 1, iterations = 100, heuristic = hc.SmartRemove) -> None:
    """ Hillclimber with a smart start station, with heuristic for smart removal of trajectories."""
    date = datetime.today().strftime('%d-%m-%Y')
    name = f"HillClimber-smart_remove_{date}"
    title = "Smart Remove"
    run_experiment(railway, traject_amount, name, heuristic, iterations, delete, add, title)
    
    
def hillclimb_traject_amount(railway: 'Railway', traject_amount: int, delete = 1, add = 1, iterations = 50, heuristic = hc.HillClimber) -> None:
    """ Run basic hillclimber N times for range of (9, 20) trajectories """    
    date = datetime.today().strftime('%d-%m-%Y')
    traject_amount = traject_amount

    if railway._max_trains == 7:
        prefix= "NH_"
        number_range = 4
    if railway._max_trains == 20:
        prefix = "NL_"
        number_range = 12
    
    for _ in range(number_range):
        title = f"Hillclimber traject amount {traject_amount}"
        name = f"{prefix}HillClimber_{traject_amount}-traject_amount_{date}"
        run_experiment(railway, traject_amount, name, heuristic, iterations, delete, add, title)
        traject_amount -= 1


def hillclimb_traject_amount_smart(railway: 'Railway', traject_amount: int, delete = 1, add = 1, iterations = 50, heuristic = hc.SmartStart) -> None:
    """ Run Smart Start Hillclimber N times for range of (9, 20) trajectories """
    date = datetime.today().strftime('%d-%m-%Y')
    traject_amount = traject_amount

    if railway._max_trains == 7:
        prefix= "NH_"
        number_range = 4
    if railway._max_trains == 20:
        prefix = "NL_"
        number_range = 12
    
    for _ in range(number_range):
        title = f"Smart Hillclimber traject amount {traject_amount}"
        name = f"{prefix}SmartStartHillClimber_{traject_amount}-traject_amount_{date}"
        run_experiment(railway, traject_amount, name, heuristic, iterations, delete, add, title)
        traject_amount -= 1
        
     
def run_experiment(railway: 'Railway', traject_amount: int, name: str, heuristic: 'HillClimber', iterations: int, delete: int, add: int, title: str) -> None:
    """ Run Hillclimber algorithm N times

    args:
    railway: the railway to start with
    traject_amount (int): the amount of trajectories to use
    name (str): the name of the file
    heuristic ('HillClimber'): the hillclimber heuristic/inherited class
    iterations (int): the number of iterations to execute hillclimber
    delete (int): the number of trajectories to delete each iteration
    add (int): the number of trajectories to add each iteration
    title (str): the title for the graph

    side effects:
    One CSV file is created for every run
    One CSV file is created for all the end scores and its run ID
    One CSV file is created for formatted output of the best railway found
    One barchart is saved for the end scores
    One line chart is made for the runs mean climb
    One railway map is saved for the visualisation of the best railway found
    """  
    
    run_count = 0
    best_climbing_railway: 'Railway' = None
    
    with open(f'output/hillclimber/{name}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['run_count','end_score'])
        
    while run_count < iterations:

        random = rd.Random(railway)
        random_railway = random.run(traject_amount)
        
        
        # create a new file
        with open(f'output/hillclimber/{name}_run_{run_count}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['iteration','score'])
            
        start = time.time()        
        print("Setting up Hill Climber...")
        climber = heuristic(random_railway)

        print("Running Hill Climber...")
        climbing_railway = climber.run(run_count, name, delete, add, active=True)

        print(f"Value of the configuration after Hill Climber: "
              f"{climbing_railway.score()}")
        end = time.time()
        running_time = end - start      
         
        # Add end score to csv        
        with open(f'output/hillclimber/{name}.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([run_count, climbing_railway.score()])
            
        if helpers.best_score(climbing_railway, best_climbing_railway):
            best_climbing_railway = copy.copy(climbing_railway)
            best_climbing_railway.formatted_output(f"hillclimber/best_formatted_output_{name}.csv", running_time) 
            helpers.object_output(climbing_railway, f"hillclimber/{name}")       
                
        run_count += 1         
    # Functions to create plots

    railway_map(f"hillclimber/{name}", title)
    counts = hist_graph(name, title)
    line_graph_average(counts, title, name)
    greedy_over_hill(name, title, 6592)
       
def line_graph_average(counts, title, name):  
    """ Plot the average, minimum and maximum scores in a line graph """
    colors = ["black", "deeppink", "plum", "olive", "orange", "grey", "firebrick", "darksalmon", "lightgrey", "gold", "deepskyblue", "chartreuse", "green", "teal",  "blue", "indigo", "greenyellow", "crimson", "lemonchiffon", "darkmagenta", "azure", "bisque"]
    plt.title(f'Hill Climber algoritme {title}')
    plt.xlabel('Iteraties')
    plt.ylabel('Score')
    
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
    plt.fill_between(x = iteration, y1 = minimum, y2 = maximum, color="lightgrey")    
        

    # plt.show()
    plt.savefig(f"output/hillclimber/average_line_{name}_{title}.png")      
    plt.close()
        
def hist_graph(name, title):
    """ Plot the end scores of every run in a bar chart """
    df = pd.read_csv(f'output/hillclimber/{name}.csv', delimiter=',')   

    run_count = df["run_count"]
    end_score = df["end_score"]
    
    count = len(df["end_score"])
    n_bins = 20
    plt.hist(end_score, bins=n_bins)

    plt.xlim(0, 8000)

    plt.xlabel('Score (K)')
    plt.ylabel('Frequentie')
    plt.title(f'Hill Climber {title}, {n_bins} bins {count} keer')

    # plt.show()

    plt.savefig(f"output/hillclimber/histogram_{name}.png")
    plt.close()
    
    return count
    
def greedy_over_hill(name, title, score):
    """ Plot the scores of the hillclimber with the greedy as subplot in a bar chart """   
    df = pd.read_csv(f'output/hillclimber/{name}.csv', delimiter=',')   

    run_count = df["run_count"]
    end_score = df["end_score"]
    
    count = len(df["end_score"])
    n_bins = 20
    plt.hist(end_score, bins=n_bins)
    plt.axvline(score, color='k', linestyle='dashed', linewidth=1)

    plt.xlim(0, 8000)
    plt.xlabel('Score (K)')
    plt.ylabel('Frequentie')
    plt.title(f'{title}, {n_bins} bins {count} keer')

    # plt.show()

    plt.savefig(f"output/hillclimber/overlay_{title}.png")
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
    plt.savefig(f"output/hillclimber/visual_{title}_Hillclimber.png") 
    plt.close()
     

    

    
        
        
