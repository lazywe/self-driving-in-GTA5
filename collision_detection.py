import cv2
from directkeys import PressKey, ReleaseKey, W, A, S, D

def reverse():
    PressKey(S)
    ReleaseKey(A)
    ReleaseKey(W)
    ReleaseKey(D)

def collision_detection(img, left_top_x, left_top_y, right_bottom_x, right_bottom_y, predict_classes):
    if predict_classes == 'truck' or predict_classes == 'car' or predict_classes == 'bus':
        mid_x = ((left_top_x + right_bottom_x) / 2) / 1280
        mid_y = ((left_top_y + right_bottom_y) / 2) / 720
        t = right_bottom_x - left_top_x
        left_right_distance = 1280 * t - 7 * (t ** 2)  # =(1280-7t)*t
        # cv2.putText(img, '{}'.format(left_right_distance), (int(mid_x * 1280), int(mid_y * 720)),
        #             cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        if left_right_distance <= 0:
            if mid_x > 0.25:
                reverse() # Too close to slow down

                cv2.putText(img, 'STOP!', (int(mid_x * 1280), int(mid_y * 720) - 30), cv2.FONT_HERSHEY_SIMPLEX,
                            1.0, (255, 0, 0), 5)
                cv2.putText(img, 'STOP!', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                            (255, 0, 0), 5)
    if predict_classes == 'bicycle' or predict_classes == 'person':
        mid_x = ((left_top_x + right_bottom_x) / 2) / 1280
        mid_y = ((left_top_y + right_bottom_y) / 2) / 720
        t = right_bottom_x - left_top_x
        left_right_distance = 1280 * t - 15 * (t ** 2)  # =(1280-8t)*t
        # cv2.putText(img, '{}'.format(left_right_distance), (int(mid_x * 1280), int(mid_y * 720)),
        #             cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        if left_right_distance <= 0:
            if mid_x > 0.15:
                reverse()  # Too close to slow down

                cv2.putText(img, 'STOP!', (int(mid_x * 1280), int(mid_y * 720) - 30), cv2.FONT_HERSHEY_SIMPLEX,
                            1.0, (255, 0, 0), 5)
                cv2.putText(img, 'STOP!', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                            (255, 0, 0), 5)

    return img