def cria_receita():
    receita = {}
    receita["nome"] = input("Digite o nome da receita: ")
    receita["autor"] = input("Digite o autor da receita: ")
    receita["tempo de preparo"] = int(
        input("Digite o tempo de preparo em segundos: "))
    receita["porções"] = int(input("Digite o rendimento em porções: "))
    receita["url"] = input("Digite o endereço na internet dessa receita: ")
    qtd_ing = int(input("Digite a quantidade de ingredientes: "))
    receita["lista de ingredientes"] = []
    for _ in range(qtd_ing):
        ingrediente = {}
        ingrediente["nome"] = input("Digite o nome do ingrediente: ")
        ingrediente["medida"] = input("Digite o tipo de medida: ")
        ingrediente["quantidade"] = float(
            input("Digite a quantidade dessa medida: "))
        ingrediente["calorias"] = float(
            input(
                "Digite a quantidade de calorias por medida para esse ingrediente: "
            )) * ingrediente["quantidade"]
        receita["lista de ingredientes"].append(ingrediente)
    receita["modo de preparo"] = input("Digite o modo de preparo: ")
    return receita


def modifica_receita(receita):
    texto = "Quais campos você deseja modificar:\n"
    texto += "1. nome.\n"
    texto += "2. autor.\n"
    texto += "4. tempo de preparo.\n"
    texto += "8. porções.\n"
    texto += "16. url.\n"
    texto += "32. lista de ingredientes.\n"
    texto += "64. modo de preparo.\n"
    print(texto)
    escolha = int(input("Digite a soma das opções: "))
    if escolha >= 64:
        escolha -= 64
        receita["modo de preparo"] = input("Digite o novo modo de preparo: ")
    if escolha >= 32:
        escolha -= 32
        receita["lista de ingredientes"] = modifica_lista_ingredientes()
    if escolha >= 16:
        escolha -= 16
        receita["url"] = input("Digite a nova url: ")
    if escolha >= 8:
        escolha -= 8
        receita["porções"] = input("Digite a nova quantidade de porções: ")
    if escolha >= 4:
        escolha -= 4
        receita["tempo de preparo"] = input("Digite o novo tempo de preparo: ")
    if escolha >= 2:
        escolha -= 2
        receita["autor"] = input("Digite o novo autor: ")
    if escolha >= 1:
        escolha -= 1
        receita["nome"] = input("Digite o novo nome: ")


def modifica_lista_ingredientes():
    qtd_ing = int(input("Digite a quantidade de ingredientes: "))
    lista_de_ingredientes = []
    for _ in range(qtd_ing):
        ingrediente = {}
        ingrediente["nome"] = input("Digite o nome do ingrediente: ")
        ingrediente["medida"] = input("Digite o tipo de medida: ")
        ingrediente["quantidade"] = int(
            input("Digite a quantidade dessa medida: "))
        ingrediente["calorias"] = int(
            input(
                "Digite a quantidade de calorias por medida para esse ingrediente: "
            )) * ingrediente["quantidade"]
        lista_de_ingredientes.append(ingrediente)
    return lista_de_ingredientes


def imprime_receita(receita):
    imprime = "\n\nRECEITA\n-------\n"
    imprime += "Nome: " + receita["nome"] + "\n"
    imprime += "Autor: " + receita["autor"] + "\n"
    imprime += "Tempo de Preparo: " + str(receita["tempo de preparo"]) + "\n"
    imprime += "Porções: " + str(receita["porções"]) + "\n"
    imprime += "url: " + receita["url"] + "\n"
    imprime += "Lista de Ingredientes:\n"
    total_calorias = 0
    for ingrediente in receita["lista de ingredientes"]:
        imprime += "\n"
        imprime += "\tNome: " + ingrediente["nome"] + "\n"
        imprime += "\tMedida: " + ingrediente["medida"] + "\n"
        imprime += "\tQuantidade: " + str(ingrediente["quantidade"]) + "\n"
        imprime += "\tCalorias: " + str(ingrediente["calorias"]) + "\n"
        total_calorias += ingrediente["calorias"]
    imprime += "Modo de Preparo: " + receita["modo de preparo"] + "\n"
    imprime += "Total de Calorias: " + str(total_calorias)
    print(imprime)


def busca_receita(lista, nome):
    for receita in lista:
        if receita["nome"] == nome:
            return receita
    return None


if __name__ == "__main__":
    receita = cria_receita()
    imprime_receita(receita)
    modifica_receita(receita)
    imprime_receita(receita)
