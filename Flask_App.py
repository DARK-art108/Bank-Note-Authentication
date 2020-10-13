# This file is a raw flask implementation test it using Postman

from flask import Flask, render_template, redirect, request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)


@app.route("/")
def predict_note_authentication():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    return "The predicted values is " + str(prediction)


@app.route("/predict_file", methods=["POST"])
def predict_file():
    df_test = pd.read_csv(request.files.get('file'))
    prediction = classifier.predict(df_test)
    return "The predicted values for the csv is " + str(list(prediction))


if __name__ == '__main__':
    app.run()

