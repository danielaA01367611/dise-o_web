import streamlit as st
#Boton, Checkbox, Radio, Selectbox

#1) st.button(label,onclick,key)
if st.button('Saluda'):
    st.write('Hola! ')
else:
    st.write('Adios')

#2) st.checkbox(label)
st.write('Confirma selección:')
check = st.checkbox('Confirmo')

if check:
    st.write('Puedes Continuar.')
else:
    st.write('Confirma por favor.')

#3) st.radio(label,options)
framework = st.radio(
    "Qué framework prefieres?",
    ('Streamlit', 'Dash'))
if framework == 'Streamlit':
    st.write('Seleccionaste Streamlit.')
else:
    st.write('No seleccionaste Streamlit.')

#4) st.selectbox()
option = st.selectbox(
    'Cómo deseas ser contactado?',
    ('Email','Télefono','celular'))
st.write('Seleccionaste:',option)