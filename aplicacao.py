# Aplicação Streamlit — Dashboard + Predição de Obesidade

# ==================================================
# BIBLIOTECAS
# ==================================================

import joblib
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# ==================================================
# CONFIGURAÇÃO DA PÁGINA
# ==================================================

st.set_page_config(
    page_title='TESTE',
    page_icon='icone.png',
    layout='wide'
)