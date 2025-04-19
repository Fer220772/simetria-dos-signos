
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

# ==================== BASE DE DADOS ====================

signos = {
    "Áries": {
        "datas": "21 de março a 19 de abril",
        "elemento": "Fogo",
        "modalidade": "Cardinal",
        "oposto": "Libra",
        "regente": "Marte",
        "compatíveis": ["Leão", "Sagitário", "Gêmeos", "Aquário"]
    },
    "Touro": {
        "datas": "20 de abril a 20 de maio",
        "elemento": "Terra",
        "modalidade": "Fixo",
        "oposto": "Escorpião",
        "regente": "Vênus",
        "compatíveis": ["Virgem", "Capricórnio", "Câncer", "Peixes"]
    },
    # Adicionar os outros signos conforme necessário
}

# ==================== FUNÇÕES ====================

def signo_oposto(signo):
    return signos.get(signo, {}).get("oposto", "Signo não encontrado")

def signos_compatíveis(signo):
    return signos.get(signo, {}).get("compatíveis", [])

def elemento_modalidade(signo):
    dados = signos.get(signo, {})
    return dados.get("elemento"), dados.get("modalidade")

def descobrir_signo(dia, mes):
    datas_signos = [
        ((3, 21), (4, 19), "Áries"),
        ((4, 20), (5, 20), "Touro"),
        # Adicionar os outros signos conforme necessário
    ]
    for inicio, fim, signo in datas_signos:
        if (mes == inicio[0] and dia >= inicio[1]) or (mes == fim[0] and dia <= fim[1]):
            return signo
    return "Data inválida"

def calcular_sinastria(signo1, signo2):
    pontos = 0
    if signo1 in signos and signo2 in signos:
        if signos[signo1]["elemento"] == signos[signo2]["elemento"]:
            pontos += 2  # Mais pontos se os elementos forem compatíveis
        if signos[signo1]["oposto"] == signo2 or signos[signo2]["oposto"] == signo1:
            pontos += 1  # Pontos por serem opostos
    return pontos

# ==================== ÁRVORE DOS ELEMENTOS ====================

elementos_interacoes = {
    "Fogo": {"Ar": "Compatível", "Terra": "Tensão", "Água": "Oposto"},
    "Terra": {"Fogo": "Tensão", "Ar": "Tensão", "Água": "Compatível"},
    "Ar": {"Fogo": "Compatível", "Terra": "Tensão", "Água": "Oposto"},
    "Água": {"Fogo": "Oposto", "Terra": "Compatível", "Ar": "Oposto"}
}

def criar_arvore_elementos():
    G = nx.Graph()

    for elemento in elementos_interacoes:
        G.add_node(elemento)

    for elemento1, interacoes in elementos_interacoes.items():
        for elemento2, relacao in interacoes.items():
            G.add_edge(elemento1, elemento2, relacao=relacao)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 8))
    nx.draw_networkx_nodes(G, pos, node_size=3000, node_color="skyblue", alpha=0.6)
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.7, edge_color="gray")
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold", font_color="black")
    
    edge_labels = nx.get_edge_attributes(G, "relacao")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
    
    plt.title("Árvore de Interações dos Elementos", fontsize=16)
    plt.axis("off")
    plt.show()

def exibir_arvore_elementos_streamlit():
    st.subheader("🌳 Árvore dos Elementos e suas Interações")
    st.write("Veja como os elementos se interagem entre si. As linhas indicam os tipos de relações entre eles.")
    criar_arvore_elementos()

# ==================== MAPA ASTRAL BÁSICO ====================

def criar_mapa_astral():
    casas = ["Casa 1", "Casa 2", "Casa 3", "Casa 4", "Casa 5", "Casa 6", "Casa 7", "Casa 8", "Casa 9", "Casa 10", "Casa 11", "Casa 12"]
    angulos = np.linspace(0, 2 * np.pi, len(casas), endpoint=False)
    
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
    ax.set_theta_direction(-1)
    ax.set_theta_offset(np.pi / 2)
    
    for i, casa in enumerate(casas):
        ax.text(angulos[i], 1.05, casa, fontsize=12, ha='center', va='center', color="black", fontweight='bold')

    ax.set_title("Mapa Astral Básico", fontsize=16, pad=20)
    plt.show()

def exibir_mapa_astral_streamlit():
    st.subheader("🌌 Mapa Astral Básico")
    st.write("Veja as casas astrológicas representadas no círculo.")
    criar_mapa_astral()

# ==================== EXPORTAÇÃO PARA PDF ====================

def exportar_para_pdf(signo1, signo2, pontos_sinastria):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setFont("Helvetica", 12)
    
    c.drawString(100, 750, f"Relatório de Sinastria entre {signo1} e {signo2}")
    c.drawString(100, 730, f"Signo 1: {signo1}")
    c.drawString(100, 710, f"Signo 2: {signo2}")
    c.drawString(100, 690, f"Compatibilidade: {pontos_sinastria} pontos")
    
    c.save()
    buffer.seek(0)
    return buffer

def download_pdf_streamlit(signo1, signo2, pontos_sinastria):
    st.subheader("📄 Exportar Relatório em PDF")
    pdf_buffer = exportar_para_pdf(signo1, signo2, pontos_sinastria)
    st.download_button("Baixar PDF", pdf_buffer, file_name="sinastria.pdf", mime="application/pdf")

# ==================== INTERFACE STREAMLIT ====================

st.set_page_config(page_title="Simetria dos Signos", layout="centered")
st.title("🔮 Simetria dos Signos")
st.markdown("Descubra signos opostos, compatibilidades e veja o círculo zodiacal.")

# Seção 1: Descubra seu signo
st.subheader("🔍 Descubra seu signo")
data = st.date_input("Sua data de nascimento", value=datetime(2000, 1, 1))
signo = descobrir_signo(data.day, data.month)
st.success(f"Seu signo é **{signo}**")

if signo in signos:
    st.markdown("### ✨ Informações do seu signo:")
    st.write(f"**Elemento:** {signos[signo]['elemento']}")
    st.write(f"**Modalidade:** {signos[signo]['modalidade']}")
    st.write(f"**Signo Oposto:** {signos[signo]['oposto']}")
    st.write(f"**Regente:** {signos[signo]['regente']}")
    st.write(f"**Signos compatíveis:** {', '.join(signos[signo]['compatíveis'])}")

# Seção 2: Cálculo de Sinastria
st.subheader("💑 Cálculo de Sinastria")
signo1 = st.selectbox("Escolha o signo da primeira pessoa", list(signos.keys()), key="signo1")
signo2 = st.selectbox("Escolha o signo da segunda pessoa", list(signos.keys()), key="signo2")

if signo1 and signo2:
    pontos = calcular_sinastria(signo1, signo2)
    if pontos >= 3:
        st.success(f"A compatibilidade entre **{signo1}** e **{signo2}** é alta! (Pontuação: {pontos})")
    elif pontos == 2:
        st.warning(f"A compatibilidade entre **{signo1}** e **{signo2}** é boa, mas não perfeita! (Pontuação: {pontos})")
    else:
        st.error(f"A compatibilidade entre **{signo1}** e **{signo2}** é baixa. (Pontuação: {pontos})")
    
    # Adicionar botão para exportação em PDF
    download_pdf_streamlit(signo1, signo2, pontos)

# Seção 3: Árvore dos Elementos
exibir_arvore_elementos_streamlit()

# Seção 4: Mapa Astral Básico
exibir_mapa_astral_streamlit()
