### Diabetes Prediction Model and Web App

### Project Overview

This repository contains a Diabetes Prediction Model and a Streamlit Web App designed to predict diabetes risk using a well-known health dataset. The project combines exploratory data analysis (EDA), machine learning model comparison, and a user-friendly web interface to deliver actionable insights and predictions. It demonstrates skills in data preprocessing, classification, visualization, and web deployment—ideal for showcasing data science proficiency.

### Dataset:
Source: Diabetes Prediction Dataset on Kaggle  

Size: 768 rows, 9 columns  

Features:  
-Age: Age of the individual (years)  

-Gender: Gender of the individual (binary)  

-Body Mass Index (BMI): Measure of body fat based on height and weight  

-Blood Pressure: Diastolic blood pressure (mmHg)  

-Insulin Level: 2-hour serum insulin (mu U/ml)  

-Skin Thickness: Triceps skin fold thickness (mm)  

-Glucose Level: Plasma glucose concentration (mg/dl)  

-Diabetes Pedigree Function: Genetic diabetes risk score  

-Number of Pregnancies: Number of times pregnant

-Target: Outcome (0 = No Diabetes, 1 = Diabetes)  

Purpose: These features capture physiological and genetic factors critical for predicting diabetes likelihood.

### Workflow:
### Exploratory Data Analysis (EDA):  
-Inspected data structure, distributions, and class balance using pandas, seaborn, and matplotlib.  

### Key findings: 
-Glucose and BMI show significant variance; dataset is imbalanced (more non-diabetic cases).

### Preprocessing:  
-Standardized column names (str.lower()).  

-Scaled features with RobustScaler to handle outliers.  

-Split data into 70% training and 30% testing sets (train_test_split).

### Modeling:  
Tested five classifiers from sklearn:  
-Random Forest (n_estimators=200, max_depth=5)  

-K-Nearest Neighbors (n_neighbors=7)  

-Support Vector Machine (SVM)  

-Logistic Regression (max_iter=200)  

-Gradient Boosting (n_estimators=50, max_depth=5)

-Evaluated with accuracy, precision, recall, and F1-score due to class imbalance.

### Visualization:  
-Distribution plots for numerical features.  

-Count plot for outcome balance.  

-Bar chart comparing model performance with accuracy labels.

### Model Deployment:  
-Saved the best-performing model (Random Forest) using pickle for integration into the web app.

### Web App:  
-Built an interactive Streamlit application to allow users to input health data and receive diabetes risk predictions.  

### Live Demo: 
[Diabetes Web App](https://diabetes-web-app-007.streamlit.app/)



### Key Insights:
Feature Importance:
- Random Forest identified Glucose Level and BMI as top predictors of diabetes risk.  

### Model Performance:
- Random Forest achieved ~75% accuracy, with balanced precision/recall (F1 ~0.70), outperforming others due to its robustness to imbalanced data.  

### EDA Highlights: 
-Higher glucose levels and BMI correlate strongly with positive diabetes outcomes (correlation heatmap analysis).

### Web App Features:
-Input Fields: Users enter values for all 9 features (e.g., Age, BMI, Glucose Level).  

### Prediction:
- Displays diabetes risk (Yes/No) based on the Random Forest model.  

### Accessibility: 
-Hosted on Streamlit Cloud for easy access—no local setup required.

### Results
-Best Model: Random Forest (Accuracy: ~75%, F1: ~0.70).  


Impact: The web app enables non-technical users (e.g., healthcare providers) to assess diabetes risk instantly.




