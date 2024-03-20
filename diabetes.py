
import numpy as np
import streamlit as st
import pickle

# Load the trained model
model = pickle.load(open('diabetes_model', 'rb'))

# Reshape input features array outside the prediction function
def preprocess_features(features):
    return np.array(features).reshape(1, -1)

# Predict diabetes based on features
def predict_diabetes(features):
    return model.predict(features)

# Create a Streamlit web app
def main():
    st.image('diabetic_pic.jpg',use_column_width='right')
    st.write("Enter the required information to predict the likelihood of having diabetes.")

    # Input fields for user information
    input_features = {
        "Pregnancies": st.number_input("How many pregnancies have you had?", min_value=0, max_value=17, value=2),
        "Glucose": st.number_input("Enter your glucose level", min_value=1, max_value=200, value=30),
        "BloodPressure": st.number_input("Enter your blood pressure", min_value=1, max_value=100, value=30),
        "SkinThickness": st.number_input("Enter your skin thickness", min_value=0, value=80),
        "Insulin": st.number_input("Enter your insulin level", min_value=0, value=20),
        "BMI": st.number_input("Enter your BMI", min_value=0.0, value=30.0),
        "DiabetesPedigreeFunction": st.number_input("Your diabetes pedigree function", min_value=0.0, value=3.0),
        "Age": st.number_input("Enter your age", min_value=1, max_value=100, value=30)
    }

    # Convert categorical input to numerical value efficiently
    input_features["Pregnancies"] = 1 if input_features["Pregnancies"] == "Yes" else 0

    if st.button("PREDICT"):
        # Gather input features and preprocess
        features = preprocess_features(list(input_features.values()))

        # Predict diabetes
        prediction = predict_diabetes(features)

        # Display the prediction
        if prediction == 0:
            st.success('Congratulations! You have a low diabetes risk')
            st.write(
                "Based on the provided information, it seems there is no immediate risk of diabetes. However, it's always advisable to consult with a healthcare professional for a more accurate assessment.")
        else:
            st.warning('Warning! You have a high diabetes risk')
            st.write(
                "Based on the provided information, there is a potential risk of diabetes. It is strongly recommended to consult with a healthcare professional for a thorough evaluation and guidance on preventive measures.")

if __name__ == '__main__':
    main()
