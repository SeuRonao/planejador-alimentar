from receitas import *


def main():
    lista_de_receitas = []
    menu = {
        "1": "Cadastrar Receita",
        "2": "Modificar Receita",
        "3": "Remover Receita",
        "4": "Imprimir Receita",
        "5": "Listar Receitas Cadastradas",
        "6": "Sair do Programa"
    }
    while True:
        for chave, valor in menu.items():
            print(f"{chave}. {valor}")
        escolha = input("Digite uma opção: ")
        if escolha == "6":
            break
        elif escolha == "1":
            lista_de_receitas.append(cria_receita())
        elif escolha == "2":
            nome = input("Qual o nome da receita: ")
            receita = busca_receita(lista_de_receitas, nome)
            if receita:
                modifica_receita(receita)
            else:
                print("Receita não encontrada...")
        elif escolha == "3":
            nome = input("Qual o nome da receita: ")
            receita = busca_receita(lista_de_receitas, nome)
            if receita:
                lista_de_receitas.remove(receita)
            else:
                print("Receita não encontrada...")
        elif escolha == "4":
            nome = input("Qual o nome da receita: ")
            receita = busca_receita(lista_de_receitas, nome)
            if receita:
                imprime_receita(receita)
            else:
                print("Receita não encontrada...")
        elif escolha == "5":
            for receita in lista_de_receitas:
                imprime_receita(receita)


if __name__ == '__main__':
    main()
