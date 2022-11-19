# -*- coding: utf-8 -*-
"""CIFAR10_FUNCTIONAL_MLP AND CNN

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/111ttAw2BmOkd_86WsPjZnWzGIO8PZEC9

#MLP and CNN ON CIFAR10 DATASET USING FUNCTIONAL MODEL

CIFAR-10 DATASET

#MLP FUNCTIONAL MODEL
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.utils import to_categorical, plot_model
from tensorflow.keras.datasets import cifar10

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

len(x_train)

len(x_test)

#reshaping
x_train = x_train.reshape(50000, 32 * 32 * 3)
x_test = x_test.reshape(10000, 32 * 32 * 3)
#normalising values between 0-1
#normalizing between 0-1
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

#num of labels
num_labels = len(np.unique(y_train))

# One Hot Encoding 
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

#NETWORK PARAMETERS
batch_size = 128
hidden_units = 512
dropout = 0.40

#from tensorflow.keras import layers
from tensorflow.keras.layers import Dense, Dropout, Input
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.models import Model
#inp=(28,28)
input_layer=Input (shape=(32*32*3), )
#input_layer=Input(shape=inp)
x= Dense(56, activation='relu') (input_layer)
x= Dense(112, activation='relu')(x)
x= Dense (240, activation='relu') (x)
x=Dense(150, activation='relu') (x)
x=Dense(10, activation='softmax') (x)
model=Model (input_layer, x)

model.summary()
plot_model(model, to_file='mlp-cifar10.png', show_shapes=True)

model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
# train the network
model.fit(x_train, y_train, epochs=5, batch_size=batch_size)

_, acc = model.evaluate(x_test,
                        y_test,
                        batch_size=batch_size,
                        verbose=0)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))

"""#CNN USING FUNCTIONAL MODEL"""

import tensorflow as tf
import pandas as pd
from tensorflow.keras.layers import Input, Conv2D, Dense, Flatten, Dropout, MaxPooling2D, BatchNormalization
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

#reshaping
x_train = x_train.reshape(-1, 32,32, 3)
x_test = x_test.reshape(-1, 32,32, 3)

#normalizing between 0-1
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

#one-hot encoding
num_labels = len(np.unique(y_train))
num_labels

#y_train = to_categorical(y_train)
#y_test = to_categorical(y_test)

i = Input(shape = x_train[0].shape)
x = Conv2D(32, (3,3), padding="same", activation="relu")(i)
x = Conv2D(32, (3,3), activation="relu")(x)
x = MaxPooling2D(pool_size=(2,2))(x)
x = Dropout(0.30)(x)
x = Conv2D(64, (3,3), padding="same", activation="relu")(x)
x = Conv2D(64, (3,3), activation="relu")(x)
x = MaxPooling2D(pool_size=(2,2))(x)
x = Dropout(0.30)(x)
x = BatchNormalization()(x)
x = Flatten()(x)
x = Dense(512, activation="relu")(x)
x = Dropout(0.5)(x)
x = Dense(num_labels, activation="softmax")(x)

model = Model(i, x)

model.summary()
plot_model(model, to_file='mlp-cifar10.png', show_shapes=True)

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=10)

# validate the model on test dataset to determine generalization
_, acc = model.evaluate(x_test,y_test,batch_size=batch_size,verbose=0)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))

# Commented out IPython magic to ensure Python compatibility.
# %%shell
# jupyter nbconvert --to html /content/CIFAR10_FUNCTIONAL_MLP_AND_CNN.ipynb