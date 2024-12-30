import streamlit as st
import pandas as pd
import numpy as np
import pickle

csv_file_path = r'C:\Users\mahap\OneDrive\Desktop\C++,JS python codes\.vscode\ML-DL-NLP\myenv\CompleteKmeansclassification\pollution.csv' 
df = pd.read_csv(csv_file_path)

st.title("Air Quality Prediction")
st.markdown("""
This app allows you to predict air quality based on various input features.  
At the start, a preview of the dataset is shown, and you can input values for specific features to make predictions.
""")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Input Features")
user_input = {}
for column in df.columns:
    if column!= "Air Quality":  # Exclude the air quality column
        user_input[column] = st.number_input(f"Enter value for {column}", value=0.0)

with open('kmeans.pkl','rb') as file:
    kmeans=pickle.load(file)
with open('scaler.pkl','rb') as file:
    scaler=pickle.load(file)

if st.button("Predict Air Quality"):
    input_data = [list(user_input.values())]
    input_data=np.array(input_data)
    prediction = kmeans.predict(input_data)
    st.subheader("Prediction")
    st.write(f"The predicted air quality is: {prediction[0]}")
