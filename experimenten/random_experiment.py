from code.algoritmen import randomise as rd
from code import helpers
from code.visualisation import visuals 

import matplotlib.pyplot as plt
import csv
import copy
from statistics import mean 


def baseline(railway):
    count = 0
    scoreplot:dict[int:int] = {}
    csv_scores:list[int]= []
    best_random_railway: 'Railway' = None
    name = "random_baseline"
    interval = 20
    helpers.create_csv(name)

    while count < 100:
      random = rd.Random(railway)
      random_railway = random.run()

      if helpers.best_score(random_railway, best_random_railway):
          best_random_railway = copy.copy(random_railway)
          best_random_railway.formatted_output("best_random_railway.csv")
      scoreplot[count]= random_railway.score()
      csv_scores.append(random_railway.score())
      count += 1  
    visuals.line_graph(scoreplot, count, name)

      
def max_traject(railway, max_trajectories):
    count = 0
    scoreplot:dict[int:int] = {}
    csv_scores:list[int]= []
    best_random_railway: 'Railway' = None
    name = "random_max_traject"
    interval = 20
    helpers.create_csv(name)

    while count < 100:
        random = rd.Random(railway)
        random_railway = random.run(max_trajectories)

        if helpers.best_score(random_railway, best_random_railway):
            best_random_railway = copy.copy(random_railway)
            best_random_railway.formatted_output("best_random_railway.csv")
        scoreplot[count]= random_railway.score()
        csv_scores.append(random_railway.score())
        count += 1  
        # if count%interval == 0:
#             # sla elke +-10 minuten de scores op in een bestand
#             helpers.append_to_csv(name, csv_scores)
    visuals.line_graph(scoreplot, count, name)
    
            
def no_visited_connections(railway, max_trajectories):
    """
    Also with max traject
    """
    count = 0
    scoreplot:dict[int:int] = {}
    csv_scores:list[int]= []
    best_random_railway: 'Railway' = None
    name = "no_visited_connections"
    interval = 20
    helpers.create_csv(name)

    while count < 100:
        nvc_random = rd.NoVisitedConnections(railway)
        random_railway2 = nvc_random.run(max_trajectories)

        if helpers.best_score(random_railway2, best_random_railway):
            best_random_railway = copy.copy(random_railway2)
            best_random_railway.formatted_output("best_random_railway.csv")
        scoreplot[count]= random_railway2.score()
        csv_scores.append(random_railway2.score())
        count += 1  
        # if count%interval == 0:
#             # sla elke +-10 minuten de scores op in een bestand
#             helpers.append_to_csv(name, csv_scores)
    
    visuals.line_graph(scoreplot, count, name)
    
def not_so_random(railway, max_trajectories):
    """
    Gestuurde start staion en gestuurde connection
    
    begin station dat nog niet is geweest en een verbinding die nog niet is geweest. beide tenzij het niet anders kan
    """
    count = 0
    scoreplot:dict[int:int] = {}
    csv_scores:list[int]= []
    best_random_railway: 'Railway' = None
    name = "not_so_random"
    interval = 20
    helpers.create_csv(name)
    
    print(f"not so random trajectories in the making\n")
    while count < 100:
        ns_random = rd.NotSoRandom(railway)
        random_railway3 = ns_random.run(max_trajectories)

        if helpers.best_score(random_railway3, best_random_railway):
            best_random_railway = copy.copy(random_railway3)
            best_random_railway.formatted_output("best_random_railway.csv")
        scoreplot[count]= random_railway3.score()
        csv_scores.append(random_railway3.score())
        count += 1  
        # if count%interval == 0:
#             # sla elke +-10 minuten de scores op in een bestand
#             helpers.append_to_csv(name, csv_scores)
            
    visuals.line_graph(scoreplot, count, name)
    
   


 