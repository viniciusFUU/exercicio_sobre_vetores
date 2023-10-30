lista = []

for i in range(1, 15 + 1):
    num = int(input(f"Digite o {i}º número da lista: "))
    lista.append(num)

    if i % 2 == 0:
        print(f"{lista[-1]} é par.")
    else:
        print(f"{lista[-1]} é impar.")
