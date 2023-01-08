a = []

for i in range(3):
    elementos = []
    for j in range(3):
        elementos.append(int(input('Digite um número para a matriz A: ')))
    a.append(elementos)

print()
print('Matriz A')
print()

for linha in a:
    for numero in linha:
        print(f'{numero:<2}', end=' ')
    print()

b = []

for i in range(3):
    elementos = []
    for j in range(3):
        elementos.append(a[i][j] ** 2)
    b.append(elementos)

print()
print('Matriz B = A²')
print()

for linha in b:
    for numero in linha:
        print(f'{numero:<2}', end=' ')
    print()
