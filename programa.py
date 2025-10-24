from funcoes import preenche_frota, posicao_valida

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}

navios_tam_qtd = [
    ("porta-aviões", 4, 1),
    ("navio-tanque", 3, 2),
    ("contratorpedeiro", 2, 3),
    ("submarino", 1, 4),
]

for nome_navio, tamanho, quantidade in navios_tam_qtd:
    i = 0
    while i< quantidade:
        print(f"Insira as informações referentes ao navio{nome_navio} que possui tamanho {tamanho}")
        linha = int(input())
        coluna = int(input())

        if nome_navio == "submarino": 
            orientacao = "horizontal"

        else: 
            orientacao = input()
            if orientacao == '1':
                orientacao = 'vertical'
            else:
                orientacao = 'horizontal'

        if posicao_valida(frota, linha, coluna, orientacao, tamanho):
            preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
            i += 1

        else: 
                print ("Esta posição não está válida")

print (frota) 
