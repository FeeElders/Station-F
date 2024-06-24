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
   


 
