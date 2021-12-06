import cv2 as cv
from config_param import *

def draw_map(img):
    # draw edges
    cv.line(img, (0, 250),        (1200, 250),        (0, 255, 0))
    cv.line(img, (0, 1200 - 250), (1200, 1200 - 250), (0, 255, 0))
    cv.line(img, (150, 0),        (150, 1200),        (0, 255, 0))
    cv.line(img, (1200 - 150, 0), (1200 - 150, 1200), (0, 255, 0))
    cv.line(img, (0, 0), (0, 1199),                   (255, 255, 0))
    cv.line(img, (0, 0), (1199, 0),                   (255, 255, 0))
    cv.line(img, (1199, 1199), (0, 1199),             (255, 255, 0))
    cv.line(img, (1199, 1199), (1199, 0),             (255, 255, 0))
    # draw tower bases
    ## TODO : check the position in final rules
    cv.circle(img, tower_base_1_pos, 25, (0, 255 , 0), 2)
    cv.circle(img, tower_base_2_pos, 25, (0, 255 , 0), 2)
    cv.rectangle(img, (375 - 25, 600 - 25)       , (375 + 25, 600 + 25)       , (0, 255, 0), 2)
    cv.rectangle(img, (1199 - 375 - 25, 600 - 25), (1199 - 375 + 25, 600 + 25), (0, 255, 0), 2)



def draw_current_area(img, area):
    for i in range(len(area)):
        if i != len(area) - 1:
            cv.line(img, area[i], area[i+1], (0, 0, 255))
        else:
            cv.line(img, area[i], area[0], (0, 0, 255))

def draw_targets(img_of_raw, img_of_detect):
    siz_of_tgt = [10, 13, 17, 21, 25] # size of panzi

    global DEBUG
    if DEBUG: # simulation drawing
        global simulation_pos
        for i in list(simulation_pos.keys()):
            color = [255, 255, 0]
            if i[0] == 'r':
                color = [0, 0, 255]
            elif i[0] == 'b':
                color = [255, 0, 0]

            cv.circle(img_of_raw, simulation_pos[i], siz_of_tgt[int(i[1:]) - 1],  color, 2)
            
    for i in list(result_pos.keys()):
        color = [255, 255, 0]
        if i[0] == 'r':
            color = [0, 0, 255]
        elif i[0] == 'b':
            color = [255, 0, 0]

        cv.circle(img_of_detect, result_pos[i], siz_of_tgt[int(i[1:]) - 1],  color, 2)

def draw_for_output(im1, im2, cur):

    draw_map(im1)
    draw_map(im2)

    draw_current_area(im2, cur)

    draw_targets(im1, im2)

    res = np.hstack((im1, im2))
    res = cv.resize(res, (1200, 600), fx=0.5, fy=0.5)
    return res