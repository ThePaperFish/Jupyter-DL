import tensorflow as tf
import numpy as np

from time import time
from tensorflow import keras
from keras.callbacks import TensorBoard

with np.load('dataset\\mnist.npz') as f:
	(x_train, y_train) = f['x_train'],f['y_train']
	(x_test, y_test) = f['x_test'],f['y_test']
	
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

tensorboard = TensorBoard(log_dir='logs/{}'.format(time()))

model.compile(optimizer=tf.keras.optimizers.SGD(0.01,0.01),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=1, callbacks=[tensorboard])
model.evaluate(x_test, y_test)