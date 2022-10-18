import streamlit as st
import pandas as pd 
from streamlit_echarts import st_echarts

st.write("""
# Esta es la primera prueba 
""")

option = {
    "xAxis": {
        "type": "category",
        "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    },
    "yAxis": { "type": "value" },
    "series": [
        {"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "line" }
    ],
}