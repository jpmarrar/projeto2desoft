from funcoes import define_posicoes, preenche_frota, posicao_valida

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
}

ordem = [
    ("porta-aviões", 4, 1),
    ("navio-tanque", 3, 2),
    ("contratorpedeiro", 2, 3),
    ("submarino", 1, 4)
]

for nome, tamanho, quantidade in ordem:
    for _ in range(quantidade):
        valido = False
        while not valido:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
            linha = int(input())
            coluna = int(input())

            if nome == "submarino":
                orientacao = "vertical"  # tanto faz; submarino ocupa uma célula
            else:
                orient = int(input())  # 1 ou 2, mas sem imprimir prompt
                orientacao = "vertical" if orient == 1 else "horizontal"

            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                valido = True
            else:
                print("Esta posição não está válida!")

print(frota)
