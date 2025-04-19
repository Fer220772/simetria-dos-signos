import networkx as nx

def criar_arvore_elementos():
    G = nx.Graph()
    G.add_nodes_from(['Fogo', 'Terra', 'Ar', 'Água'])
    G.add_edges_from([
        ('Fogo', 'Terra'),
        ('Terra', 'Ar'),
        ('Ar', 'Água'),
        ('Água', 'Fogo')
    ])
    return G

SIGNO_DESCRICOES = {
    "Áries": "Impulsivo, corajoso, cheio de energia e iniciativa.",
    "Touro": "Paciente, determinado, amante do conforto e da estabilidade.",
    "Gêmeos": "Curioso, comunicativo, versátil e adaptável.",
    "Câncer": "Sensível, protetor, apegado ao lar e à família.",
    "Leão": "Confiante, carismático, gosta de ser o centro das atenções.",
    "Virgem": "Detalhista, prático, organizado e analítico.",
    "Libra": "Diplomático, sociável, busca equilíbrio e harmonia.",
    "Escorpião": "Intenso, emocional, determinado e misterioso.",
    "Sagitário": "Aventureiro, otimista, amante da liberdade e do conhecimento.",
    "Capricórnio": "Responsável, disciplinado, ambicioso e prático.",
    "Aquário": "Inovador, independente, idealista e visionário.",
    "Peixes": "Sonhador, empático, sensível e criativo.",
    "Desconhecido": "Não foi possível identificar o signo com os dados fornecidos."
}

def descobrir_signo(dia, mes):
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Áries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Touro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Gêmeos"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Câncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leão"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgem"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpião"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitário"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        return "Capricórnio"
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Aquário"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "Peixes"
    return "Desconhecido"

def gerar_mapa_astral(nome, data_nascimento):
    try:
        dia, mes, ano = map(int, data_nascimento.split("/"))
        signo = descobrir_signo(dia, mes)
    except:
        signo = "Desconhecido"

    ascendente = signo  # Simulação
    lua = signo          # Simulação
    jupiter = signo      # Simulação

    descricao = SIGNO_DESCRICOES.get(signo, "Descrição não disponível.")
    return (
        f"Mapa Astral de {nome}\n"
        f"Data de Nascimento: {data_nascimento}\n"
        f"Signo Solar: {signo}\n"
        f"Ascendente: {ascendente}\n"
        f"Lua: {lua}\n"
        f"Júpiter: {jupiter}\n"
        f"Descrição: {descricao}"
    )
