from funcoes import *

frota = {}

navios = [
    ("porta-aviões", 4, 1),
    ("navio-tanque", 3, 2),
    ("contratorpedeiro", 2, 3),
    ("submarino", 1, 4)
]

for nome, tamanho, quantidade in navios:
    for _ in range(quantidade):
        print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
        while True:
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            # Submarino não precisa perguntar orientação
            if nome == "submarino":
                orientacao = "vertical"  # tanto faz para tamanho 1
            else:
                opc = int(input("[1] Vertical [2] Horizontal >"))
                while opc not in (1, 2):
                    opc = int(input("[1] Vertical [2] Horizontal >"))
                orientacao = "vertical" if opc == 1 else "horizontal"

            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                break
            else:
                print("Esta posição não está válida!")

print(frota)
