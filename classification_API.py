import numpy as np
from flask import Flask, request, jsonify, render_template
from api_functions import read_Image, preprocess, prediction


app = Flask(__name__)



@app.route('/home/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['GET','POST'])
def predict():

	if request.method == 'POST':

		base64_file = request.form.get("myfile")

		img = read_Image(base64_file)

		preprocessed_image = preprocess(img)

		prediction_ = prediction(preprocessed_image)

		pred_res = {'Score' : prediction_[0], 'Breed' : prediction_[1]}

		return render_template('display.html', prediction='prediction results : {}'.format(pred_res))

	else:

		return render_template('index.html')
	

if __name__ == "__main__":

    app.run(debug=True)


