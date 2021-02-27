import cv2
import numpy as np
import pandas as pd
import keras
import base64
from PIL import Image
from io import BytesIO
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

def load_model():

	_load_model = keras.models.load_model(r"C:\Users\User\Desktop\jiko\resnet_50") #change saved model location as per need.

	return _load_model

model = load_model()


def read_Image(file):

	f = open(file, 'r')
	data = f.read()
	f.closed

	im = Image.open(BytesIO(base64.b64decode(data)))

	return im


def preprocess(image):

	images = []

	image_data = np.asarray(image)

	img_ = cv2.resize(image_data, (224,224))

	images.append(img_)

	x_test = np.array(images, dtype='float64')

	return x_test




def prediction(array_):

	train_df = pd.read_csv(r'C:\Users\User\Desktop\jiko\dog-breed-identification\labels.csv')

	'''
	Labelizing labels.
	'''
	y = train_df['breed'][0:3452].values

	target_ = LabelEncoder()

	y = target_.fit_transform(y)

	labels_ = list(target_.classes_)




	'''
		Prediction
	'''
	predictions = model.predict(array_)

	print(predictions)
	max_prob = np.argmax(predictions,axis=1)

	list_ = [predictions[0][max_prob[0]], labels_[max_prob[0]] ]

	return list_


