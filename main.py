import time
import csv
from csv import writer
import copy
import sys, argparse, getopt

from code import helpers
from code.classes import station, railway, connection, trajectory
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

    # Add arguments
    parser.add_argument("-k", "--kaart", default = "nl", choices = ["nl", "nh"], help = "choose which data you want to use")
    parser.add_argument("-a", "--algoritme", default = "random", choices = ["random", "greedy", "hillclimber"], help = "Choose algorithm")
    parser.add_argument("-ex", "--experiment", default = "bs", help = "Choose experiment")

    # Read arguments from command line
    args = parser.parse_args()

    # set the scene for whole Netherlands
    if args.kaart == "nl":
        time = 180
        max_trajectories = 20
        stations_csv = "StationsNationaal"
        connections_csv = "ConnectiesNationaal"

    # set the scene for Holland
    if args.kaart == "nh":
        time = 120
        max_trajectories = 7
        stations_csv = "StationsHolland"
        connections_csv = "ConnectiesHolland"        
    
    railway = railway.Railway(max_trajectories, time)
    railway.load_stations(f"data/{stations_csv}.csv")
    railway.load_connections(f"data/{connections_csv}.csv")


    # initialize dicionaries with command line arguments and corresponding experiment functions
    random_dict = {"bs": random_experiment.baseline,
                   "mt": random_experiment.max_traject,
                   "nvc_max": random_experiment.no_visited_connections_max,
                   "nvc_random": random_experiment.no_visited_connections_random,
                   "nsr": random_experiment.not_so_random,
                   "tr": [random_experiment.trajectory_amount, random_experiment.notsorandom_trajectory_amount]}

    greedy_dict = {"bs": greedy_experiment.greedy, 
                   "smart": greedy_experiment.smart_greedy,
                   "rd_greedy": greedy_experiment.random_greedy,
                   "tr": [greedy_experiment.trajectory_amount, greedy_experiment.smart_trajectory_amount]}
        

    hillclimber_dict = {"bs": hillclimber_experiment.hillclimb,
                        "4_2": hillclimber_experiment.hillclimb_4_2,
                        "nr": hillclimber_experiment.hillclimb_noreturn,
                        "smart_s": hillclimber_experiment.hillclimb_smart_start,
                        "smart_r": hillclimber_experiment.smart_remove,
                        "tr": [hillclimber_experiment.hillclimb_traject_amount, hillclimber_experiment.hillclimb_traject_amount_smart]}


    print("WELCOME TO RailNL")
    
    if args.algoritme:
        print(f"You chose the {args.algoritme} algorithm!")

        # ----------------------------------Random------------------------------
        if args.algoritme == "random":
            if args.experiment == "bs" or args.experiment == "nvc_random":
                random_dict[args.experiment](railway)
            elif args.experiment == "tr":
                random_dict[args.experiment][0](railway, max_trajectories)
                random_dict[args.experiment][1](railway, max_trajectories)
            else:
                random_dict[args.experiment](railway, 13)


        # -----------------------------------Greedy-----------------------------
        if args.algoritme == "greedy":
            if args.experiment == "smart":
                greedy_dict[args.experiment](railway, 17)
            elif args.experiment == "tr":
                greedy_dict[args.experiment][0](railway, max_trajectories)
                greedy_dict[args.experiment][1](railway, max_trajectories)
            else:
                greedy_dict[args.experiment](railway, 19)


        # ---------------------------------HillClimber--------------------------
        if args.algoritme == "hillclimber":
            if args.experiment == "tr":
                hillclimber_dict[args.experiment][0](railway, max_trajectories)
                hillclimber_dict[args.experiment][1](railway, max_trajectories)
            elif args.experiment == "4_2":
                hillclimber_dict[args.experiment](railway, max_trajectories)
            else:
                hillclimber_dict[args.experiment](railway, 11)
