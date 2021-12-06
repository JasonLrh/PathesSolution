import cv2 as cv
import numpy as np
import random
import sys
import math

import ui_api
from config_param import *

# init
if len(sys.argv) != 2:
    print("Error argument number. please select team color.")
    exit()
our_team_color = sys.argv[1][0]
if our_team_color != 'r' and our_team_color != 'b':
    print("Error argument. [r] | [b]")
    print("your argument : %s" % our_team_color)
    exit()
exp_targets = []
for i in range(5):
    if i % 2 == 0:
        ele = "%s%d" % (our_team_color, 5 - i)
    else:
        if our_team_color == 'r':
            c = 'b'
        else:
            c = 'r'
        ele = "%s%d" % (c, 5 - i)
    exp_targets.append(ele)
print("target : ", exp_targets)


img = np.zeros((1200, 1200), np.uint8)
pros = np.zeros((1200, 1200), np.uint8)


def process_area(position):
    global delta_angle, dis_n, dis_p

    x, y, angle = position
    angle_n = angle - delta_angle
    angle_p = angle + delta_angle
    point = [(int(np.cos(angle_n) * dis_n + x), int(np.sin(angle_n) * dis_n + y)),
             (int(np.cos(angle_n) * dis_p + x), int(np.sin(angle_n) * dis_p + y)),
             (int(np.cos(angle_p) * dis_p + x), int(np.sin(angle_p) * dis_p + y)),
             (int(np.cos(angle_p) * dis_n + x), int(np.sin(angle_p) * dis_n + y))]
    return point


step = 0
base_scan = [   [600, 50,  3 * np.pi/4],\
                [1050, 220, np.pi/2],\
                [150, 220, np.pi/2],\
                [150, 520, np.pi/2],\
                [1050, 520, np.pi/2],
                ]
base_scan_step = 0

target_position = base_scan[0]
solution_count = 0

def on_process():
    global step, target_position
    if step == 0:
        global base_scan_step
        base_scan_step += 1
        if base_scan_step >= len(base_scan):
            step += 1
            print("next_step")
            on_process()
            return
        target_position = base_scan[base_scan_step]
    elif step == 1:
        global solution_count, pos
        print("exp :", exp_targets[solution_count])
        target_position = result_pos[exp_targets[solution_count]]
        delta = list(np.array(pos[0:1]) - np.array(target_position))
        theta = np.arctan2(delta[1], delta[0])
        target_position.append(theta)
        print(target_position)
        # solution_count += 1
        # if solution_count == len(exp_targets):
        #     step += 1
        #     print("next_step")
    elif step == 2:
        pass



def process_step(im1, im2, cl1, cl2):  
    cnts, heri = cv.findContours((im2), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(cl2, cnts, -1, [255, 0, 255], 8)

    if DEBUG:
        global simulation_pos
        for i in list(simulation_pos.keys()):
            if im2[simulation_pos[i][1], simulation_pos[i][0]] != 0:
                result_pos[i] = simulation_pos[i]
    
    if DEBUG:# ! simulation : step generate
        global pos, step_angle, step_dis
        delta = list(np.array(pos) - np.array(target_position))
        k_state = 0
        if np.abs(delta[0]**2 + delta[1] ** 2) <= 1.5 * step_dis:
            pos[0] = target_position[0]
            pos[1] = target_position[1]
            k_state = 1
        else:
            theta = np.arctan2(delta[1], delta[0])
            pos[0] -= np.cos(theta) * step_dis
            pos[1] -= np.sin(theta) * step_dis
        
        if np.abs(delta[2]) <= step_angle:
            pos[2] = target_position[2]
            if k_state == 1:
                k_state = 2
        else:
            if delta[2] > 0:
                pos[2] -= step_angle
            else:
                pos[2] += step_angle
        cv.line(cl1, (int(pos[0]), int(pos[1])), (int(target_position[0]), int(target_position[1])), [0, 255, 0], 2)
        cv.line(cl2, (int(pos[0]), int(pos[1])), (int(target_position[0]), int(target_position[1])), [0, 255, 0], 2)
        if k_state == 2: # arrive at target
            on_process()


if DEBUG: # ! simulation : process tareget
    random.seed(1)
    for i in ['r', 'b']:
        for j in range(1, 6):
            name = "%c%d" % (i, j)
            posa = [random.randint(150, 1200 - 150),
                    random.randint(250, 1200 - 250)]
            simulation_pos[name] = posa

while True:
    curi = process_area(pos)  # get robot camera position -> curios area
    res1 = cv.fillPoly(img, [np.array(curi)], (255))
    res2 = cv.fillPoly(pros, [np.array(curi)], (255))

    rb1 = cv.cvtColor(res1, cv.COLOR_GRAY2BGR)
    rb2 = cv.cvtColor(res2, cv.COLOR_GRAY2BGR)

    process_step(res1, res2, rb1, rb2)

    cv.imshow('img', ui_api.draw_for_output(rb1, rb2, curi))
    key = cv.waitKey(1)
    if key == ord('q'):
        break

    img[:, :] = 0

cv.destroyAllWindows()