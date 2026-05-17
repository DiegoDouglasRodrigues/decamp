import streamlit as st
import numpy as np
import pandas as pd
from faker import Faker
from datetime import date

st.title("Beneficiamento")

# =====================================================
# PESQUISA
# =====================================================
with st.container(border=True):

    st.write("Selecione o romaneio")

    col_input, col_btn = st.columns([3, 1])

    with col_input:
        pedido = st.text_input(
            "Número do pedido",
            label_visibility="collapsed"
        )

    with col_btn:
        pesquisar = st.button("🔍")

    if pesquisar:
        if pedido:
            st.success(f"Buscando pedido: {pedido}")
        else:
            st.warning("Digite um número de pedido.")


# =====================================================
# DATAFRAME
# =====================================================
@st.cache_data
def get_profile_dataset(
        number_of_items: int = 20,
        seed: int = 0
):

    fake = Faker()

    np.random.seed(seed)
    Faker.seed(seed)

    data = []

    for _ in range(number_of_items):

        profile = fake.profile()

        data.append(
            {
                "name": profile["name"],
                "cor_beneficiamento": "",
                "data_beneficiamento": None,
            }
        )

    return pd.DataFrame(data)


# =====================================================
# SESSION STATE
# =====================================================
if "df" not in st.session_state:
    st.session_state.df = get_profile_dataset()

df = st.session_state.df


# =====================================================
# CONFIGURAÇÃO COLUNAS
# =====================================================
column_configuration = {

    "name": st.column_config.TextColumn(
        "Nome",
        width="medium",
    ),

    "cor_beneficiamento": st.column_config.TextColumn(
        "Cor Beneficiamento",
        width="medium",
    ),

    "data_beneficiamento": st.column_config.DateColumn(
        "Data Beneficiamento",
        format="DD/MM/YYYY",
    ),
}


# =====================================================
# TABELA PRINCIPAL
# =====================================================
st.subheader("Todos os registros")

event = st.dataframe(
    df,
    column_config=column_configuration,
    use_container_width=True,
    hide_index=True,
    on_select="rerun",
    selection_mode="multi-row",
)

people = event.selection.rows


# =====================================================
# FORMULÁRIO
# =====================================================
if people:

    st.divider()

    st.subheader("Beneficiamento")

    col1, col2 = st.columns(2)

    # =============================================
    # DATA
    # =============================================
    with col1:

        data_escolhida = st.date_input(
            "Selecione a Data",
            value=date.today(),
            format="DD/MM/YYYY"
        )

    # =============================================
    # COR
    # =============================================
    with col2:

        cor_escolhida = st.selectbox(
            "Selecione a Cor",
            [
                "PRETO",
                "BRANCO",
                "CINZA",
                "MARROM"
            ]
        )

    # =============================================
    # BOTÕES CRUD
    # =============================================
    col_btn1, col_btn2, col_btn3 = st.columns(3)

    with col_btn1:

        salvar = st.button(
            "💾 SALVAR",
            use_container_width=True
        )

    with col_btn2:

        excluir = st.button(
            "🗑️ EXCLUIR",
            use_container_width=True
        )

    with col_btn3:

        limpar = st.button(
            "🧹 LIMPAR",
            use_container_width=True
        )

    # =============================================
    # SALVAR
    # =============================================
    if salvar:

        for row in people:

            st.session_state.df.loc[
                row,
                "data_beneficiamento"
            ] = data_escolhida

            st.session_state.df.loc[
                row,
                "cor_beneficiamento"
            ] = cor_escolhida

        st.success("Dados atualizados com sucesso!")

        st.rerun()

    # =============================================
    # EXCLUIR
    # =============================================
    if excluir:

        st.session_state.df = (
            st.session_state.df
            .drop(index=people)
            .reset_index(drop=True)
        )

        st.success("Registro(s) removido(s)!")

        st.rerun()

    # =============================================
    # LIMPAR
    # =============================================
    if limpar:

        for row in people:

            st.session_state.df.loc[
                row,
                "data_beneficiamento"
            ] = None

            st.session_state.df.loc[
                row,
                "cor_beneficiamento"
            ] = ""

        st.success("Campos limpos!")

        st.rerun()

else:

    st.info(
        "Selecione uma ou mais linhas para habilitar o formulário."
    )