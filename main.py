import time
import csv
from csv import writer
import copy
import sys, argparse, getopt

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
    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional argument
    parser.add_argument("-m", "--map", default = "nl", choices = ["nl", "nh"], help = "choose which data you want to use")
    parser.add_argument("-a", "--algoritme", default = "random", choices = ["Random", "Greedy", "HillClimber"], help = "Choose algorithm")
    parser.add_argument("-ex", "--experiment", default = "bs", help = "Do Trajectory Amount Experiment")

    # Read arguments from command line
    args = parser.parse_args()

    if args.map == "nl":
        time = 180
        max_trajectories = 20
        stations_csv = "StationsNationaal"
        connections_csv = "ConnectiesNationaal"

    if args.map == "nh":
        time = 120
        max_trajectories = 7
        stations_csv = "StationsHolland"
        connections_csv = "ConnectiesHolland"        
    
    railway = railway.Railway(max_trajectories, time)
    railway.load_stations(f"data/{stations_csv}.csv")
    railway.load_connections(f"data/{connections_csv}.csv")


    # initialize dicionary with all experiments
    random_dict{"baseline": "random_experiment.baseline",
                "max_traject": "random_experiment.max_traject",
                "nvc_max": "random_experiment.no_visited_connections_max",
                "nvc_random": "random_experiment.no_visited_connections_random",
                "not_so_random": "random_experiment.not_so_random"}
                
    

    print("WELCOME TO RailNL")
    
    if args.algoritme:
        print(f"Running {args.algoritme} algorithm.")
        if args.algoritme == "random" and args.experiment == "bs":
            random_dict["baseline"](railway)
            
    
      
