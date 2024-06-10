from code.classes import station, railway, connection, trajectory
from code.visualisation import visuals 
from code.algoritmen  import randomise as rd

if __name__ == "__main__":
    print("WELCOME TO RailNL")

    railway = railway.Railway()

    railway.load_stations("data/StationsHolland.csv")
    railway.load_connections("data/ConnectiesHolland.csv")


    # --------------------Random----------------------------------
    count = 0
    scoreplot = {}
    

    while count <= 10000:
        random_railway = rd.Random(railway)
        rd_railway = random_railway.run()
        
        scoreplot[count]= rd_railway.score()
        count += 1
   

    # --------------------------- Visualisation --------------------------------
    visuals.visualise(scoreplot)
