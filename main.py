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


    while count <= 2:
        random = rd.Random(railway)
        random_railway = random.run()
        scoreplot[count]= random_railway.score()
        count += 1

   # --------------------------- Visualisation --------------------
    visuals.line_graph(scoreplot)
    
#    visuals.railway_map("data/StationsNationaal.csv", "data/ConnectiesNationaal.csv", random_railway)



