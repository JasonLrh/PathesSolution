
import numpy as np

DEBUG = True

# Variables
if DEBUG:
    simulation_pos = {}
result_pos = {} # panzi's postion
'''
如果是真机调试
程序读取摄像头位置(pos)以及反馈的块信息(更新字典)，
然后计算出当前块的位置(target_position)
'''
pos = [600, 50, np.pi/2]


# TODO : config param(ref : camera)
delta_angle = np.pi/6
dis_n = 30
dis_p = 500

# ! simulation param
# TODO : config param(ref : robot's Wheel)
if DEBUG:
    step_angle = np.pi/180
    step_dis = 10