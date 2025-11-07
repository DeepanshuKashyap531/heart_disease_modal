# CardioPredict Pro  
**AI-Powered Heart Disease Prediction System**  
**93% Accuracy** | Random Forest Classifier | Flask Web App

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3%2B-green?logo=flask&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3%2B-orange?logo=scikit-learn&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

> **Live Demo:** [https://cardiopredict-pro.onrender.com](https://heart-disease-modal.onrender.com/) *(deployed on Render)*

---

### Project Overview
**CardioPredict Pro** is an intelligent web application that predicts the **risk of heart disease** using **11 clinical features** with **93% accuracy**.

Built using **Random Forest Classifier** on the **UCI Heart Disease Dataset**, this tool helps in early detection and serves as a **powerful educational & portfolio project**.

---

### Model Performance

```text
Model Accuracy: 92.93%

```
### Classification Report

```

              precision    recall  f1-score   support
           
       0       0.97      0.88      0.92        89
       1       0.89      0.98      0.93        95

    accuracy                          0.93       184
   macro avg     0.93      0.93      0.93       184
weighted avg     0.93      0.93      0.93       184



Sensitivity (Recall for Disease): 98%
Specificity: 88%
Precision (Positive Predictive Value): 89%
F1-Score: 0.93 (Excellent balance)

```

### Features Used

1. Age                  → Patient age in years
2. Sex                  → M (1), F (0)
3. ChestPainType        → TA, ATA, NAP, ASY
4. RestingBP            → Resting blood pressure (mm Hg)
5. Cholesterol          → Serum cholesterol (mg/dl)
6. FastingBS            → Fasting blood sugar > 120 mg/dl (1 = Yes)
7. RestingECG           → Normal, ST, LVH
8. MaxHR                → Maximum heart rate achieved
9. ExerciseAngina       → Y (1), N (0)
10. Oldpeak             → ST depression value
11. ST_Slope            → Up, Flat, Down


## Tech Stack
yamlLanguage: Python 3.9+
Framework: Flask
ML Library: scikit-learn
Frontend: HTML5, Bootstrap 5, Font Awesome
Deployment: Render (Free Tier)
Model: RandomForestClassifier() → model.pkl

##Project Structure

textCardioPredict-Pro/
├── app.py                  # Flask backend + prediction logic
├── model.pkl               # Trained Random Forest model
├── templates/
│   └── index.html          # Responsive UI with sound effects
├── requirements.txt
├── README.md               # This file
└── .gitignore

##How to Run Locally

bash# 1. Clone the repository
git clone https://github.com/DeepanshuKashyap02/CardioPredict-Pro.git
cd CardioPredict-Pro

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
Open browser → http://127.0.0.1:5000

## Features

Real-time prediction with 93% accuracy
Professional medical UI (clean, responsive, mobile-friendly)
Heartbeat sound effect on "About Model" click
Beating heart animation
Detailed model documentation modal
GitHub + Portfolio links in navbar & footer
Copyright © Deepanshu Kashyap

## Clean, professional interface trusted by healthcare standards

## Deployment (Free Forever)
Deployed on Render.com in under 2 minutes:
bashrender.com → New Web Service → Connect GitHub Repo → Deploy

## Developer & ML engenieer Enthusiast
Name: Deepanshu Kashyap

Role: Machine Learning Engineer & Full-Stack Developer

Location: Maharashtra, India

GitHub: https://github.com/DeepanshuKashyap02

Portfolio: https://mywebsite700.vercel.app/

LinkedIn: https://linkedin.com/in/deepanshukashyap02

Email: deepanshukashyap02@gmail.com

## Disclaimer

This project is for educational and portfolio purposes only.
It is not intended for actual medical diagnosis. Always consult a qualified doctor.

## Star this Project!

If you like this work, please give it a star on GitHub!

Built with passion, precision, and purpose.
© 2025 Deepanshu Kashyap. All rights reserved.

### Tech Stack

Backend:     Python + Flask
Frontend:    HTML5 + Bootstrap 5 + Font Awesome
ML Model:    RandomForestClassifier (scikit-learn)
Deployment:  Render / Railway / PythonAnywhere
Dataset:     UCI Heart Disease Dataset

