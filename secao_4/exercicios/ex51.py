from math import sqrt
x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))
dist = sqrt(x ** 2 + y ** 2)
print(f'A distância entre o ponto de origem (0, 0) e o ponto ({x}, {y}) é {dist}')
