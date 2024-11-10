#Load in all the libraries

from keras.preprocessing.image import load_img, img_to_array  
from keras.models import load_model
from numpy import argmax


model = load_model('model.h5') #Load in the model


def prediction(img, model): #Make a function to predict an image to test this model

	classes = ['accident', 'dense_traffic', 'fire', 'sparse_traffic'] #Make a list of the classes
	# img = img.resize((224, 224)) #Resize image
	img = img_to_array(img) #Convert into an array
	img = img.reshape(-1, 224, 224,3) #Reshape it

	pred = model.predict(img) #Predict the image

	return classes[int(argmax(pred, axis=1))] #Return the classified labels
