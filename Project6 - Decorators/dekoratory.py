import time
import cv2
import numpy as np
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-n','--number',help = 'number of loop iterations',type = int, default = 1)
args = parser.parse_args()
print(f'Loop iterations  {args.number = }')

def decorator (func):
    def wrapper():
        start = time.time()
        for i in range(args.number):
            func()
        end = time.time()
        print(f'Elapsed time: {end - start} seconds' )
    return wrapper


def saturation():
    image = cv2.imread("im2.jpg")
    alpha = 2
    new_image = np.zeros(image.shape, image.dtype)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            for c in range(image.shape[2]):
                new_image[y, x, c] = np.clip(alpha * image[y, x, c], 0, 255)
    cv2.imwrite("new_imag.jpg", new_image)
    return new_image

saturation = decorator(saturation)
saturation()

