import streamlit as st
import pandas as pd
import sqlite3
from datetime import date

st.title("Beneficiamento")
st.title("Beneficiamento!")

# =====================================================
# CARREGA DADOS SQLITE
# =====================================================
@st.cache_data
def carregar_dados():

    conn = sqlite3.connect("expedicao.db")

    query = """
    SELECT
        id,
        lote,
        nf_saida,
        loja,
        ce,
        cor,
        peso_programado,
        data_programada,
        data_enviada,
        peso_enviado,
        data_recebida,
        peso_recebido
    FROM expedicao
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


# =====================================================
# SESSION STATE
# =====================================================
if "df" not in st.session_state:
    st.session_state.df = carregar_dados()

df = st.session_state.df


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

            filtro = df[
                df["lote"].astype(str).str.contains(
                    pedido,
                    case=False,
                    na=False
                )
            ]

            st.session_state.df = filtro

            st.success(f"Resultado para: {pedido}")

        else:

            st.session_state.df = carregar_dados()

            st.warning("Digite um número de pedido.")


# =====================================================
# CONFIGURAÇÃO COLUNAS
# =====================================================
column_configuration = {

    "id": st.column_config.NumberColumn(
        "ID",
        width="small",
    ),

    "lote": st.column_config.NumberColumn(
        "Lote",
        width="small",
    ),

    "nf_saida": st.column_config.NumberColumn(
        "NF Saída",
        width="small",
    ),

    "loja": st.column_config.TextColumn(
        "Loja",
        width="small",
    ),

    "ce": st.column_config.TextColumn(
        "C/E",
        width="small",
    ),

    "cor": st.column_config.TextColumn(
        "Cor",
        width="small",
    ),

    "peso_programado": st.column_config.NumberColumn(
        "Peso Programado",
        format="%.2f",
    ),

    "peso_enviado": st.column_config.NumberColumn(
        "Peso Enviado",
        format="%.2f",
    ),

    "peso_recebido": st.column_config.NumberColumn(
        "Peso Recebido",
        format="%.2f",
    ),

    "data_programada": st.column_config.DateColumn(
        "Data Programada",
        format="DD/MM/YYYY",
    ),

    "data_enviada": st.column_config.DateColumn(
        "Data Enviada",
        format="DD/MM/YYYY",
    ),

    "data_recebida": st.column_config.DateColumn(
        "Data Recebida",
        format="DD/MM/YYYY",
    ),
}


# =====================================================
# TABELA PRINCIPAL
# =====================================================
st.subheader("Todos os registros")

event = st.dataframe(
    st.session_state.df,
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
    # BOTÕES
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
    # SALVAR SQLITE
    # =============================================
    if salvar:

        conn = sqlite3.connect("expedicao.db")

        cursor = conn.cursor()

        for row in people:

            registro_id = st.session_state.df.iloc[row]["id"]

            cursor.execute("""
                UPDATE expedicao
                SET
                    cor = ?,
                    data_recebida = ?
                WHERE id = ?
            """, (
                cor_escolhida,
                data_escolhida.strftime("%Y-%m-%d"),
                int(registro_id)
            ))

        conn.commit()
        conn.close()

        st.cache_data.clear()

        st.session_state.df = carregar_dados()

        st.success("Dados atualizados com sucesso!")

        st.rerun()

    # =============================================
    # EXCLUIR SQLITE
    # =============================================
    if excluir:

        conn = sqlite3.connect("expedicao.db")

        cursor = conn.cursor()

        for row in people:

            registro_id = st.session_state.df.iloc[row]["id"]

            cursor.execute("""
                DELETE FROM expedicao
                WHERE id = ?
            """, (int(registro_id),))

        conn.commit()
        conn.close()

        st.cache_data.clear()

        st.session_state.df = carregar_dados()

        st.success("Registro(s) removido(s)!")

        st.rerun()

else:

    st.info(
        "Selecione uma ou mais linhas para habilitar o formulário."
    )