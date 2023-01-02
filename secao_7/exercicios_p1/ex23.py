lista1 = []
lista2 = []
produto_escalar = 0

for c in range(1, 6):
    n1 = int(input(f'Digite o {c}ª número para a primeira lista: '))
    n2 = int(input(f'Digite o {c}ª número para a segunda lista: '))
    lista1.append(n1)
    lista2.append(n2)

for i in range(5):
    produto_escalar += lista1[i] * lista2[i]

print()
print(lista1)
print(lista2)
print(produto_escalar)
