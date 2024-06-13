import pickle

from code.classes import station, railway, connection, trajectory
from code.visualisation import visuals 
from code.algoritmen  import randomise as rd



if __name__ == "__main__":
    with open('best_railway.obj', 'rb') as file:
        loaded_railway = pickle.load(file)

    print(loaded_railway)
    print(loaded_railway.score())

