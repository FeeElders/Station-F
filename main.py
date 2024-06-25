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
        max_trajectories = 7
        stations_csv = "StationsHolland"
        connections_csv = "ConnectiesHolland"

    railway = railway.Railway(max_trajectories, time)
    railway.load_stations(f"data/{stations_csv}.csv")
    railway.load_connections(f"data/{connections_csv}.csv")

    
 
    # --------------------Random----------------------------------
    
    # # name = random_experiment.baseline(railway, max_trajectories)
    # random_experiment.graph("nh_random_baseline")

    # # name = random_experiment.max_traject(railway, max_trajectories)
    # random_experiment.graph("nh_random_max_traject")

    # # name = random_experiment.no_visited_connections_max(railway, max_trajectories)
    # random_experiment.graph("nh_no_visited_connections")

    # # name = random_experiment.not_so_random(railway, max_trajectories)
    # random_experiment.graph("nh_not_so_random")

    # name = random_experiment.trajectory_amount(railway)
    # random_experiment.graph(name)


    # ------------------------------------Greedy------------------------------

    # greedy_experiment.greedy(railway)
    # greedy_experiment.smart_greedy(railway)


    # greedy_long = gr.GetLongestConnection(railway)
    # gr_long = greedy_long.run(20)
    # print(f"greedy score: {gr_long.score()}")



    # greedy_experiment.trajectory_amount(railway)


    # ------------------------------HillClimber-------------------------------


    # hillclimber_experiment.hillclimb(railway, max_trajectories)
    # hillclimber_experiment.hillclimb_4_2(railway, max_trajectories)
    # hillclimber_experiment.hillclimb_noreturn(railway, max_trajectories)
    # hillclimber_experiment.hillclimb_smart_start(railway, max_trajectories)
    # hillclimber_experiment.hillclimb_traject_amount(railway, max_trajectories)

    hillclimber_experiment.smart_remove(railway, max_trajectories)
    
    # random = rd.Random(railway)
    # random_railway = random.run()
    # smart_remove = hc.SmartRemove(random_railway)
    # smart_climber = smart_remove.run(1, "test_hilly_smart_remove", 1, 1)

    
    # --------------------------- Visualisation --------------------
#
#     visuals.line_graph(scoreplot, count)
#     visuals.hillclimber_graph(climber.all_scores)
#     visuals.railway_map(smart_railway, smart_railway.score(), "Smart Start Station")
#     visuals.climbing_map(climbing_railway)
