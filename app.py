import pickle
import numpy as np
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Load model
model = pickle.load(open('heart_disease_model.pkl', 'rb'))

# Column order (MUST match training)
columns = [
    'Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS',
    'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope'
]

# Mappings
sex_map = {'M': 1, 'F': 0}
chest_pain_map = {'TA': 0, 'ATA': 1, 'NAP': 2, 'ASY': 3}
resting_ecg_map = {'Normal': 0, 'ST': 1, 'LVH': 2}
exercise_angina_map = {'Y': 1, 'N': 0}
st_slope_map = {'Up': 2, 'Flat': 1, 'Down': 0}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    result_class = ""

    if request.method == 'POST':
        try:
            data = {
                'Age': float(request.form['Age']),
                'Sex': sex_map[request.form['Sex']],
                'ChestPainType': chest_pain_map[request.form['ChestPainType']],
                'RestingBP': float(request.form['RestingBP']),
                'Cholesterol': float(request.form['Cholesterol']),
                'FastingBS': int(request.form['FastingBS']),
                'RestingECG': resting_ecg_map[request.form['RestingECG']],
                'MaxHR': float(request.form['MaxHR']),
                'ExerciseAngina': exercise_angina_map[request.form['ExerciseAngina']],
                'Oldpeak': float(request.form['Oldpeak']),
                'ST_Slope': st_slope_map[request.form['ST_Slope']]
            }

            input_df = pd.DataFrame([data], columns=columns)
            prediction = model.predict(input_df)[0]

            if prediction == 1:
                result = "This person gives the sign of heart disease."
                result_class = "alert-danger"
            else:
                result = "According to model analysis, this person is most likely okay."
                result_class = "alert-success"

        except Exception as e:
            result = f"Error: {str(e)}"
            result_class = "alert-warning"

    return render_template('index.html', result=result, result_class=result_class)

if __name__ == '__main__':
    app.run(debug=True)