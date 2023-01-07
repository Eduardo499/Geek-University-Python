lista1 = []
lista2 = []

while len(lista1) < 10:
    while len(lista2) < 3:
        nota = int(input('Digite a nota: '))
        if 0 <= nota <= 10:
            lista2.append(nota)
        else:
            print('Nota inválida, válida apenas no intervalo de 0 a 10')
    lista1.append(lista2)
    lista2 = []

print()

for linha in lista1:
    for letra in linha:
        print(letra, end=' ')
    print()

print()

quantidade = [0, 0, 0]

for i in range(10):
    for j in range(3):
        if min(lista1[i]) == lista1[i][j]:
            quantidade[j] += 1
            break

for i in range(3):
    print(f"A quantidade de alunos com a menor nota na prova {i+1}: {quantidade[i]}")
