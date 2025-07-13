import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')
if st.button('Construir histograma'):
    st.write('Creación de un histograma para la columna odometer')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

if st.button('Construir diagrama de dispersión'):
    st.write('Creación de un diagrama de dispersión odometer vs price')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)