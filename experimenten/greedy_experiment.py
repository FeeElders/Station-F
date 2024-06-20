from code.algoritmen import greedy as gr
from code import helpers
from code.visualisation import visuals

import matplotlib.pyplot as plt
import pandas as pd

import csv
import copy
import time

from statistics import mean 


def greedy(railway: 'Railway') -> None:

    name = 


    # create a new file
    with open(f'output/greedy/{name}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['iterations','score'])
