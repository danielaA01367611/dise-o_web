#------ Encabezado / import
import streamlit as st


#-----Tipos de Texto a imprimir
st.title("Título")

st.header("Header")

st.subheader("Sub Header")

st.markdown("Markdown")

st.code("Bloque de código. Ex - int a = 5")

st.text("Text")

st.write("write")


#----Variables
var1 = "Hola"
var2 = 5
st.write(var1)
st.write("Value of var2 = ",var2)