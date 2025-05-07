import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Análisis de anuncios de autos')

car_data = pd.read_csv('vehicles_us.csv')

if st.button('Mostrar histograma'):
    st.write('Histograma: Odómetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

if st.button('Mostrar dispersión'):
    st.write('Gráfico de dispersión: Precio vs Año')
    fig = px.scatter(car_data, x='model_year', y='price')
    st.plotly_chart(fig, use_container_width=True)
