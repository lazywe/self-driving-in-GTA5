import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Flatten,\
    Conv2D, MaxPooling2D
from keras.layers.normalization import BatchNormalization
from keras.optimizers import Adam
import numpy as np
import os
import tensorflow as tf
from keras.utils.generic_utils import get_custom_objects
from keras import backend as K
import time
###############swish activation function######
def swish(x):
    return (K.sigmoid(x) * x)
###########################################

os.environ["CUDA_VISIBLE_DEVICES"] = "0"  #（其中0,1是选择所调用的gpu）


def alexnet_pro():
    model = Sequential()
    # 1st Convolutional Layer
    model.add(Conv2D(filters=96, input_shape=(294, 523), kernel_size=(3, 3),
                     strides=(4, 4), padding='valid'))
    # model.add(Activation('relu'))
    model.add(Activation(swish))
    ######strided convolution instead of pool########
    model.add(Conv2D(filters=96, kernel_size=(
        3, 3), strides=(2, 2), padding='valid'))
    #############################
    # # Pooling
    # model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='valid'))
    # Batch Normalisation before passing it to the next layer
    model.add(BatchNormalization())

    ##############add conv after 1st Conv#############
    model.add(Conv2D(filters=256, kernel_size=(
        3, 3), strides=(1, 1), padding='valid'))
    # model.add(Activation('relu'))
    model.add(Activation(swish))
    model.add(BatchNormalization())
    #####################################

    # 2nd Convolutional Layer
    model.add(Conv2D(filters=256, kernel_size=(
        3, 3), strides=(1, 1), padding='valid'))
    # model.add(Activation('relu'))
    model.add(Activation(swish))
    ######strided convolution instead of pool########
    model.add(Conv2D(filters=96, kernel_size=(
        3, 3), strides=(2, 2), padding='valid'))
    #############################
    # # Pooling
    # model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='valid'))
    # Batch Normalisation
    model.add(BatchNormalization())

    ##############add conv after 2nd conv#############
    model.add(Conv2D(filters=256, kernel_size=(
        3, 3), strides=(1, 1), padding='valid'))
    # model.add(Activation('relu'))
    model.add(Activation(swish))
    model.add(BatchNormalization())
    #################


    # 3rd Convolutional Layer
    model.add(Conv2D(filters=384, kernel_size=(
        3, 3), strides=(1, 1), padding='valid'))
    # model.add(Activation('relu'))
    model.add(Activation(swish))
    # Batch Normalisation
    model.add(BatchNormalization())

    ##############add conv after 3rd conv#############
    model.add(Conv2D(filters=384, kernel_size=(
        3, 3), strides=(1, 1), padding='valid'))
    # model.add(Activation('relu'))
    model.add(Activation(swish))
    model.add(BatchNormalization())
    #################


    # 4th Convolutional Layer
    model.add(Conv2D(filters=416, kernel_size=(
        3, 3), strides=(1, 1), padding='valid'))
    # model.add(Activation('relu'))
    model.add(Activation(swish))
    # Batch Normalisation
    model.add(BatchNormalization())



    # 5th Convolutional Layer
    model.add(Conv2D(filters=256, kernel_size=(
        3, 3), strides=(1, 1), padding='valid'))
    # model.add(Activation('relu'))
    model.add(Activation(swish))
    ######strided convolution instead of pool########
    model.add(Conv2D(filters=256, kernel_size=(
        3, 3), strides=(2, 2), padding='valid'))
    #############################
    # # Pooling
    # model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='valid'))
    # Batch Normalisation
    model.add(BatchNormalization())


    # Passing it to a dense layer
    model.add(Flatten())
    # 1st Dense Layer
    model.add(Dense(4096, input_shape=(294 * 523 * 3,)))
    model.add(Activation('relu'))
    # Add Dropout to prevent overfitting
    model.add(Dropout(0.4))
    # Batch Normalisation
    model.add(BatchNormalization())

    # 2nd Dense Layer
    model.add(Dense(4096))
    model.add(Activation('relu'))
    # Add Dropout
    model.add(Dropout(0.4))
    # Batch Normalisation
    model.add(BatchNormalization())

    # 3rd Dense Layer
    model.add(Dense(1000))
    model.add(Activation('relu'))
    # Add Dropout
    model.add(Dropout(0.4))
    # Batch Normalisation
    model.add(BatchNormalization())

    # Output Layer
    model.add(Dense(9))
    model.add(Activation('softmax'))

    model.summary()
    optimizer = Adam(lr=0.0001)
    #optimizer = Adam(lr=0.01)

    # (4) Compile
    model.compile(loss='categorical_crossentropy', optimizer=optimizer,
                  metrics=['accuracy'])
    return model

def alexnet():
    model = Sequential()
# 1st Convolutional Layer
    model.add(Conv2D(filters=96, input_shape=(294, 523, 1), kernel_size=(11, 11),
                     strides=(4, 4), padding='valid'))
    model.add(Activation('relu'))
    # Pooling
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='valid'))
    # Batch Normalisation before passing it to the next layer
    model.add(BatchNormalization())

    # 2nd Convolutional Layer
    model.add(Conv2D(filters=256, kernel_size=(
        11, 11), strides=(1, 1), padding='valid'))
    model.add(Activation('relu'))
    # Pooling
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='valid'))
    # Batch Normalisation
    model.add(BatchNormalization())

    # 3rd Convolutional Layer
    model.add(Conv2D(filters=384, kernel_size=(
        3, 3), strides=(1, 1), padding='valid'))
    model.add(Activation('relu'))
    # Batch Normalisation
    model.add(BatchNormalization())

    # 4th Convolutional Layer
    model.add(Conv2D(filters=384, kernel_size=(
        3, 3), strides=(1, 1), padding='valid'))
    model.add(Activation('relu'))
    # Batch Normalisation
    model.add(BatchNormalization())

    # 5th Convolutional Layer
    model.add(Conv2D(filters=256, kernel_size=(
        3, 3), strides=(1, 1), padding='valid'))
    model.add(Activation('relu'))
    # Pooling
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='valid'))
    # Batch Normalisation
    model.add(BatchNormalization())

    # Passing it to a dense layer
    model.add(Flatten())
    # 1st Dense Layer
    model.add(Dense(4096, input_shape=(294*523*3,)))
    model.add(Activation('relu'))
    # Add Dropout to prevent overfitting
    model.add(Dropout(0.4))
    # Batch Normalisation
    model.add(BatchNormalization())

    # 2nd Dense Layer
    model.add(Dense(4096))
    model.add(Activation('relu'))
    # Add Dropout
    model.add(Dropout(0.4))
    # Batch Normalisation
    model.add(BatchNormalization())

    # 3rd Dense Layer
    model.add(Dense(1000))
    model.add(Activation('relu'))
    # Add Dropout
    model.add(Dropout(0.4))
    # Batch Normalisation
    model.add(BatchNormalization())

    # Output Layer
    model.add(Dense(9))
    model.add(Activation('softmax'))

    model.summary()
    optimizer = Adam(lr=0.0001)

    # (4) Compile
    model.compile(loss='categorical_crossentropy', optimizer=optimizer,
                  metrics=['accuracy'])
    return model