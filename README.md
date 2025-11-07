# heart_disease_modal

# CardioPredict Pro  
**AI-Powered Heart Disease Prediction System**  
**93% Accuracy** | Random Forest Classifier | Flask Web App

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3%2B-green?logo=flask&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3%2B-orange?logo=scikit-learn&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

> **Live Demo:** [https://cardiopredict-pro.onrender.com](https://cardiopredict-pro.onrender.com) *(deployed on Render)*

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

              precision    recall  f1-score   support
           
       0       0.97      0.88      0.92        89
       1       0.89      0.98      0.93        95

    accuracy                          0.93       184
   macro avg     0.93      0.93      0.93       184
weighted avg     0.93      0.93      0.93       184



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

### Tech Stack

Backend:     Python + Flask
Frontend:    HTML5 + Bootstrap 5 + Font Awesome
ML Model:    RandomForestClassifier (scikit-learn)
Deployment:  Render / Railway / PythonAnywhere
Dataset:     UCI Heart Disease Dataset

