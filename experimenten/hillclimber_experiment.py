from code.algoritmen import hillclimber as hc
from code.algoritmen import randomise as rd
from code import helpers
from code.visualisation import visuals 

import matplotlib.pyplot as plt
import csv
import copy
import time

from statistics import mean 


def hillclimb(railway):
    run_count = 0
    #TO DO random_railway importeren of maken
    
    datum = "19-06-2024"
    with open(f'output/hillclimber/hillclimber_{datum}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['run_count','end_score'])
        
    while run_count < 2:
        random = rd.Random(railway)
        random_railway = random.run(20)
        start = time.time()
        # create a new file
        with open(f'output/hillclimber/run_{run_count}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['iterations','score'])
        
        iterations = 300
        print("Setting up Hill Climber...")
        climber = hc.HillClimber(random_railway)

        print("Running Hill Climber...")
        climbing_railway = climber.run(run_count, active=True)

        print(f"Value of the configuration after Hill Climber: "
              f"{climber.railway.score()}")
        end = time.time()
        running_time = end - start      
        climber.railway.formatted_output(f"hillclimber/formatted_output_climber_{run_count}.csv", running_time)
                
        # Add end score to csv        
        with open(f'output/hillclimber/hillclimber_{datum}.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([run_count, climber.railway.score()])
                
        run_count += 1
     
     
        
    


    
        
        