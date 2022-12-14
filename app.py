from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)  # Initialize the flask App
model = pickle.load(open('models/model_LR.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/predict', methods=['POST'])
def predict():
    distance = float(request.form['distance'])
    surge = float(request.form['surge'])
    ride = int(request.form['ride'])

    val = [distance, surge]

    ride_types = {0: 0,
                  1: 1,
                  2: 2,
                  3: 3,
                  4: 4,
                  5: 5,
                  6: 6,
                  7: 7,
                  8: 8,
                  9: 9,
                  10: 10,
                  11: 11,
                  12: 12}

    for i in range(0, 13):
        if ride_types[ride] == i:
            val.append(1.0)
        else:
            val.append(0.0)

    prediction = model.predict([val])
    output = round(prediction[0], 2)
    return render_template("main.html", prediction=output)


if __name__ == "__main__":
    app.run(debug=True)