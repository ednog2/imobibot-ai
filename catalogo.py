
import json
from pathlib import Path

ARQUIVO = Path(__file__).parent / "imoveis.json"


def carregar_imoveis():
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def buscar_imoveis(
    bairro=None,
    quartos=None,
    preco_max=None,
    finalidade=None
):
    imoveis = carregar_imoveis()
    resultados = []

    for imovel in imoveis:
        if bairro and bairro.lower() not in imovel["bairro"].lower():
            continue

        if quartos is not None and imovel["quartos"] < quartos:
            continue

        if preco_max is not None and imovel["preco"] > preco_max:
            continue

        if finalidade and finalidade.lower() != imovel["finalidade"].lower():
            continue

        resultados.append(imovel)

    return resultados
