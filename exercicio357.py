nome = []
salario = []

for i in range(0, 3):
    nome1 = input("\nDigite seu nome: ")
    salario1 = int(input("Digite o valor do teu salário: \n"))
    reajuste = salario1 * 0.08
    salario_com_reajuste = salario1 + reajuste

    nome.append(nome1)
    salario.append(salario_com_reajuste)

for n in range(0, 3):
    print(f"nome: {nome[n]} salario: {salario[n]}")
