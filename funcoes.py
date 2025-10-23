def define_posicoes(linha, coluna, orientacao, tamanho):
    lista = []
    for i in range(tamanho):
        if orientacao == "horizontal":
            lista.append([linha, coluna + i])
        elif orientacao == "vertical":
            lista.append([linha + i, coluna])
    return lista
    
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio in frota:
        frota[nome_navio].append(posicoes)
    else:
        frota[nome_navio] = [posicoes]
    return frota
    
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro
    
def posiciona_frota(frota):
    tabuleiro = []
    for i in range(10):
        linha = [0] * 10
        tabuleiro.append(linha)
    for nome_navio in frota:
        for navio in frota[nome_navio]: 
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1
    return tabuleiro
