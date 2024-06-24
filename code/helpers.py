import csv
import pickle
from csv import writer
from code.classes import railway


def best_score(new_railway, best_railway) -> bool:
    if best_railway is None or new_railway.score() > best_railway.score():
        return True
    else:
        return False


def create_csv(name) -> None:
    with open(f'output/{name}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['score'])


def append_to_csv(name, csv_scores) -> None:   
    
        with open(f'output/{name}.csv', 'a', newline='') as file:
            writer_new = csv.writer(file)
#            writer_new.writerow(["time", time])
            for score in csv_scores:
                writer_new.writerow([score])
                
        csv_scores.clear()
        
        
def object_output(railway: 'Railway', filename: str) -> None:
    """ 
    Save the connections so that we can visualise them
    When the track is complete give back all the connections
    Containing start and finish of each connection and the time passed 
    """
    
    with open(f'output/{filename}.pkl', 'wb') as file:
        pickle.dump(railway, file)                   
        file.close()

    
    # with open(f'output/{filename}', 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['train', 'stations'])
#
#
#         for train in railway._trains:
#             train_id = train
#             formatted_id = f"train_{train_id}"
#             trajectory_obj = railway._trains[train]
#             station_objects = trajectory_obj._trajectory
#
#             counter = 1
#             for station in station_objects:
#
#                 stations_list.append(station._name)
#
#
#             writer.writerow([formatted_id, stations_string])
    
 
