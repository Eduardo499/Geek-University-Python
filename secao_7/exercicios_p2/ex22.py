a = []
b = []

for i in range(3):
    elementos = []
    for j in range(3):
        elementos.append(int(input('Digite um número para a matriz A: ')))
    a.append(elementos)

for i in range(3):
    elementos = []
    for j in range(3):
        elementos.append(int(input('Digite um número para a matriz B: ')))
    b.append(elementos)

print()
print('Matriz A')
print()

for linha in a:
    for numero in linha:
        print(f'{numero:<2}', end=' ')
    print()

print()
print('Matriz B')
print()

for linha in b:
    for numero in linha:
        print(f'{numero:<2}', end=' ')
    print()

c = []

for i in range(3):
    elementos = []
    for j in range(3):
        elementos.append(a[i][j] * b[i][j])
    c.append(elementos)

print()
print('Matriz C = A * B')
print()

for linha in c:
    for numero in linha:
        print(f'{numero:<2}', end=' ')
    print()
