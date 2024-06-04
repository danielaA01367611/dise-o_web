import streamlit as st
#Layouts y Contenedores: Sidebar, Columnas, Expander

#1) Sidebar
add_selectbox = st.sidebar.selectbox(
    "Como deseas ser contactado?",
    ("Email","Teléfono Oficina","Celular"))

with st.sidebar:
    add_radio = st.radio(
        "Elige un método de envío",
        ("Standard","Premium"))

    
#2) Columnas
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Esta es la columna 1")
    st.title("Col 1")
    st.write("Texto en columna 1")

with col2:
    st.header("Esta es la columna 2")
    st.title("Col 2")
    st.write("Texto en columna 2")

with col3:
    st.header("Esta es la columna 3")
    st.title("Col 3")
    st.write("Texto en columna 3")


#3) Expander
st.bar_chart({"data":[1,5,2,6,2,1]})

with st.expander("Expandir >"):
    st.write("Texto a colocar dentro de la sección del Expander")