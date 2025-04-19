import streamlit as st
from functions import gerar_mapa_astral, criar_arvore_elementos
import matplotlib.pyplot as plt
import networkx as nx

st.set_page_config(page_title="Simetria dos Signos", layout="centered")
st.title("🔮 Simetria dos Signos")
st.markdown("Insira seu nome e data de nascimento para descobrir seu Mapa Astral simplificado.")

nome = st.text_input("Nome completo")
data_nascimento = st.text_input("Data de nascimento (dd/mm/aaaa)", placeholder="Ex: 01/01/1970")

if st.button("Gerar Mapa Astral"):
    if nome and data_nascimento:
        resultado = gerar_mapa_astral(nome, data_nascimento)
        st.text_area("Resultado do Mapa Astral", resultado, height=200)
    else:
        st.warning("Por favor, preencha todos os campos corretamente.")

st.markdown("---")
st.subheader("🌌 Árvore dos Elementos")
st.markdown("Visualização simplificada da conexão entre os elementos dos signos.")

G = criar_arvore_elementos()
pos = nx.circular_layout(G)
fig, ax = plt.subplots()
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=14, ax=ax)
st.pyplot(fig)

st.markdown("---")
st.markdown("Desenvolvido com ❤️ usando Streamlit")
