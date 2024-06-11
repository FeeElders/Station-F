import copy
import random


class Random():
    def __init__(self, railway) -> None:
        self.new_railway = copy.deepcopy(railway)


    def run(self) -> 'Railway':

        while self.new_railway.trains() <= random.randint(1, self.new_railway._max_trains):
            current_station = self.new_railway.get_random_station()
            self.new_railway.new_trajectory(current_station)
            
            train_number = self.new_railway.trains()
            traject = self.new_railway._trains[train_number]
            

            while traject.is_running():
                time = traject.time_left()
                current_station = traject.current_station()
                connection = self.new_railway.get_random_connection(current_station._name, time)
                if connection == None:
#                    traject.end()
                    break

                
                else: 
                    traject.add_connection(connection)    


        print(f"the score: {self.new_railway.score()}")
                    
        return self.new_railway
