import streamlit as st

st.title('Upload de Romaneio')

with st.container(border=True):
    st.subheader("Enviar arquivo")

    # estado para controlar exibição do uploader
    if "mostrar_upload" not in st.session_state:
        st.session_state.mostrar_upload = False

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        novo = st.button("Novo Romaneio")

    with col2:
        enviar = st.button("Enviar")

    with col3:
        cancelar = st.button("Cancelar")

    with col4:
        voltar = st.button("Voltar")

    # ativa o upload ao clicar em Novo
    if novo:
        st.session_state.mostrar_upload = True
        st.info("Novo romaneio iniciado.")

    arquivo = None

    # só mostra upload depois do botão Novo
    if st.session_state.mostrar_upload:
        arquivo = st.file_uploader(
            "Selecione o arquivo Excel",
            type=["xlsx", "xls"]
        )

    # lógica dos botões
    if enviar:
        if arquivo is not None:
            st.success(f"Arquivo '{arquivo.name}' enviado com sucesso!")
        else:
            st.warning("Selecione um arquivo antes de enviar.")

    if cancelar:
        st.session_state.mostrar_upload = False
        st.warning("Operação cancelada.")

    if voltar:
        st.info("Voltando para a página anterior...")