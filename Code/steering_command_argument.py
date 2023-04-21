# steering_command_argument.py
# Author: Sean Gonzales
#4-21-23 version
from jetracer.nvidia_racecar import NvidiaRacecar

import argparse 


car= NvidiaRacecar()

parser = argparse.ArgumentParser()

#adding a way to input into the program "--value" flag
parser.add_argument('--value', type=float, required=True)

args = parser.parse_args()

car.steering = args.value

print=("The command servo value is: ", args.value)