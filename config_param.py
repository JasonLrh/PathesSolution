
import numpy as np

DEBUG = True

# Variables， 
# ! not configureable
if DEBUG:
    simulation_pos = {}
result_pos = {} # panzi's postion
exp_targets = []
'''
如果是真机调试
程序读取摄像头位置(pos)以及反馈的块信息(更新字典)，
然后计算出当前块的位置(target_position)
'''
# ? not suggest to change(rules)
pos = [600, 50, np.pi/2]
task_progress = 0
tower_base_1_pos = (375       , 600)
tower_base_2_pos = (1199 - 375, 600)


# TODO : config param(ref : camera)
delta_angle = np.pi/6
dis_n = 30
dis_p = 500

# simulation param
# ? configureable
if DEBUG:
    step_angle = np.pi/45
    step_dis = 10