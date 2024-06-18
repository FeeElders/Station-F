import random

from randomise import Random, NotSoRandom

class Greedy():
    def __init__(self, railway: 'Railway') -> None:
        self.railway = copy.deepcopy(railway)


    def get_shortest_connection(self) -> 'Connection':
        # TODO: implement
        pass

    
    def get_longest_connection(self) -> 'Connection':
        # TODO: implement
        pass

        
    def run_greedy(self) -> Railway:
        # TODO: implement
        pass


class RandomGreedy(Greedy, NotSoRandom):
    def random_or_greedy(self) -> Connection:
        """ Choose either a random connection or a greedy connection. """
        random_number = random.random()

        if random_number < 0.2:
            connection = get_random_connection()
        elif random_number < 0.8:
            connection = get_shortest_connection()
        else:
            connection = get_longest_connection()

        return connection


    def run_rdGreedy(self) -> Railway:
        # TODO: implement

        # connection = random_or_greedy
        pass
