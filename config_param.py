
import numpy as np

DEBUG = True

# Variables
if DEBUG:
    simulation_pos = {}
result_pos = {} # targets postion
pos = [600, 50, np.pi/2]
target_position = [600, 600, np.pi/2]

# TODO : config param(ref : camera)
delta_angle = np.pi/6
dis_n = 30
dis_p = 500

# ! simulation param
# TODO : config param(ref : robot's Wheel)
if DEBUG:
    step_angle = np.pi/180
    step_dis = 5