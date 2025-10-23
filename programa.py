frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
}

especificacao = [
    ("porta-aviões",    4, 1),
    ("navio-tanque",    3, 2),
    ("contratorpedeiro",2, 3),
    ("submarino",       1, 4),
]

def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            pass

for nome, tamanho, qtd in especificacao:
    for _ in range(qtd):
        while True:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
            linha  = ler_int("Linha: ")
            coluna = ler_int("Coluna: ")

            if nome == "submarino":
                orientacao = "vertical"  # valor neutro para funções
            else:
                op = ler_int("[1] Vertical [2] Horizontal >")
                orientacao = "vertical" if op == 1 else "horizontal"

            if not posicao_valida(frota, linha, coluna, orientacao, tamanho):
                print("Esta posição não está válida!")
                continue

            preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
            break

print(frota)
