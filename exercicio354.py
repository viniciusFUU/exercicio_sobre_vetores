lista = [None] * 20

for i in range(20):
    print(f"Digite o {i}º número: ")
    lista[i] = int(input())

for i in range(20):
    print(f"{i + 1} - {lista[i]}")

    if lista[i] % 2 == 0:
        print("Par")
    else:
        print("Impar")
