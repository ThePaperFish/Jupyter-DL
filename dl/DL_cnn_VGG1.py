#Own
import sub_direct as s

#Keras
import keras

from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, BatchNormalization
from keras.layers import Conv2D, MaxPooling2D

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16

import numpy as np
from sklearn.utils import shuffle

def load_image():
#load path
	path = ".\\dataset\\test1"
	list = s.loop_images(path)
	
#load label
	label = []
	temp = s.loop_dir(path)
	for i in range(len(temp)):
		label += [(i)] * len(s.loop_images(temp[i], 0))
		
	#one hot
	label = keras.utils.to_categorical(np.array(label), len(temp))
	
#load image
	list = [load_img(i, target_size=(224, 224)) for i in list]
	list = np.array([img_to_array(i) for i in list])
	list = preprocess_input(list)
	
	return np.array(list),np.array(label)
	
def load_model():
	input_shape = (224, 224, 3)
	model = Sequential()
	
	model.add(Conv2D(64, kernel_size=(3, 3),activation='relu',padding='same',input_shape=input_shape))
	model.add(Conv2D(64, kernel_size=(3, 3),activation='relu',padding='same'))
	model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
	
	model.add(Conv2D(128, kernel_size=(3, 3),activation='relu',padding='same'))
	model.add(Conv2D(128, kernel_size=(3, 3),activation='relu',padding='same'))
	model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
	
	# model.add(Conv2D(256, kernel_size=(3, 3),activation='relu',padding='same'))
	# model.add(Conv2D(256, kernel_size=(3, 3),activation='relu',padding='same'))
	# model.add(Conv2D(256, kernel_size=(3, 3),activation='relu',padding='same'))
	# model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
	
	# model.add(Conv2D(512, kernel_size=(3, 3),activation='relu',padding='same'))
	# model.add(Conv2D(512, kernel_size=(3, 3),activation='relu',padding='same'))
	# model.add(Conv2D(512, kernel_size=(3, 3),activation='relu',padding='same'))
	# model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
	
	# model.add(Conv2D(512, kernel_size=(3, 3),activation='relu',padding='same'))
	# model.add(Conv2D(512, kernel_size=(3, 3),activation='relu',padding='same'))
	# model.add(Conv2D(512, kernel_size=(3, 3),activation='relu',padding='same'))
	# model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
	
	#model.load_weights('model_w\\vgg16_weight.h5')

	model.add(Flatten())
	model.add(Dense(1024, activation='relu'))
	model.add(Dense(512, activation='relu'))
	model.add(Dense(10, activation='softmax'))
	
	return model

# load_image
data_in, data_out = load_image()
#data_in, data_out = shuffle(data_in, data_out)

temp = 800
train_x, train_y = data_in[:temp], data_out[:temp]
test_x, test_y = data_in[temp:], data_out[temp:]

# load the model
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(loss=keras.losses.categorical_crossentropy,
    optimizer='adam', metrics=['accuracy'])

# Train Model
model.fit(train_x, train_y,
	batch_size=20,  epochs=10,  verbose=2,
	validation_data=(train_x, train_y))
	
model.evaluate(test_x, test_y, verbose=0)

model.save_weights('model_w\\test.h5')


















