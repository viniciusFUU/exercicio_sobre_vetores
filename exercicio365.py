i = int(input("quantos cheques: "))

num = [None] * i
valor = [None] * i
data = [None] * i
destino = [None] * i

if i <= 20:
    for var in range(i):
        num[var] = input("numero do cheque: ")
        valor[var] = int(input("valor do cheque: "))
        data[var] = input("data do cheque (ddmmaa): ")
        destino[var] = input("destino do cheque: ")

    for var in range(i):
        print(
            f"cheque numero {num[var]} valor {valor[var]} data {data[var]} destino {destino[var]}")
else:
    print("Digite um número de cheques que seja menor ou igual a 20.")
