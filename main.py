import time
import csv
from csv import writer
import copy

from code import helpers
from code.classes import station, railway, connection, trajectory
from code.visualisation import visuals 
from code.algoritmen  import randomise as rd

if __name__ == "__main__":
    print("WELCOME TO RailNL")

    railway = railway.Railway(20, 180)
    railway.load_stations("data/StationsNationaal.csv")
    railway.load_connections("data/ConnectiesNationaal.csv")

    # --------------------Random----------------------------------
    count = 0
    scoreplot:dict[int:int] = {}
    csv_scores:list[int]= []
    best_random_railway: 'Railway' = None
    name = "scores"
    interval = 20
    helpers.create_csv(name)

    while count < 40:
        random = rd.Random(railway)
        random_railway = random.run(20)

        if helpers.best_score(random_railway, best_random_railway):
            best_random_railway = copy.copy(random_railway)
            best_random_railway.formatted_output("best_random_railway.csv")
        scoreplot[count]= random_railway.score()
        csv_scores.append(random_railway.score())
        count += 1  
        helpers.append_to_csv(name, interval, count, csv_scores)      
 

    # --------------------Hill climber------------------------------
   
 #   climber = HillClimber(random_railway)
   

    # --------------------------- Visualisation --------------------
    #visuals.line_graph(scoreplot, iterations)
    visuals.railway_map(best_random_railway)




