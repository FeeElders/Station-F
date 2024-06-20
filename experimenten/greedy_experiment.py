from code.algoritmen import greedy as gr
from code import helpers
from code.visualisation import visuals

import matplotlib.pyplot as plt
import pandas as pd
import csv
import copy
import time

from statistics import mean 
from datetime import datetime

def greedy(railway: 'Railway') -> None:
    date = datetime.today().strftime('%d-%m-%Y')
    name = f"Greedy_{date}"
    scoreplot:dict[int:int] = {}
    count = 0
    interval = 20
    
    # create a new file
    with open(f'output/greedy/{name}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['iterations','score'])

    start = time.time()
    while count < 2:
        greedy = gr.Greedy(railway)
        greedy_railway = greedy.run(15)
        end = time.time()
        running_time = end-start

        greedy_railway.formatted_output(f"greedy/formatted_output_{name}_run_{count}.csv", running_time)
        scoreplot[count] = greedy_railway.score()
        
        if count%interval == 0:
            # sla elke +-10 minuten de scores op in een bestand
            with open(f'output/greedy/{name}.csv', 'a', newline='') as file:
                writer_new = csv.writer(file)
                for score in scoreplot:
                    writer_new.writerow([score, scoreplot[score]])
            scoreplot= {}
        count += 1  
    with open(f'output/greedy/{name}.csv', 'a', newline='') as file:
        writer_new = csv.writer(file)
        for score in scoreplot:
            writer_new.writerow([score, scoreplot[score]])
            
    return name


def smart_greedy(railway: 'Railway') -> None:
    date = datetime.today().strftime('%d-%m-%Y')
    name = f"SmartGreedy_{date}"
    scoreplot:dict[int:int] = {}
    count = 0
    interval = 20
    
    # create a new file
    with open(f'output/greedy/{name}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['iterations','score'])

    start = time.time()
    while count < 2:
        smart_greedy = gr.SmartStartStation(railway)
        smart_railway = smart_greedy.run(15)
        end = time.time()
        running_time = end-start

        smart_railway.formatted_output(f"greedy/formatted_output_{name}_run_{count}.csv", running_time)
        scoreplot[count] = smart_railway.score()
        
        if count%interval == 0:
            # sla elke +-10 minuten de scores op in een bestand
            with open(f'output/greedy/{name}.csv', 'a', newline='') as file:
                writer_new = csv.writer(file)
                for score in scoreplot:
                    writer_new.writerow([score, scoreplot[score]])
            scoreplot= {}
        count += 1  
    with open(f'output/greedy/{name}.csv', 'a', newline='') as file:
        writer_new = csv.writer(file)
        for score in scoreplot:
            writer_new.writerow([score, scoreplot[score]])
            
    return name
