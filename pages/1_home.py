import time

import streamlit as st
import datetime


st.title('essa é a minha pagina inicial!!!!')
st.title('essa é a minha pagina inicial!!!!')
st.title('essa é a minha pagina inicial!!!!')

st.write('___________________________________________________________________________________________________________________________________________________________')


# --- LINHA 1 ---
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🏠 Home"):
        st.write(" atualizando Pagina")
        time.sleep(2)
        st.switch_page("pages/1_home.py")



with col2:
    if st.button("🔍 Operacional"):
        st.switch_page("pages/2_operacional.py")


with col3:
    if st.button("⚙️ Relatorios"):
        st.switch_page("pages/3_relatorios.py")


# Espaço opcional entre linhas
st.write("")


# --- LINHA 2 ---
col4, col5, col6 = st.columns(3)

with col4:
    if st.button("👤 Desenvovimento"):
        st.write("Desenvovimento")

with col5:
    if st.button("📊 Desenvovimento"):
        st.write("Desenvovimento")

with col6:
    if st.button("❓ Desenvovimento"):
        st.write("Desenvovimento")



#streamlit run app.py
