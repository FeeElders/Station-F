from code.classes import station, railway, connection, trajectory
from code.algoritmen  import randomise

if __name__ == "__main__":
    print("WELCOME TO RailNL")

    railway = railway.Railway()
    railway.load_stations()
    railway.load_connections()


    # --------------------Random----------------------------------
    random_railway = randomise.random(railway)
   

#    railway.formatted_output()


## uiteindelijk deze dingen 10000 keer uitvoeren en plotten om de gemiddelde 
