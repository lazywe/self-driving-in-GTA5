from directkeys import PressKey, ReleaseKey, W, A, S, D
import numpy as np
from keras.models import load_model
import random
import cv2

from grabscreen import grab_screen
import time
from getkeys import key_check
from yolo import YOLO
from find_lane import roi,draw_lanes,process_img
from collision_detection import collision_detection


def straight():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
    ReleaseKey(S)


def left():
    ReleaseKey(W)
    PressKey(A)
    ReleaseKey(S)
    ReleaseKey(D)
    PressKey(A)
    ReleaseKey(S)
    ReleaseKey(D)


def right():
    ReleaseKey(W)
    PressKey(D)
    ReleaseKey(A)
    ReleaseKey(S)
    PressKey(D)
    ReleaseKey(A)
    ReleaseKey(S)

def reverse():
    PressKey(S)
    ReleaseKey(A)
    ReleaseKey(W)
    ReleaseKey(D)


def forward_left():
    PressKey(W)
    PressKey(A)
    ReleaseKey(D)
    ReleaseKey(S)
    PressKey(W)
    PressKey(A)
    ReleaseKey(D)
    ReleaseKey(S)

def forward_right():
    PressKey(W)
    PressKey(D)
    ReleaseKey(A)
    ReleaseKey(S)
    PressKey(W)
    PressKey(D)
    ReleaseKey(A)
    ReleaseKey(S)

def reverse_left():
    PressKey(S)
    PressKey(A)
    ReleaseKey(W)
    ReleaseKey(D)
    PressKey(S)
    PressKey(A)
    ReleaseKey(W)
    ReleaseKey(D)

def reverse_right():
    PressKey(S)
    PressKey(D)
    ReleaseKey(W)
    ReleaseKey(A)
    PressKey(S)
    PressKey(D)
    ReleaseKey(W)
    ReleaseKey(A)

def no_keys():
    if random.randrange(0, 3) == 1:
        PressKey(W)
    else:
        ReleaseKey(W)
    ReleaseKey(A)
    ReleaseKey(S)
    ReleaseKey(D)


model = load_model('model_new_2.h5')
yolo = YOLO()
paused = False

print("Starting in... ")
for i in list(range(5))[::-1]:
    print(i+1)
    time.sleep(1)

while True:

    if not paused:
        last_time = time.time()

        #screen = grab_screen(region=(0, 40, 800, 600))
        image_array = grab_screen(region=(0, 30, 1280, 750))
        array_to_image = Image.fromarray(image_array, mode='RGB')
        r_image, left_top_x, left_top_y, right_bottom_x, right_bottom_y, predict_classes = yolo.detect_image(
            array_to_image)

        img = np.asarray(r_image)

        img = collision_detection(img, left_top_x, left_top_y, right_bottom_x, right_bottom_y, predict_classes)

        new_screen, original_image = process_img(img)

        screen_for_prediction = cv2.resize(
            original_image, (523, 294))
        screen_for_prediction = cv2.GaussianBlur(
            screen_for_prediction, (3, 3), 0)
        # screen_for_prediction = screen_for_prediction.reshape(1,
        #                                                       224, 224, 1)
        screen_for_prediction = screen_for_prediction.reshape(1,
                                                              523, 294, 3)
        prediction = model.predict(screen_for_prediction)[0]
        mode_choice = np.argmax(prediction)
        if mode_choice == 0:
            straight()
            choice_picked = 'straight'
        elif mode_choice == 1:
            reverse()
            choice_picked = 'reverse'
        elif mode_choice == 2:
            left()
            choice_picked = 'left'
        elif mode_choice == 3:
            right()
            choice_picked = 'right'
        elif mode_choice == 4:
            forward_left()
            choice_picked = 'forward+left'
        elif mode_choice == 5:
            forward_right()
            choice_picked = 'forward+right'
        elif mode_choice == 6:
            reverse_left()
            choice_picked = 'reverse+left'
        elif mode_choice == 7:
            reverse_right()
            choice_picked = 'reverse+right'
        elif mode_choice == 8:
            no_keys()
            choice_picked = 'nokeys'

        ###Print FPS ####
        # print("Fps: {} Prediction: {}".format(
        #     1 / (time.time() - last_time), choice_picked))
        # #cv2.imshow("Screen", cv2.resize(screen, (400, 200)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
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
            ReleaseKey(A)
            ReleaseKey(W)
            ReleaseKey(D)
            time.sleep(1)
