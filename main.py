import time
import csv
from csv import writer
import copy

from code import helpers
from code.classes import station, railway, connection, trajectory
from code.visualisation import visuals 
from code.algoritmen  import randomise as rd
from code.algoritmen  import hillclimber as hc
from code.algoritmen import greedy as gr

from experimenten import random_experiment
from experimenten import hillclimber_experiment
from experimenten import greedy_experiment
from datetime import datetime

if __name__ == "__main__":
    print("WELCOME TO RailNL")
    
    data = "nl"
    
    if data == "nl":
        time = 180
        max_trajectories = 20
        stations_csv = "StationsNationaal"
        connections_csv = "ConnectiesNationaal"
        
    elif data == "nh":
        time = 120
        trajectories = 7
        stations_csv = "StationsHolland"
        connections_csv = "ConnectiesHolland"

    railway = railway.Railway(max_trajectories, time)
    railway.load_stations(f"data/{stations_csv}.csv")
    railway.load_connections(f"data/{connections_csv}.csv")

    
 
    # --------------------Random----------------------------------
    
    # name = random_experiment.baseline(railway)
    # random_experiment.graph("random_baseline")

    # name = random_experiment.max_traject(railway, max_trajectories)
    # random_experiment.graph("random_max_traject")

    # name = random_experiment.no_visited_connections(railway, max_trajectories)
    # random_experiment.graph("no_visited_connections")

    # name = random_experiment.not_so_random(railway, max_trajectories)
    # random_experiment.graph("not_so_random")




    # ------------------------------------Greedy------------------------------

    # greedy = gr.Greedy(railway)
#     greedy_railway = greedy.run(20)
#     print(f"greedy score: {greedy_railway.score()}")
#
#     smart_greedy = gr.SmartStartStation(railway)
#     smart_railway = smart_greedy.run(20)
#     print(f"greedy score: {smart_railway.score()}")
#
#     #name = greedy_experiment.greedy(railway)
#     name = greedy_experiment.smart_greedy(railway)
    #visuals.railway_map(smart_railway, smart_railway.score(), "Smart Start Station")
    # greedy_long = gr.GetLongestConnection(railway)
    # gr_long = greedy_long.run(20)
    # print(f"greedy score: {gr_long.score()}")


    # ------------------------------HillClimber-------------------------------
    delete = 1
    add = 1
    name = "test"
    greedy = gr.SmartStartStation(railway)
    greedy_railway = greedy.run(15)
    climber = hc.SmartStart(greedy_railway)

    print("Running Hill Climber...")
    climbing_railway = climber.run(1, name, delete, add, active=True)

    print(f"Value of the configuration after Hill Climber: "
          f"{climber.railway.score()}")

    # naam = hillclimber_experiment.hillclimb(railway)
    # naam = hillclimber_experiment.hillclimb_4_2(railway)
    # naam = hillclimber_experiment.hillclimb_noreturn(railway)


    # count = hillclimber_experiment.hist_graph(name)
    # hillclimber_experiment.line_graph(count, "random 1 traject", name)

    
    # --------------------------- Visualisation --------------------
#
#     visuals.line_graph(scoreplot, count)
#     visuals.hillclimber_graph(climber.all_scores)
#     visuals.railway_map(smart_railway, smart_railway.score(), "Smart Start Station")
#     visuals.climbing_map(climbing_railway)
