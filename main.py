import time
import csv
from csv import writer
from code import helpers
from code.classes import station, railway, connection, trajectory
from code.visualisation import visuals 
from code.algoritmen  import randomise as rd

if __name__ == "__main__":
    print("WELCOME TO RailNL")

    railway = railway.Railway(20, 180)
    railway.load_stations("data/StationsNationaal.csv")
    railway.load_connections("data/ConnectiesNationaal.csv")

    # --------------------Random----------------------------------
    count = 0
    scoreplot:dict[int:int] = {}
    csv_scores:list[int]= []
    
    start = time.time()
    # with open('scores.csv', 'w', newline='') as file:
#         writer = csv.writer(file)

    while time.time() - start < 3600:
        random = rd.Random(railway)
        random_railway = random.run()
        scoreplot[count]= random_railway.score()
        csv_scores.append(random_railway.score())
        count += 1
        
        
    with open('scores.csv', 'a', newline='') as file:
        writer_new = csv.writer(file)
        for score in csv_scores:
            writer_new.writerow(score)
        print("opgeslagen")

    while True:
        # sla elke 10 minuten de scores op in een bestand
        time.sleep(600)
        
   # --------------------Hill climber------------------------------
   



   # --------------------------- Visualisation --------------------
    visuals.line_graph(scoreplot)
    
    # visuals.railway_map(random_railway)



