# -*- coding: utf-8 -*-
"""MNIST_(Deep_Learning_with_Python).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DaMQTsJlF9jRhAtejvTQnNQc3zussmbb

# **Importing Libraries**
"""

from tensorflow.keras.datasets import mnist

"""# **Loading Data**"""

(train_images, train_labels) , (test_images, test_labels) = mnist.load_data()

train_images.shape , train_labels.shape , test_images.shape , test_labels.shape

from keras import models
from keras import layers

"""# **Building the Model Section**"""

model = models.Sequential()
model.add(layers.Dense(512,activation = 'relu',input_shape = (28*28,)))
model.add(layers.Dense(10,activation = 'softmax'))

"""# **Compiling the model before training**"""

model.compile(optimizer='rmsprop',
              loss = 'sparse_categorical_crossentropy',
              metrics = ['accuracy'])

"""# **Reshaping Train Images**"""

train_images = train_images.reshape((60000,28*28))
train_images = train_images.astype('float32')/255

"""# **Reshaping Test Images**"""

test_images = test_images.reshape((10000,28*28))
test_images = test_images.astype('float32')/255

"""# **Training the Model**"""

result=model.fit(train_images,train_labels,batch_size=128,epochs=10)

"""# Plotting the Graph"""

#Plot the accuracy and loss graphs

import matplotlib.pyplot as plt


def plot_acc_loss(result, epochs):
    acc = result.history['accuracy']
    loss = result.history['loss']
    #val_acc = result.history['val_accuracy']
    #val_loss = result.history['val_loss']
    plt.figure(figsize=(15, 5))
    plt.subplot(121)
    # plt.plot(range(1,epochs), acc[1:], label='Train_accuracy')
    # plt.plot(range(1,epochs), val_acc[1:], label='Val_accuracy')
    plt.plot(acc, label='Train_accuracy')
    #plt.plot(val_acc, label='Val_accuracy')


    plt.title('Accuracy over ' + str(epochs) + ' Epochs', size=15)
    plt.legend()
    plt.grid(True)
    plt.subplot(122)
    # plt.plot(range(1,epochs), loss[1:], label='Train_loss')
    # plt.plot(range(1,epochs), val_loss[1:], label='Val_loss')
    plt.plot(loss, label='Train_loss')
    #plt.plot(val_loss, label='Val_loss')


    plt.title('Loss over ' + str(epochs) + ' Epochs', size=15)
    plt.legend()
    plt.grid(True)
    plt.show()
    
plot_acc_loss(result, 10)

model.summary()

model.evaluate(test_images,test_labels)

train_labels[0]

test_labels[0]

model.predict(test_images)

