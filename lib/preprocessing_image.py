#!/usr/bin/env python

import os
import cv2
import numpy as np


transparent_pixel = np.array([0,0,0,0], dtype=np.uint8)
red_pixel = np.array([0,0,255,255], dtype=np.uint8)


def remove_edge_of_farm_from_tif(filename, remove_pixel_width=10, debug=False, remove_as_pixel = transparent_pixel):
    # read image
    # tif must open as unchanged
    image = cv2.imread(filename, cv2.IMREAD_UNCHANGED )
    # copy to final image
    final_image = image.copy()
    # loop over all pixels
    h = image.shape[0]
    w = image.shape[1]
    current_x = 0
    current_y = 0
    last_x = w - 1
    last_y = h - 1
    current_processing = 0
    max_processing = h * w
    while current_processing < max_processing:
        current_processing += 1
        if current_x > last_x:
            current_x = 0
            current_y += 1
        if current_y > last_y:
            break
        # processing x
        if debug:
            print(current_x, current_y)

        current_pixel = image[current_y, current_x]

        if current_x == 0:
            previous_pixel = transparent_pixel
        else:
            previous_pixel = image[current_y, current_x - 1]

        # check upper pixel
        if current_y ==  0:
            upper_pixel = transparent_pixel
        else:
            upper_pixel = image[current_y-1, current_x]
        # check below pixel
        if current_y == last_y:
            below_pixel = transparent_pixel
        else:
            below_pixel = image[current_y+1, current_x]

        if current_x == last_x:
            next_pixel = transparent_pixel
        else:
            next_pixel = image[current_y, current_x + 1]

        previous_transparency = ( previous_pixel == transparent_pixel ).all()
        current_transparency = ( current_pixel == transparent_pixel ).all()
        next_transparency = ( next_pixel == transparent_pixel ).all()
        upper_transparency = ( upper_pixel == transparent_pixel ).all()
        below_transparency = ( below_pixel == transparent_pixel ).all()

        # 현재 필셀이 공백이고 다음 픽셀이 공백이 아니면 
        # x 축을  remove_pixel_width 만큼 이미지를 공백으로 칠한다.
        if ( current_transparency == True and next_transparency != True):
            for x in range(current_x+1, current_x + remove_pixel_width+1):
                if x <= (w -1 ):
                    final_image[current_y,x] = remove_as_pixel
                    if debug:
                        print("set ", current_y, x, "to transparent" )
        # 현재 픽셀은 공백이 아니고 전픽셀이 공백일대
        if ( current_transparency != True) and ( previous_transparency == True):
            for x in range(current_x+1, current_x + remove_pixel_width+1):
                if x <= (w -1 ):
                    final_image[current_y,x] = remove_as_pixel
                    if debug:
                        print("set ", current_y, x, "to transparent" )

        # 현재 픽셀이 공백이고 그전 픽셀은 공백이 아닐때 
        # x 축을 좌측으로 remove_pixel_width 만큼 이미지를 공백으로 칠하고 current_x 를 1만큼 이동한다.
        if (current_transparency == True) and (previous_transparency != True):
            for x in range(current_x-1, current_x - remove_pixel_width-1, -1):
                if x > 0:
                    final_image[current_y,x] = remove_as_pixel
                    if debug:
                        print("set ", current_y, x, "to transparent" )
        # 윗 픽셀이 투명이고 현 픽셀이 투명이 아니면 아래로 remove_pixel_width 만큼 이미지를 공백으로 칠한다.
        if ( upper_transparency == True) and ( current_transparency != True):
            for y in range(current_y, current_y + remove_pixel_width+1):
                if y <= last_y and y > 0:
                    final_image[y,current_x] = remove_as_pixel
                    if debug:
                        print("set ", current_y, x, "to transparent" )
        # 아랫픽셀이 투명이고 현필셀이 투명이 아니면 위로 remove_pixel_width 만큼 이미지를 공백으로 칠한다.
        if ( below_transparency == True) and ( current_transparency != True):
            for y in range(current_y, current_y - remove_pixel_width-1, -1):
                if y <= last_y and y > 0:
                    final_image[y,current_x] = remove_as_pixel
                    if debug:
                        print("set ", current_y, x, "to transparent" )

            pass
        current_x += 1
    return final_image


current_dir = os.path.dirname(os.path.realpath(__file__))
testing_file = os.path.join(current_dir, "../tests/fixture/학동리-8384.tif")

"""
# for debugging 삭제된 부분을 빨강색으로 정리한다.
from lib.preprocessing_image import *
final_image = remove_edge_of_farm_from_tif(testing_file, debug=False, remove_as_pixel = red_pixel)
cv2.imwrite("/mnt/d/systech-output/trans/test1.tif", final_image)

"""


if __name__ == '__main__':
    remove_edge_of_farm_from_tif(testing_file)
