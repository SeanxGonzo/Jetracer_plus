# steering_command_argument.py
# Author: Sean Gonzales

from jetracer.nvidia_racecar import NvidiaRacecar

import argparse 


car= NvidiaRacecar()

parser = argparse.ArgumentParser()

parser.add_argument('--value', type=float, required=True)

args = parser.parse_args()

car.steering = args.value

print=("The command servo value is: ", args.value)