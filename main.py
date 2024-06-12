from code.classes import station, railway, connection, trajectory
from code.visualisation import visuals 
from code.algoritmen  import randomise as rd

if __name__ == "__main__":
    print("WELCOME TO RailNL")

    railway = railway.Railway(20, 180)
    best_railway: dict[int: 'Railway'] = {}

    railway.load_stations("data/StationsNationaal.csv")
    railway.load_connections("data/ConnectiesNationaal.csv")


    # --------------------Random----------------------------------
    count = 0
    scoreplot = {}
    



    while count <= 10:
        random = rd.Random(railway)
        random_railway = random.run()
        scoreplot[count]= random_railway.score()
        
        # check if railway score is higher than previous and save this railway
        best_railway = random.best_score(random_railway) 
        count += 1
        
    
        
   # --------------------Hill climber------------------------------
   
        Hill(best_railway)
   # --------------------------- Visualisation --------------------
    # visuals.line_graph(scoreplot)
    
    visuals.railway_map(random_railway)



