def define_posicoes(linha, coluna, orientacao, tamanho):
    lista = []
    i = 1
    while i < tamanho:
        cord = []
        if orientacao == "horizontal":
            cord = [linha, coluna + (i-1)]
        elif orientacao == "vertical":
            cord = [linha + (i-1), coluna]
        lista.append(cord)
        i += 1
    return lista
