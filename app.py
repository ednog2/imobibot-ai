
import os
import re
import time
import unicodedata

import streamlit as st
from dotenv import load_dotenv
from google import genai

from catalogo import buscar_imoveis

load_dotenv()

st.set_page_config(
    page_title="ImobiBot AI",
    page_icon="🏠"
)

st.title("🏠 ImobiBot AI")
st.caption("Seu assistente imobiliário inteligente")


def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto.lower())
    return "".join(
        letra for letra in texto
        if not unicodedata.combining(letra)
    )


def extrair_filtros(pergunta):
    texto = normalizar(pergunta)
    filtros = {}

    if "gleba palhano" in texto or "palhano" in texto:
        filtros["bairro"] = "Gleba Palhano"

    quartos = re.search(
        r"(\d+)\s*(?:quartos?|dormitorios?)",
        texto
    )
    if quartos:
        filtros["quartos"] = int(quartos.group(1))

    preco = re.search(
        r"(?:ate|no maximo|orcamento de|aluguel de ate)"
        r"\s*r?\$?\s*([\d.,]+)",
        texto
    )
    if preco:
        valor = preco.group(1).replace(".", "").replace(",", ".")
        filtros["preco_max"] = float(valor)

    filtros["finalidade"] = "Locação"
    return filtros


def formatar_imoveis(imoveis):
    if not imoveis:
        return (
            "Não encontrei imóveis compatíveis com esses filtros "
            "no catálogo disponível. Podemos tentar outro orçamento "
            "ou quantidade de quartos?"
        )

    linhas = ["Encontrei estas opções no catálogo:\n"]

    for imovel in imoveis:
        linhas.append(
            f"**{imovel.get('edificio', 'Apartamento')}** "
            f"(código {imovel['id']})\n"
            f"- Bairro: {imovel['bairro']}\n"
            f"- Quartos: {imovel['quartos']}\n"
            f"- Área: {imovel['area_m2']} m²\n"
            f"- Aluguel: R$ {imovel['preco']:,.2f}\n"
            f"- [Ver anúncio]({imovel['url']})\n"
        )

    linhas.append(
        "\nOs valores e a disponibilidade devem ser "
        "confirmados diretamente com a imobiliária."
    )

    return "\n".join(linhas)


if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])

pergunta = st.chat_input("Digite sua mensagem...")

if pergunta:
    st.session_state.mensagens.append({
        "role": "user",
        "content": pergunta
    })

    with st.chat_message("user"):
        st.write(pergunta)

    with st.chat_message("assistant"):
        with st.spinner("Buscando imóveis..."):

            filtros = extrair_filtros(pergunta)
            resultados = buscar_imoveis(**filtros)

            resposta_local = formatar_imoveis(resultados)
            texto = resposta_local

            chave = os.getenv("GEMINI_API_KEY")

            if chave:
                try:
                    cliente = genai.Client(api_key=chave)

                    contexto = (
                        "Você é um assistente imobiliário de Londrina. "
                        "Responda em português brasileiro. "
                        "Não invente imóveis ou características. "
                        "Use somente os resultados fornecidos. "
                        "Preserve os links dos anúncios. "
                        "Se não houver resultados, informe isso. "
                        "Não afirme que uma visita foi agendada.\n\n"
                        f"Pergunta do cliente: {pergunta}\n\n"
                        f"Resultado da busca:\n{resposta_local}"
                    )

                    for tentativa in range(4):
                        try:
                            resposta = cliente.models.generate_content(
                                model="gemini-3.5-flash-lite",
                                contents=contexto
                            )
                            if resposta.text:
                                texto = resposta.text
                            break

                        except Exception as erro:
                            if "503" in str(erro) and tentativa < 3:
                                time.sleep(2)
                            else:
                                raise

                except Exception as erro:
                    print(
                        "Gemini indisponível:",
                        type(erro).__name__,
                        str(erro)
                    )
                    texto = resposta_local

            st.markdown(texto)

    st.session_state.mensagens.append({
        "role": "assistant",
        "content": texto
    })
