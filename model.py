import streamlit as st
import pandas as pd 

df = pd.read_csv("Importaciones.csv")
st.line_chart(df)
