import streamlit as st
import pandas as pd 

st.write("""
# Esta es la primera prueba 
""")

df = pd.read_csv("Importacion.csv")
st.dataframe(df)