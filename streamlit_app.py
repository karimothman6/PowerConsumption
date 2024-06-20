import streamlit as st 
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor

#Load Model
model = joblib.load("model.joblib")


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

KW=(model.predict(test))**0.5
st.write(KW)
