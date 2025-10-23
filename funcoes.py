def define_posicoes(linha, coluna, orientacao, tamanho):
    lista = []
    for i in range(tamanho):
        if orientacao == "horizontal":
            lista.append([linha, coluna + i])
        elif orientacao == "vertical":
            lista.append([linha + i, coluna])
    return lista
