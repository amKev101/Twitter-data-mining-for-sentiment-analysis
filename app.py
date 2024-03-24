import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

#Create flask application
app = Flask(__name__)

#Load the pickle model from model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", method = [POST])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)   

    return render_template("index.html", prediction_text = "The lfower species is {}".format(prediction))

 