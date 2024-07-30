import streamlit as st
import pickle
import numpy as np
import os


cwd = os.getcwd()
path = os.path.join(cwd,'model.pkl')

# Load the model from the file
with open(path, 'rb') as f:
    model = pickle.load(f)


st.header("Prediction Website")
with st.form("my_form"):
    st.write("Inside the form")
    col1, col2 = st.columns(2)
    avg_temperature = col1.number_input("Input average Temperature",min_value=None, max_value=None, value=None)
    avg_humidity = col2.number_input("Input average Humidity",min_value=None, max_value=None, value=None)
    if avg_humidity!=None and avg_temperature!=None:
        result = np.exp(model.predict([[avg_temperature, avg_humidity]]))
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Appliances", result)