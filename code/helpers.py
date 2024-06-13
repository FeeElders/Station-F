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


def append_to_csv(name, interval, count, csv_scores) -> None:   
    if count%interval == 0:
        # sla elke +-10 minuten de scores op in een bestand
        with open(f'output/{name}.csv', 'a', newline='') as file:
            writer_new = csv.writer(file)
            for score in csv_scores:
                print(score)
                writer_new.writerow([score])
                
        csv_scores.clear()
