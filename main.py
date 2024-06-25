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
    
    random_experiment.trajectory_amount(railway, max_trajectories)
    # random_experiment.baseline(railway, max_trajectories)
#     random_experiment.max_traject(railway, max_trajectories)
#     random_experiment.no_visited_connections_max(railway, max_trajectories)
#     random_experiment.not_so_random(railway, max_trajectories)
    
    


    # ------------------------------------Greedy------------------------------
    # greedy_experiment.trajectory_amount(railway, max_trajectories)
    # greedy_experiment.greedy(railway, max_trajectories)
    # greedy_experiment.smart_greedy(railway, max_trajectories)
    # greedy_experiment.random_greedy(railway, max_trajectories)
    
    # ------------------------------HillClimber-------------------------------

    # hillclimber_experiment.hillclimb_traject_amount(railway, max_trajectories)
    # hillclimber_experiment.hillclimb(railway, max_trajectories)
    # hillclimber_experiment.hillclimb_4_2(railway, max_trajectories)
    # hillclimber_experiment.hillclimb_noreturn(railway, max_trajectories)
    # hillclimber_experiment.hillclimb_smart_start(railway, max_trajectories)
    # hillclimber_experiment.smart_remove(railway, max_trajectories)
    
    
    # --------------------------- Visualisation --------------------
#
#     visuals.line_graph(scoreplot, count)
#     visuals.hillclimber_graph(climber.all_scores)
#     visuals.railway_map(smart_railway, smart_railway.score(), "Smart Start Station")
#     visuals.climbing_map(climbing_railway)
