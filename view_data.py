from PIL import Image
import numpy as np
import time


a = np.load('F:/.../self-driving-in-GTA5/collect_data/training_data-2.npy')  #Change it to your path

# print(a[499][0].shape)
print(a[10][1])   #press_key
b = Image.fromarray(a[10][0], mode='RGB')  #image

# b = Image.fromarray(a)

b.show()

# img = np.array(Image.open("lena.jpg"))
# img = Image.fromarray(img, mode='RGB')
# img.show()
