soma = 0
nota = 10
notas_digitadas = 0

while 10 <= nota <= 20:
    nota = int(input('Digite sua nota: '))
    if 10 <= nota <= 20:
        soma += nota
        notas_digitadas += 1
    else:
        break

print(f'A média das notas digitadas válidas é {soma / notas_digitadas}')
