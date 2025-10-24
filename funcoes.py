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
    
def afundados(frota, tabuleiro):
    total_afundados = 0
    for nome_navio in frota:
        for navio in frota[nome_navio]:  
            afundado = True
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                if tabuleiro[linha][coluna] != 'X':
                    afundado = False
                    break
            if afundado:
                total_afundados += 1
    return total_afundados
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    lista = []
    novas_posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in novas_posicoes:
        if posicao[0] < 0 or posicao[0] > 9 or posicao[1] < 0 or posicao[1] > 9:
            return False
    for nome_navio in frota:
        for navio in frota[nome_navio]:
            for posicao in navio:
                if posicao in novas_posicoes:
                    return False 
    return True
