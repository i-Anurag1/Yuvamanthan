# Import the required functions/Libraries 

import cv2
from keras.models import load_model	
from make_predictions import prediction


#Make function to predict each video

def detective(path, model):

	#Check if the file is in the correct format

	if path[:4] == '.mp4' or '.avi':
		pass
	else:
		return 'Error: Unsupported file format. Only .mp4/.avi files are allowed.'

	cap = cv2.VideoCapture(path) #Get the path of the video and open it

	c = 0 #Make a variable to increase everytime we work on a frame

	predictions = [] #List to store our predictions for every frame we worked on

	while(cap.isOpened()): 
		ret, frame = cap.read()
		if ret == False:
			break

		if c % 5 == 0: #Apply this every 5 frames instead of all frames so as to save compute and time
			frame = cv2.resize(frame, (224, 224)) #Resize the frame
			predictions.append(prediction(frame, model)) #Predict the frame and append to our list
		else:
			pass

		c+=1 #Increment c

	accident = 0 #variable to record the number of accident images found
	fire = 0 #variable to record the number of fire images found

	for i in predictions: #Iterate through each value in predictions and increment the respective variables
		if i == 'accident':
			accident+=1
		elif i == 'fire':
			fire+=1
		else:
			pass

	#If the model detects something irregular more than 2 times, then return the output. This is to prevent false positives

	if accident >= 2:
		return 'Result: Accident detected'
	elif fire >= 2:
		return 'Result: Fire detected'
	else:
		return 'Result: No accident detected'
