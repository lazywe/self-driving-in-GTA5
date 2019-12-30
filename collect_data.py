import numpy as np
from grabscreen import grab_screen
import cv2
import time
from getkeys import key_check
import os
from datetime import datetime
import colorsys
from timeit import default_timer as timer

from keras import backend as K
from keras.models import load_model
from keras.layers import Input
from PIL import Image, ImageFont, ImageDraw

from yolo3.model import yolo_eval, yolo_body, tiny_yolo_body
from yolo3.utils import letterbox_image
from keras.utils import multi_gpu_model
import tensorflow as tf
from grabscreen import grab_screen
from statistics import mean
from numpy import ones,vstack
from numpy.linalg import lstsq
from yolo import YOLO
from find_lane import roi,draw_lanes,process_img
from collision_detection import collision_detection
config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.7
session = tf.Session(config=config)

w = [1, 0, 0, 0, 0, 0, 0, 0, 0]
s = [0, 1, 0, 0, 0, 0, 0, 0, 0]
a = [0, 0, 1, 0, 0, 0, 0, 0, 0]
d = [0, 0, 0, 1, 0, 0, 0, 0, 0]
wa = [0, 0, 0, 0, 1, 0, 0, 0, 0]
wd = [0, 0, 0, 0, 0, 1, 0, 0, 0]
sa = [0, 0, 0, 0, 0, 0, 1, 0, 0]
sd = [0, 0, 0, 0, 0, 0, 0, 1, 0]
nk = [0, 0, 0, 0, 0, 0, 0, 0, 1]

t = datetime.now()
formatted_time = t.strftime('%y_%m_%d_%H_%M')


def keys_to_output(keys):
    '''
    Convert keys to a ...multi-hot... array
     0  1  2  3  4   5   6   7    8
    [W, S, A, D, WA, WD, SA, SD, NOKEY] boolean values.
    '''
    output = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    if 'W' in keys and 'A' in keys:
        output = wa
    elif 'W' in keys and 'D' in keys:
        output = wd
    elif 'S' in keys and 'A' in keys:
        output = sa
    elif 'S' in keys and 'D' in keys:
        output = sd
    elif 'W' in keys:
        output = w
    elif 'S' in keys:
        output = s
    elif 'A' in keys:
        output = a
    elif 'D' in keys:
        output = d
    else:
        output = nk
    return output


def preprocess_screen(screen):

    screen = cv2.resize(screen, (523, 294))
    return screen


starting_value = 1


while True:
    file_name = 'F:/.../self-driving-in-GTA5/collect_data/training_data-{}.npy'.format(   # Change it to your path
        starting_value)
    if os.path.isfile(file_name):
        print(
            'File exists, creating new training_data.npy file')
        starting_value += 1
    else:
        print('Starting fresh file with training_data.npy number: ', starting_value)
        training_data = []

        break


def main(file_name, starting_value):

    yolo = YOLO()
    file_name = file_name
    starting_value = starting_value

    print("Starting in....")
    for i in list(range(5))[::-1]:
        print(i+1)
        time.sleep(1)

    training_data = []

    paused = False
    while(True):
        if not paused:

            image_array = grab_screen(region=(0, 30, 1280, 750))
            array_to_image = Image.fromarray(image_array, mode='RGB')
            r_image, left_top_x, left_top_y, right_bottom_x, right_bottom_y, predict_classes = yolo.detect_image(
                array_to_image)

            img = np.asarray(r_image)
            img = collision_detection(img, left_top_x, left_top_y, right_bottom_x, right_bottom_y, predict_classes)

            new_screen, original_image = process_img(img)

            screen = preprocess_screen(original_image)

            keys = key_check()
            output = keys_to_output(keys)
            training_data.append([screen, output])

            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

            if len(training_data) % 100 == 0:
                print(len(training_data))

                if len(training_data) == 500:
                    np.save(file_name, training_data)
                    print('SAVED')
                    training_data = []
                    starting_value += 1
                    file_name = 'F:/.../self-driving-in-GTA5/collect_data/training_data-{}.npy'.format(  # Change it to your path
                        starting_value)

        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                print('Unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)


main(file_name, starting_value)
