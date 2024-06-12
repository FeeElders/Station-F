import pickle
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


    best_railway: 'Railway' = None

    # --------------------Random----------------------------------
    count = 0
    scoreplot = {}

    test_copies = []


    while count <= 10000:
        random = rd.Random(railway)
        random_railway = random.run()
        # if helpers.best_score(random_railway, best_railway):
        #    best_railway = copy.copy(random_railway)
        #test_copies.append(random_railway)
        scoreplot[count]= random_railway.score()
        count += 1

    # for railway in test_copies:
    #     railway.print_trajectories()

        
    with open('best_random_railway.obj', 'wb') as file:
        pickle.dump(random_railway, file)

   # --------------------------- Visualisation --------------------
    visuals.line_graph(scoreplot)
    
#    visuals.railway_map("data/StationsNationaal.csv", "data/ConnectiesNationaal.csv", random_railway)



