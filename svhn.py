import tensorflow as tf
import numpy as np
from scipy.io import loadmat
import scipy
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers
from sklearn.metrics import f1_score
import os.path
import subprocess, datetime
import cv2

# loading data
def loading_data():

    # First, download dataset (train and test)
    # check in current folder
    if (os.path.exists('train_32x32.mat')):
        print("train_32x32.mat exists")
    else:
        subprocess.run(['wget', '-P', 'http://ufldl.stanford.edu/housenumbers/train_32x32.mat'])
        
    if (os.path.exists('test_32x32.mat')):
        print("test_32x32.mat exists")
    else:
        subprocess.run(['wget', '-P', 'http://ufldl.stanford.edu/housenumbers/test_32x32.mat'])
        
    # Loading data from mat file
    X_train = loadmat('train_32x32.mat')["X"]
    y_train = loadmat('train_32x32.mat')["y"]
    X_test = loadmat('test_32x32.mat')["X"]
    y_test = loadmat('test_32x32.mat')["y"]

    # Normalization
    X_train, X_test = X_train / 255.0, X_test / 255.0

    # Relabel 10 to 0
    y_train[y_train==10] = 0
    y_test[y_test==10] = 0

    # Reshape arrays (#samples, width, height, channel)
    X_train = X_train.transpose((3, 0, 1, 2))
    X_test = X_test.transpose((3, 0, 1, 2))

    # Split origin train set into train set and validation set (10%)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.1)

    return X_train, X_test, X_val, y_train, y_test, y_val

# define models
def create_model(model_choice='A'): 
    
    # sequential model
    model = tf.keras.Sequential()

    if model_choice == 'A':
        model.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, padding='same', activation='relu', input_shape=(32,32,3)))
        model.add(layers.BatchNormalization())
        model.add(tf.keras.layers.MaxPooling2D(pool_size=2, padding='same'))
        model.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, padding='same', activation='relu'))
        model.add(layers.BatchNormalization())    
        model.add(tf.keras.layers.MaxPooling2D(pool_size=2, padding='same'))

        model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=3, padding='same', activation='relu'))
        model.add(layers.BatchNormalization()) 
        model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=3, padding='same', activation='relu'))
        model.add(layers.BatchNormalization())    
        model.add(tf.keras.layers.MaxPooling2D(pool_size=2, padding='same'))

        model.add(tf.keras.layers.Conv2D(filters=128, kernel_size=3, padding='same', activation='relu'))
        model.add(layers.BatchNormalization()) 
        model.add(tf.keras.layers.Conv2D(filters=128, kernel_size=3, padding='same', activation='relu'))
        model.add(layers.BatchNormalization())    
        model.add(tf.keras.layers.MaxPooling2D(pool_size=2, padding='same'))             
 

    elif model_choice == 'B':
        model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=3, padding='same', activation='relu', input_shape=(32,32,3)))
        model.add(layers.BatchNormalization())
        model.add(tf.keras.layers.MaxPooling2D(pool_size=2, padding='same'))
        model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=3, padding='same', activation='relu'))
        model.add(layers.BatchNormalization())    
        model.add(tf.keras.layers.MaxPooling2D(pool_size=2, padding='same'))

        model.add(tf.keras.layers.Conv2D(filters=128, kernel_size=3, padding='same', activation='relu'))
        model.add(layers.BatchNormalization()) 
        model.add(tf.keras.layers.Conv2D(filters=128, kernel_size=3, padding='same', activation='relu'))
        model.add(layers.BatchNormalization())    
        model.add(tf.keras.layers.MaxPooling2D(pool_size=2, padding='same'))

        model.add(tf.keras.layers.Conv2D(filters=256, kernel_size=3, padding='same', activation='relu'))
        model.add(layers.BatchNormalization()) 
        model.add(tf.keras.layers.Conv2D(filters=256, kernel_size=3, padding='same', activation='relu'))
        model.add(layers.BatchNormalization())    
        model.add(tf.keras.layers.MaxPooling2D(pool_size=2, padding='same'))              


    elif model_choice == 'C':
        model.add(layers.Conv2D(64, kernel_size=(3,3), padding='same', input_shape=(32,32,3), activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.Conv2D(64, kernel_size=(3,3), padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.MaxPool2D(pool_size=(2, 2), padding='same'))

        model.add(layers.Conv2D(128, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.Conv2D(128, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.MaxPool2D(pool_size=(2, 2), padding='same'))

        model.add(layers.Conv2D(256, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.Conv2D(256, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.MaxPool2D(pool_size=(2, 2), padding='same'))

        model.add(layers.Conv2D(512, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.Conv2D(512, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.MaxPool2D(pool_size=(2, 2), padding='same'))

        model.add(layers.Conv2D(512, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.Conv2D(512, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.MaxPool2D(pool_size=(2, 2), padding='same'))        
    

    elif model_choice == 'D':
        model.add(layers.Conv2D(64, kernel_size=(3,3), padding='same', input_shape=(32,32,3), activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.Conv2D(64, kernel_size=(3,3), padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.MaxPool2D(pool_size=(2, 2), padding='same'))

        model.add(layers.Conv2D(128, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.Conv2D(128, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.MaxPool2D(pool_size=(2, 2), padding='same'))

        model.add(layers.Conv2D(256, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.Conv2D(256, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.Conv2D(256, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.MaxPool2D(pool_size=(2, 2), padding='same'))

        model.add(layers.Conv2D(512, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.Conv2D(512, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.Conv2D(512, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.MaxPool2D(pool_size=(2, 2), padding='same'))

        model.add(layers.Conv2D(512, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.Conv2D(512, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.Conv2D(512, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.MaxPool2D(pool_size=(2, 2), padding='same'))

    else:
        raise ValueError("Invalid model.")


    model.add(layers.Flatten())
    model.add(layers.Dense(4096, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(2048, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(10, activation='softmax'))

    # Check model details
    model.summary()
    
    # Compile model
    model.compile(optimizer=tf.keras.optimizers.Adam(),
                    loss = 'sparse_categorical_crossentropy',
                    metrics=['accuracy'])
    return model


def traintest():
    # Loading train and test data
    X_train, X_test, X_val, y_train, y_test, y_val = loading_data()
    
    # Train : Test : Validation = 65931 : 26032 : 7326
    '''
    Train data shape:  (65931, 32, 32, 3)
    Test data shape:  (26032, 32, 32, 3)
    Validation data shape:  (7326, 32, 32, 3)
    label_train shape:  (65931, 1)
    label_test shape:  (26032, 1)
    label_validation shape:  (7326, 1)
    '''
    print('Train data shape: ', X_train.shape)
    print('Test data shape: ', X_test.shape)
    print('Validation data shape: ', X_val.shape)
    print('label_train shape: ', y_train.shape)
    print('label_test shape: ', y_test.shape)
    print('label_validation shape: ', y_val.shape)

    # choose the type of model to train
    model_choice = 'A'
    #model_choice = 'B'
    #model_choice = 'C'
    #model_choice = 'D'

    # create model
    model = create_model(model_choice)

    # Callback: Save the model.
    checkpointer = tf.keras.callbacks.ModelCheckpoint(
        filepath=os.path.join('.', 'checkpoints', model_choice+'-best-v6.h5'),
        verbose=1,
        save_best_only=True)

    # Callback: Stop when we stop learning.
    early_stopper = tf.keras.callbacks.EarlyStopping(patience=5, monitor='val_loss')

    # Callback: TensorBoard
    log_dir = os.path.join('.', 'logs', model_choice+'-'+datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir)

    # Callback: CSVLogger
    csv_logger = tf.keras.callbacks.CSVLogger(os.path.join(log_dir, model_choice+'-'+datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+'.log'))
    
    # Training
    model.fit(X_train,
              y_train,
              epochs=30,
              batch_size=128,
              validation_data=(X_val, y_val),
              callbacks=[early_stopper, checkpointer, tensorboard_callback, csv_logger],
              verbose=2)

    # predict labels for testing set
    y_predict = model.predict_classes(X_test, batch_size=128)
    # average F1 scores across each class
    average_f1 = f1_score(y_test, y_predict, average='weighted')
    return average_f1


# Predict a single image
def test(image):

    # Load model
    model_path = 'model-best.h5'
    saved_model = tf.keras.models.load_model(model_path)

    # read image and resize images to 32*32, and also norm   
    img = np.reshape((cv2.resize(cv2.imread(image,3),(32,32))) / 255.0, [1,32,32,3])
    # predict
    output = saved_model.predict_classes(img)
    return output

# main function
if __name__ == '__main__':
    average_f1 = traintest()
    print("f1_score: ", average_f1)

