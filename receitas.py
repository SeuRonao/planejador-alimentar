def adiciona_receita(lista):
    receita = {}
    receita["nome"] = input("Digite o nome da receita: ")
    receita["autor"] = input("Digite o autor da receita: ")
    receita["tempo de preparo"] = int(input("Digite o tempo de preparo em segundos: "))
    receita["porções"] = int(input("Digite o rendimento em porções: "))
    receita["url"] = input("Digite o endereço na internet dessa receita: ")
    qtd_ing = int(input("Digite a quantidade de ingredientes: "))
    receita["lista de ingredientes"] = []
    for _ in range(qtd_ing):
        ingrediente = {}
        ingrediente["nome"] = input("Digite o nome do ingrediente: ")
        ingrediente["medida"] = input("Digite o tipo de medida: ")
        ingrediente["quantidade"] = int(input("Digite a quantidade dessa medida: "))
        ingrediente["calorias"] = int(input("Digite a quantidade de calorias por medida para esse ingrediente: ")) * ingrediente["quantidade"]
        receita["lista de ingredientes"].append(ingrediente)
    receita["modo de preparo"] = input("Digite o modo de preparo: ")
    lista.append(receita)

def imprime_receita(receita):
    imprime = ""
    imprime += "Nome: " + receita["nome"] + "\n"
    imprime += "Autor: " + receita["autor"] + "\n"
    imprime += "Tempo de Preparo: " + str(receita["tempo de preparo"]) + "\n"
    imprime += "Porções: " + str(receita["porções"]) + "\n"
    imprime += "url: " + receita["url"] + "\n"
    imprime += "Lista de Ingredientes:\n"
    for ingrediente in receita["lista de ingredientes"]:
        imprime += "\tNome: " + ingrediente["nome"] + "\n"
        imprime += "\tMedida: " + ingrediente["medida"] + "\n"
        imprime += "\tQuantidade: " + str(ingrediente["quantidade"]) + "\n"
        imprime += "\tCalorias: " + str(ingrediente["calorias"]) + "\n"
    imprime += "Modo de Preparo:" + receita["modo de preparo"]
    print(imprime)

if __name__ == "__main__":
    lista = []
    adiciona_receita(lista)
    print(lista)
    imprime_receita(lista[0])