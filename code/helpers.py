import csv
import pickle
from csv import writer
from code.classes import railway


def best_score(new_railway, best_railway) -> bool:
    """ Determine the best score between two railways.

    Args:
    new_railway ('Railway'): the new railway
    best_railway ('Railway'): the best railway to compare it with
    """
    if best_railway is None or new_railway.score() > best_railway.score():
        return True
    else:
        return False


def create_csv(name: str) -> None:
    """ Create new CSV file

    Args:
    name (str): the name of the file
    """
    with open(f'output/{name}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['score'])


def append_to_csv(name: str, csv_scores: list[int]) -> None:   
    """ Append scores to csv file.

    Args:
    name (str): the name of the file
    csv_scores (dict[int:int]): the csv scores per iteration"""
    with open(f'output/{name}.csv', 'a', newline='') as file:
        writer_new = csv.writer(file)
        for score in csv_scores:
            writer_new.writerow([score])
                
        csv_scores.clear()
        
        
def object_output(railway: 'Railway', filename: str) -> None:
    """ Pickle railway object. """    
    with open(f'output/{filename}.pkl', 'wb') as file:
        pickle.dump(railway, file)                   
        file.close()
