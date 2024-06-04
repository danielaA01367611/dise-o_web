import streamlit as st
import datetime
#Entradas de Texto, Número, Fecha

#1) Entrada de Texto
title = st.text_input('Título de Película','Spiderman')
st.write("El título de película es: ",title)


#2) Entrada numérica
num = st.number_input('Inserta un número: ')
st.write("El número es: ",num)


#3) Entrada de fecha
d = st.date_input(
    'Tu fecha de nacimiento: ',
    datetime.date(2000,7,22))
st.write("Tu fecha de nacimiento es: ",d)
