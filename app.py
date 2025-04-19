import streamlit as st
from functions import gerar_mapa_astral

st.set_page_config(page_title='Simetria dos Signos', layout='centered')

st.title('🔮 Simetria dos Signos')

nome = st.text_input('Nome completo')
dia = st.number_input('Dia de nascimento', min_value=1, max_value=31, step=1)
mes = st.number_input('Mês de nascimento', min_value=1, max_value=12, step=1)
ano = st.number_input('Ano de nascimento', min_value=1900, max_value=2100, step=1)

if st.button('Gerar Mapa Astral'):
    data_nascimento = f'{dia:02}/{mes:02}/{ano}'
    resultado = gerar_mapa_astral(nome, data_nascimento)
    st.text_area('Resultado', resultado, height=200)
