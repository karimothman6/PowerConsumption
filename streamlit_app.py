import streamlit as st 
import pandas as pd
import joblib
import numpy as np

model_path = 'model.joblib'

if not os.path.exists(model_path):
    st.error(f"The model file {model_path} does not exist. Please ensure the file is in the correct directory.")
else:
    try:
        # Load the model
        model = joblib.load(model_path)
        st.success("Model loaded successfully!")
    except Exception as e:
        st.error(f"Error loading the model: {e}")

    # Define the prediction function
    def predict_kw(input_data):
        prediction = model.predict(input_data)
        return np.sqrt(abs(prediction))

st.markdown("# Power Consumption")

st.write("Welcome to the app")

shift = st.selectbox(
    "Shift",
    (1, 2, 3))

MSU = st.number_input("MSU")

st.write("Line Status")

LineNotStaffed = st.slider("Line Not Staffed",0,10)
STNU = st.slider("STNU",0,10)
STNUVAR = st.slider("STNU VAR",0,10)
EO = st.slider("EO NON SHIPPABLE",0,10)
Shutdown=st.radio("Shutdown",['Yes','No'],horizontal=True)

if Shutdown=='Yes': Shutdown=1
if Shutdown=='No': Shutdown=0


test=pd.DataFrame([shift,MSU,LineNotStaffed,STNU,STNUVAR,EO,Shutdown]).T

if st.button('Predict'):
    prediction = predict_kw(test)
    st.write(f"Predicted KW: {prediction[0]}")
