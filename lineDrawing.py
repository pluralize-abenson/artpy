"""
Credit to Pirosuke. Minor edits to improve readability and usability.
"""
import os
import cv2
import numpy as np


def create_line_drawing_image(img, kernelDim=5):
    kernel = np.ones((kernelDim, kernelDim), np.uint8)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_dilated = cv2.dilate(img_gray, kernel, iterations=1)
    img_diff = cv2.absdiff(img_dilated, img_gray)
    contour = 255 - img_diff
    return contour


def convert_images(dir_from, dir_to, file_type = 'jpg'):
    for file_name in os.listdir(dir_from):
        if file_name.endswith(file_type) or file_name.endswith(file_type.upper()):
            print(file_name)
            img = cv2.imread(os.path.join(dir_from, file_name))
            img_contour = create_line_drawing_image(img)
            cv2.imwrite(os.path.join(dir_to, file_name), img_contour)Im