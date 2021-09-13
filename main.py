import streamlit as st
import pandas as pd
import numpy as np
import subprocess

st.title('Guía de ventas')
#this verifies if someone pressed the button
if(st.button('Calcular tasa del día')):
    subprocess.run(['py','run.py'], cwd='./Scraper/Scraper/spiders')
    
st.sidebar.header('User Input Features')