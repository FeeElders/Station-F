from code.classes import station, railway, connection, trajectory
from code.visualisation import visuals 
from code.algoritmen  import randomise

if __name__ == "__main__":
    print("WELCOME TO RailNL")

    railway = railway.Railway()
    railway.load_stations()
    railway.load_connections()
    

    # --------------------Random----------------------------------
    count = 0
    scoreplot = {}
    

    while count <= 10000:
        random_railway = randomise.random(railway)
        
        
        scoreplot[count]= random_railway.score()
        count += 1
   

    # --------------------------- Visualisation --------------------------------
    visuals.visualise(scoreplot)