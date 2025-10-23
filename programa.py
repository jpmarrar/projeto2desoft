from funcoes import define_posicoes, preenche_frota, posicao_valida

frota = {"porta-aviões": [], "navio-tanque": [], "contratorpedeiro": [], "submarino": []}

navios_info = {"porta-aviões": {"tamanho": 4, "quantidade": 1},"navio-tanque": {"tamanho": 3, "quantidade": 2},"contratorpedeiro": {"tamanho": 2, "quantidade": 3},"submarino": {"tamanho": 1, "quantidade": 4}}

for nome_navio, info in navios_info.items():
    for i in range(info["quantidade"]):
        print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {info['tamanho']}", end=" ")
        posicao_valida_flag = False

        while not posicao_valida_flag:
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            if nome_navio != "submarino":
                orientacao_input = int(input("[1] Vertical [2] Horizontal >"))
                orientacao = "vertical" if orientacao_input == 1 else "horizontal"
            else:
                orientacao = "vertical"

            if posicao_valida(frota, linha, coluna, orientacao, info["tamanho"]):
                frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, info["tamanho"])
                posicao_valida_flag = True
            else:
                print("Esta posição não está válida!", end=" ")

print(f"{frota}", end="")
