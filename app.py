import streamlit as st
import requests

def buscarCEP(cep):
    resposta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    return resposta

st.set_page_config(
    page_title="Buscador de CEP",
    page_icon="🔎"

)
st.title("Sistema de busca de CEP")
st.divider()


menu = st.sidebar
cep = menu.text_input('Digite o CEP: ')
botao = menu.button('Pesquisar')

if botao:
    resposta = buscarCEP(cep)
    if resposta.status_code == 200:
        st.success('CEP encontrado com sucesso', icon='✅')
        dados = resposta.json()
        col1 , col2 = st.columns(2)
        col1.markdown(f"**CEP:** {dados['cep']}")
        col1.markdown(f"**CEP:** {dados['logradouro']}")
        col1.markdown(f"**Bairro:** {dados['bairro']}")
        col1.markdown(f"**Cidade:** {dados['localidade']}")
        col2.markdown(f"**Estado:** {dados['estado']}")
        col2.markdown(f"**Região:** {dados['regiao']}")
        col2.markdown(f"**DDD:** {dados['ddd']}")
        st.balloons()

    else: 
        st.error("o CEP informado é inválido", icon='❌')

