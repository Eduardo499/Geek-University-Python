x = []
y = []

for i in range(5):
    x.append(int(input(f'Digite um elemento para o vetor X: ')))
    y.append(int(input(f'Digite um elemento para o vetor Y: ')))

conjunto_x = set(x)
conjunto_y = set(y)

produto = 0
for c in range(5):
    produto += x[c] * y[c]

print()
print(f'A soma dos elementos dos dois vetores é {sum(conjunto_x) + sum(conjunto_y)}')
print(f'o produto dos elementos dos dois vetores é {produto}')
print(f'A diferença entre os dois vetores é {conjunto_x.difference(conjunto_y)}')
print(f'A intersecção entre os dois vetores é {conjunto_x.intersection(conjunto_y)}')
print(f'A união entre os dois vetores é {conjunto_x.union(conjunto_y)}')
