from flask import Flask, redirect, render_template, url_for, request
import numpy as np
import datetime
from joblib import load
import sklearn

app = Flask(__name__)


@app.route('/')
def home():

    current_year = datetime.datetime.now()

    return render_template('home.html', current_year=current_year)


@app.route('/doc', methods=["GET"])
def help_doc():

    return render_template('help_doc.html')


@app.route('/form', methods=['POST'])
def form_access():

    age = int(request.form['age'])
    mean_value_age = 54.42
    std_for_age = 9.05
    val_1 = (age - mean_value_age)/std_for_age

    sex = request.form['sex']
    if sex == "male":
        val_2 = 1
    elif sex == "female":
        val_2 = 0

    trestbps = int(request.form["trestbps"])
    mean_value_trestbps = 130.07
    std_trestbps = 15.15
    val_3 = (trestbps - mean_value_trestbps)/std_trestbps

    chol = int(request.form["chol"])
    mean_value_chol = 243.23
    std_chol = 44.62
    val_4 = (chol-mean_value_chol)/std_chol

    val_5 = int(request.form["fbs"])

    thalach = int(request.form["thalach"])
    mean_value_thalach = 149.84
    std_thalach = 22.45
    val_6 = (thalach - mean_value_thalach)/std_thalach

    val_7 = int(request.form["fbs"])

    oldpeak = float(request.form["oldpeak"])
    mean_value_oldpeak = 0.97
    std_oldpeak = 1.04
    val_8 = (oldpeak-mean_value_oldpeak)/std_oldpeak

    cp = int(request.form["cp"])
    if cp == 0:
        val_9, val_10, val_11 = 0, 0, 0
    elif cp == 1:
        val_9, val_10, val_11 = 1, 0, 0
    elif cp == 2:
        val_9, val_10, val_11 = 0, 1, 0
    else:
        val_9, val_10, val_11 = 0, 0, 1

    ca = int(request.form["ca"])
    if ca == 0:
        val_12, val_13, val_14, val_15 = 0, 0, 0, 0
    elif ca == 1:
        val_12, val_13, val_14, val_15 = 1, 0, 0, 0
    elif ca == 2:
        val_12, val_13, val_14, val_15 = 0, 1, 0, 0
    elif ca == 3:
        val_12, val_13, val_14, val_15 = 0, 0, 1, 0
    else:
        val_12, val_13, val_14, val_15 = 0, 0, 0, 1

    restecg = int(request.form["restecg"])
    if restecg == 0:
        val_16, val_17 = 0, 0
    elif restecg == 1:
        val_16, val_17 = 1, 0
    else:
        val_16, val_17 = 0, 1

    slope = int(request.form["slope"])
    if slope == 0:
        val_18, val_19 = 0, 0
    elif slope == 1:
        val_18, val_19 = 1, 0
    else:
        val_18, val_19 = 0, 1

    thal = int(request.form["thal"])
    if thal == 0:
        val_20, val_21, val_22 = 0, 0, 0
    elif thal == 1:
        val_20, val_21, val_22 = 1, 0, 0
    elif thal == 2:
        val_20, val_21, val_22 = 0, 1, 0
    else:
        val_20, val_21, val_22 = 0, 0, 1

    features_array = np.array([val_1, val_2, val_3, val_4, val_5, val_6, val_7, val_8, val_9, val_10, val_11, val_12, val_13, val_14, val_15, val_16, val_17, val_18, val_19, val_20, val_21, val_22])
    array = features_array.reshape(1, -1)
    model = load("model.joblib")
    preds = model.predict(array)

    return render_template('prediction.html', age=age, sex=sex, preds=preds)


if __name__ == "__main__":
    app.run(debug=True)
