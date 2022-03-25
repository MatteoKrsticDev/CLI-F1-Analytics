# Libraries importation
from time import sleep
from matplotlib import pyplot as plt
import fastf1
import fastf1.plotting
from fastf1 import *
import colorama
from colorama import Back
import os

# color class to make everything prettier

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


# Function to create the time graph

def TimeGraph():
    fastf1.plotting.setup_mpl()
    fastf1.Cache.enable_cache(r"""Your path""") # Insert he path of the folder where you want to collect the cache. 
    # I raccomend to use the cache folder that is already present in the project
    # You have to paste the path of your folder like this: "YOUR DISK:\path\CLI-F1-Analytics\src\cache"

    print(color.RED + "Welcome to the cli-f1-analytics" + color.RESET)
    print(color.BLUE + "Enter the year of the session you want" + color.RESET)

    year = input("=>")

    print(color.BLUE + "Enter the circuit you want" + color.RESET)

    circuit = input("=>")
    str(circuit)
    print(color.BLUE + "Enter the session you want" + color.RESET)
    print(color.GREEN + "FP1, FP2, FP3, Q = qualification, R = race" + color.RESET)

    session_type = input("=>")

    session_type.upper()
    session = fastf1.get_session(int(year), str(circuit), str(session_type))

    print(color.BLUE + "Enter the driver you want" + color.RESET)
    driver = input("=>")
    str(driver)
    driver2 = driver[0:3].upper()


    session.load()

    # collecting informations
    car = session.laps.pick_driver(driver2).pick_fastest()
    car_data = car.get_car_data()
    q = car_data['Time']
    qs = car_data['Speed']

    # plotting
    ax = plt.subplot()
    ax.plot(q, qs, label='speed')
    ax.set_xlabel('Time')
    ax.set_ylabel('Speed [km/h]')
    ax.set_title(str(driver) + " lap" + " in " + str(circuit) + " year " + str(year))
    ax.legend()
    plt.show()




def main():
    print(color.GREEN  + "Welcome to the CLI-F1-Analytics" + color.RESET)
    print(" ")
    print(color.BLUE + "To begin choose an option" + color.RESET)
    print(color.RED + "[1] Speed camparision over time" + color.RESET)
    print(color.RED + "[2] exit" + color.RESET)
    action = input("=>")
    if action == '1':
        TimeGraph()
    elif action == '2':
        exit
    else:  
        os.system("cls")
        main()
main()