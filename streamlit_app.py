import streamlit as st 
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor

# Function to load the model
def load_model(path):
    try:
        model = joblib.load(path)
        st.write("Model loaded successfully.")
        return model
    except ModuleNotFoundError as e:
        st.error(f"ModuleNotFoundError: {e}")
        st.error("Ensure all dependencies are installed and available.")
    except ValueError as e:
        st.error(f"ValueError: {e}")
        st.error("This error is often due to version incompatibilities. Please ensure the scikit-learn version used to create the model matches the one used to load it.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
    return None

# Load the model
model = load_model("model.joblib")

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


# Check if the model was loaded successfully before making predictions
if model is not None:
    # Example test data, replace with your actual test data
    test=pd.DataFrame([shift,MSU,LineNotStaffed,STNU,STNUVAR,EO,Shutdown]).T    
    try:
        KW = (model.predict(test))**0.5
        st.write(f"Predicted value: {KW}")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
else:
    st.error("Model could not be loaded. Predictions cannot be made.")

test=pd.DataFrame([shift,MSU,LineNotStaffed,STNU,STNUVAR,EO,Shutdown]).T

KW=(model.predict(test))**0.5
st.write(KW)
