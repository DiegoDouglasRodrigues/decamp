import streamlit as st
import pandas as pd
import numpy as np



st.set_page_config(page_title="Meu App", layout="wide")

# Menu lateral
pg = st.navigation([
    st.Page("pages/1_home.py", title="Pagina Inicial"),
    st.Page("pages/2_operacional.py", title="Pagina Operacional"),
    st.Page("pages/3_relatorios.py", title="Pagina Relatorios"),
    st.Page("pages/4_beneficiamento.py", title="Beneficiamento"),

])

pg.run()


#streamlit run app.py