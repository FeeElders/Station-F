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
    
    # # name = random_experiment.baseline(railway)
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

    # # name = greedy_experiment.greedy(railway)
    # greedy_experiment.graph("nh_Greedy_22-06-2024")



    # name = greedy_experiment.smart_greedy(railway)
    # greedy_experiment.graph("nh_SmartGreedy_22-06-2024")


    # greedy_long = gr.GetLongestConnection(railway)
    # gr_long = greedy_long.run(20)
    # print(f"greedy score: {gr_long.score()}")


    # rd_greedy = gr.RandomGreedy(railway)
    # rand_gr_railway = rd_greedy.run(20)
    # print(f"randomgreedy score: {rand_gr_railway.score()}")

    greedy_experiment.trajectory_amount(railway)

    # ------------------------------HillClimber-------------------------------


    # naam = hillclimber_experiment.hillclimb(railway)
    # # naam = hillclimber_experiment.hillclimb_4_2(railway)
    # # hillclimber_experiment.hillclimb_noreturn(railway)
    # hillclimber_experiment.hillclimb_smart_start(railway)


    # count = hillclimber_experiment.hist_graph(name)
    # hillclimber_experiment.line_graph(count, "random 1 traject", name)
    # hillclimber_experiment.railway_map("climber_0")
    
    # count = hillclimber_experiment.hist_graph("nh_HillClimber_23-06-2024")
    # hillclimber_experiment.line_graph(20, "Noord Holland Basic Climber", "nh_HillClimber_23-06-2024")

    # smart_climber = hc.SmartRemove(railway)
    # climber_railway = smart_climber.run(1, "test_smart_climber", 1, 1)
    
    
    # --------------------------- Visualisation --------------------
#
#     visuals.line_graph(scoreplot, count)
#     visuals.hillclimber_graph(climber.all_scores)
#     visuals.railway_map(smart_railway, smart_railway.score(), "Smart Start Station")
#     visuals.climbing_map(climbing_railway)
