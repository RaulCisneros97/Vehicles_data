import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('notebooks/vehicles_us.csv')
st.header('Análisis sobre los anuncios de ventas de coches en Estados Unidos')
hist_button = st.button('Construir histograma')
scat_button = st.button('Contruir gráfico de dispersión')

if hist_button:
    st.write('Creación de histrograma sobre los anuncios de ventas de coches en E.U. con base en el millaje del coche')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
    
if scat_button:
    st.write('Creación de gráfico de dispersión que compara el precio del coche con base en el millaje del mismo')
    fig_1 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig_1, use_container_width=True)
    
