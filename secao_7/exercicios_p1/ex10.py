notas = []

for c in range(1, 16):
    nota = int(input(f'Digite a {c}° nota: '))
    if nota > 0:
        notas.append(nota)
print(f'A média das notas é {sum(notas) / len(notas)}')
