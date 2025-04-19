import streamlit as st
from functions import criar_arvore_elementos, gerar_mapa_astral
import networkx as nx

def main():
    st.title('Simetria dos Signos')
    st.write('Bem-vindo ao aplicativo de simetria dos signos!')

    nome = st.text_input("Digite seu nome:")

    # Campos separados para data de nascimento
    col1, col2, col3 = st.columns(3)
    with col1:
        dia = st.number_input("Dia", min_value=1, max_value=31, step=1)
    with col2:
        mes = st.number_input("Mês", min_value=1, max_value=12, step=1)
    with col3:
        ano = st.number_input("Ano", min_value=1900, max_value=2100, step=1)

    if nome and dia and mes and ano:
        data_nascimento = f"{int(dia):02d}/{int(mes):02d}/{int(ano)}"
        mapa_astral = gerar_mapa_astral(nome, data_nascimento)
        st.write(mapa_astral)

        # Gerar e exibir árvore dos elementos
        G = criar_arvore_elementos()
        st.write("Árvore dos Elementos:", G.nodes)

if __name__ == "__main__":
    main()
