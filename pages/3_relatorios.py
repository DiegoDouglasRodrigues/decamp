import streamlit as st

st.title('RELATÓRIOS VENDAS')

with st.container(border=True):
    st.write("Relatorio")

    col1, col2 = st.columns([1, 3])

    with col1:
        opcao = st.selectbox(
            "Escolha um relatório:",
            ["Selecione o relatorio", "Acompanhamento de pedido", "Vendas por dia", "Vendas por mês", "Vendas por produto"]
        )

        if opcao == "Acompanhamento de pedido":
            col_input, col_btn = st.columns([3, 1])

            with col_input:
                pedido = st.text_input("Número do pedido", label_visibility="collapsed")

            with col_btn:
                pesquisar = st.button("🔍")

    # lógica fora da coluna
    if opcao == "Selecione o relatorio":
        st.write("...")

    elif opcao == "Vendas por dia":
        st.write("Mostrando relatório diário...")

    elif opcao == "Vendas por mês":
        st.write("Mostrando relatório mensal...")

    elif opcao == "Vendas por produto":
        st.write("Mostrando relatório por produto...")

    elif opcao == "Acompanhamento de pedido":
        if pesquisar:
            if pedido:
                st.success(f"Buscando pedido: {pedido}")
            else:
                st.warning("Digite um número de pedido.")