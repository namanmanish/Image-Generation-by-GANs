%matplotlib inline
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


classifier = Sequential()

classifier.add(Conv2D(32, (3, 3), input_shape = (32, 32, 3), activation = 'relu'))

classifier.add(MaxPooling2D(pool_size = (2, 2)))

classifier.add(Conv2D(32, (3, 3), activation = 'relu'))

classifier.add(MaxPooling2D(pool_size = (2, 2)))

classifier.add(Flatten())

classifier.add(Dense(units = 128, activation = 'relu'))

classifier.add(Dense(units = 1, activation = 'sigmoid'))

classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

#taken from Keras Image Preprocessing
train_datagen = ImageDataGenerator(rescale = 1./255,
shear_range = 0.2,
zoom_range = 0.2,
horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('dataset/training_set',
target_size = (32, 32),
batch_size = 32,
class_mode = 'binary')

test_set = test_datagen.flow_from_directory('dataset/test_set',
target_size = (32, 32),
batch_size = 32,
class_mode = 'binary')

classifier.fit_generator(training_set,
steps_per_epoch = 1000,
epochs = 3,
validation_data = test_set,
validation_steps = 2)

#predicting from single_prediction
import numpy as np
from keras.preprocessing import image
test_image = image.load_img('dataset/single_prediction/face_191.jpg', target_size = (32, 32))

test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices
if result[0][0] == 1:
    prediction = 'woman'
else:
    prediction = 'man'
    
print("Given Image is:",prediction)



img = mpimg.imread('dataset/single_prediction/face_191.jpg')
imgplot = plt.imshow(img)
