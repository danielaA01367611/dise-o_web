import pandas as pd
import numpy as np
import streamlit as st

#función y argumentos para gráfico de línea
#st.line_chart(data,x,y,width,height)
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['A','B','C'])

st.line_chart(chart_data)

#función y argumentos para gráfico de área
#st.line_chart(data,x,y,width,heigth)
st.area_chart(chart_data)

#función y argumentos para gráfico de barra
#st.bar_chart(data,x,y,width,heigth)
st.bar_chart(chart_data)