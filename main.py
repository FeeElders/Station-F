import time
import csv
from csv import writer
import copy

from code import helpers
from code.classes import station, railway, connection, trajectory
from code.visualisation import visuals 
from code.algoritmen  import randomise as rd
from code.algoritmen  import hillclimber as hc

#from experimenten import hillclimber_experiment


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

    while count < 1:
        random = rd.Random(railway)
        random_railway = random.run(20)

        if helpers.best_score(random_railway, best_random_railway):
            best_random_railway = copy.copy(random_railway)
            best_random_railway.formatted_output("best_random_railway.csv")
        scoreplot[count]= random_railway.score()
        csv_scores.append(random_railway.score())
        count += 1  
        if count%interval == 0:
            # sla elke +-10 minuten de scores op in een bestand
            helpers.append_to_csv(name, csv_scores)

    # print("random railway in the making")
 #    random = rd.Random(railway)
 #    random_railway = random.run(20)
 #    print(f"print random trajectories")
 #    random_railway.formatted_output("random_railway.csv")
 #
 #
 #    # ---------------------------NoVisitedConnections----------------------------
 #    print("no visited connections railway in the making")
 #    nvc_random = rd.NoVisitedConnections(railway)
 #    random_railway2 = nvc_random.run(20)
 #    random_railway2.formatted_output("no_visited_connections.csv")
 #
 #
 #    # -------------------------------NotSoRandom-----------------------
 #    print(f"not so random trajectories in the making\n")
 #    ns_random = rd.NotSoRandom(railway)
 #    random_railway3 = ns_random.run(4)
    
    
    # --------------------------- Hill Climber ---------------------------------
    iterations = 300
    helpers.create_csv(f"hillyscores{iterations}")
    start = time.time()
    print("Setting up Hill Climber...")
    climber = hc.HillClimber(random_railway)

    print("Running Hill Climber...")
    climbing_railway = climber.run(iterations, active=True)

    print(f"Value of the configuration after Hill Climber: "
          f"{climber.railway.score()}")
          
    end = time.time()
    time = end - start    
    
    # hillclimber_experiment.hillclimb(test_graph, transmitters)
    # hillclimber_experiment.hillclimb_continue(test_graph, transmitters, "output/hillclimber/hillclimber.csv")
    # hillclimber_experiment.hillclimb_graph()

    # hillclimber_experiment.hillclimber_averages(test_graph, transmitters)
    # hillclimber_experiment.hillclimber_averages_graph()
    # hillclimber_experiment.hillclimber_averages_filled_graph()

    # hillclimber_experiment.hillclimber_xopt_comparison(test_graph, transmitters)
    # hillclimber_experiment.hillclimber_xopt_comparison_graph()  
    
    # --------------------------- Visualisation --------------------

    # visuals.line_graph(scoreplot, count)
    visuals.hillclimber_graph(climber.all_scores)
    visuals.railway_map(climbing_railway, climber.railway.score(), "Hill Climber")
    # visuals.climbing_map(climbing_railway)
    
    csv_scores_climber = list(climber.all_scores.values())
    climber.railway.formatted_output(f"hilly{iterations}.csv")
    helpers.append_to_csv(f"hillyscores{iterations}", csv_scores_climber, time)




