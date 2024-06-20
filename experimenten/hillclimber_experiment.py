from code.algoritmen import hillclimber as hc
from code.algoritmen import randomise as rd
from code import helpers
from code.visualisation import visuals 

import pandas as pd
import matplotlib.pyplot as plt
import csv
import copy
import time

from statistics import mean 


def hillclimb(railway):
    run_count = 0
    #TO DO random_railway importeren of maken
    
    datum = "20-06-2024"
    with open(f'output/hillclimber/hillclimber_{datum}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['run_count','end_score'])
        
    while run_count < 20:
        random = rd.Random(railway)
        random_railway = random.run(20)
        start = time.time()
        # create a new file
        with open(f'output/hillclimber/run_{run_count}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['iterations','score'])
        
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
        
    return datum
       
def line_graph(counts):  
    """
    Plotten van de score vs de iteraties in een histogram
    y as komt de score en op de x as het aantal pogingen
    """
    colors = ["black", "deeppink", "plum", "olive", "orange", "grey", "firebrick", "darksalmon", "lightgrey", "gold", "deepskyblue", "chartreuse", "green", "teal",  "blue", "indigo", "greenyellow", "crimson", "lemonchiffon", "darkmagenta", "azure", "bisque"]
    fig, ax = plt.subplots()

    ax.set_title('Hill Climber algoritme')
    ax.set_xlabel('Iteraties')
    ax.set_ylabel('Score')

    print(f"counts: {counts}")
    for run_count in range(counts):
        print(run_count)
        df = pd.read_csv(f'output/hillclimber/run_{run_count}.csv', delimiter=',')   
        x = df["iterations"]
        y = df["score"]
           
        # We can set the number of bins with the *bins* keyword argument.
        plt.plot(x, y, color=colors[run_count], linestyle="-")    

    plt.show()
    fig.savefig(f"output/hillclimber/line_graph_hillclimber.png")      
        
def hist_graph(datum):
    """
    Plotten van de scores per algoritme in een hisogram
    y as komt het aantal pogingen en op de x as de score
    """
    
    fig, axs = plt.subplots()
    df = pd.read_csv(f'output/hillclimber/hillclimber_{datum}.csv', delimiter=',')
    run_count = df["run_count"]
    end_score = df["end_score"]#.values.tolist()
    
    print(end_score)

    count = len(df["end_score"])
    print(count)
    n_bins = 5

    # We can set the number of bins with the *bins* keyword argument.
    axs.hist(end_score, bins=n_bins)

    axs.set_xlim(0, 8000)
   
    axs.set(xlabel='Score (K)', ylabel='Frequentie',
              title=f'Hill Climber 400 bins {count} keer')
    plt.show()
    fig.savefig(f"output/hillclimber/histogram_hillclimber_{datum}.png")
    
    return count
     
     

    


    
        
        
