import cv2
import matplotlib.pyplot as plt
import numpy as np

img = np.zeros((720, 1280, 3), np.uint8)
# area1 = np.array([[120, 670], [120, 600], [300, 430], [850, 430], [1280, 600], [1280, 670], [230, 670]
#                          ])
area1 = np.array([[150, 670], [250, 430], [850, 430], [1280, 600], [1280, 670],[1000,670],[600,450],[450,450],[300,670]
                         ])
cv2.fillPoly(img, [area1], (255, 255, 255))

plt.imshow(img)
#plt.savefig("filename.png")
plt.show()
