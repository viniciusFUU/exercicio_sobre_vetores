entrada = []
vetor = []

for i in range(3):
    frente = int(input(f"\nDigite o {i+1}º número da primeira lista: "))
    entrada.append(frente)
    tras = int(input(f"\nDigite o {i+1}º número da segunda lista: "))
    vetor.insert(0, tras)

print(f"{entrada},\n{vetor}")
