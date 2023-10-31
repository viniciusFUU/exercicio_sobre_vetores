clientes = []

while True:
    print("\n*** MENU ***")
    print("1 - Cadastrar dados do cliente")
    print("2 - Cadastrar milhagem do cliente")
    print("3 - Listar milhagem do cliente")
    print("4 - Imprimir os nomes que têm maior e menor milhagem")
    print("5 - Imprimir os nomes e as milhagens")
    print("6 - SAIR")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        if len(clientes) >= 50:
            print("A quantidade máxima de clientes (50) foi atingida. Não é possível adicionar mais clientes.")
        else:
            nome = input("Nome do cliente: ")
            endereco = input("Endereço do cliente: ")
            clientes.append({"nome": nome, "endereco": endereco, "milhagem": 0})
            print("Dados do cliente cadastrados com sucesso!")

    elif opcao == '6':
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
