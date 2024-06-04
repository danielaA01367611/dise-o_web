import streamlit as st
from datetime import time
from datetime import datetime

#Ej. 1
edad = st.slider('Qué edad tienes?',0,130,25)
st.write("Tengo ",edad," años.")


#Ej. 2
valores = st.slider(
    'Selecciona un rango de valores',
    0.0,100.0,(25.0, 75.0))
st.write("Valores:",valores)


#Ej. 3
start_time = st.slider(
    'Cúando inicias?',
    value=datetime(2024,6,3,9,30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:",start_time)

