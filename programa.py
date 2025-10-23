from funcoes import define_posicoes, preenche_frota, posicao_valida

frota = {}
tipos_de_navios = { 
    "porta-aviões": (4,1),
    "navio-tanque": (3,2),
    "contratorpedeiro": (2, 3),
    "submarino": (1, 4)
}
for nome, (tamanho, quantidade) in tipos_de_navios.items():
    for i in range(quantidade):
        print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
        posicao_certa = False
