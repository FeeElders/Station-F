import time
import csv
from csv import writer
import copy

from code import helpers
from code.classes import station, railway, connection, trajectory
from code.visualisation import visuals 
from code.algoritmen  import randomise as rd
from code.algoritmen  import hillclimber as hc

from experimenten import random_experiment


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
    
    random_experiment.baseline(railway)
    random_experiment.max_traject(railway, max_trajectories)
    random_experiment.no_visited_connections(railway, max_trajectories)
    random_experiment.not_so_random(railway, max_trajectories)
   
      
    # # --------------------------- Hill Climber ---------------------------------
#     iterations = 300
#     helpers.create_csv(f"hillyscores{iterations}")
#     # start = time.time()
#     print("Setting up Hill Climber...")
#     climber = hc.HillClimber(random_railway)
#
#     print("Running Hill Climber...")
#     climbing_railway = climber.run(iterations, active=True)
#
#     print(f"Value of the configuration after Hill Climber: "
#           f"{climber.railway.score()}")
#
#     # end = time.time()
# #     time = end - start
#
#     # hillclimber_experiment.hillclimb(test_graph, transmitters)
#     # hillclimber_experiment.hillclimb_continue(test_graph, transmitters, "output/hillclimber/hillclimber.csv")
#     # hillclimber_experiment.hillclimb_graph()
#
#     # hillclimber_experiment.hillclimber_averages(test_graph, transmitters)
#     # hillclimber_experiment.hillclimber_averages_graph()
#     # hillclimber_experiment.hillclimber_averages_filled_graph()
#
#     # hillclimber_experiment.hillclimber_xopt_comparison(test_graph, transmitters)
#     # hillclimber_experiment.hillclimber_xopt_comparison_graph()
#
#     # --------------------------- Visualisation --------------------
#
#  #   visuals.line_graph(scoreplot, count)
#     visuals.hillclimber_graph(climber.all_scores)
#     visuals.railway_map(climbing_railway, climber.railway.score(), "Hill Climber")
#     # visuals.climbing_map(climbing_railway)
#
#     csv_scores_climber = list(climber.all_scores.values())
#     climber.railway.formatted_output(f"hilly{iterations}.csv")
#     helpers.append_to_csv(f"hillyscores{iterations}", csv_scores_climber, time)




