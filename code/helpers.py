import csv
from csv import writer

def best_score(new_railway, best_railway) -> bool:
    if best_railway is None or new_railway.score() > best_railway.score():
        return True
    else:
        return False


def create_csv(name) -> None:
    with open(f'output/{name}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['score'])


def append_to_csv(name, csv_scores, time) -> None:   
    
        with open(f'output/{name}.csv', 'a', newline='') as file:
            writer_new = csv.writer(file)
            writer_new.writerow(["time", time])
            for score in csv_scores:
                writer_new.writerow([score])
                
        csv_scores.clear()
