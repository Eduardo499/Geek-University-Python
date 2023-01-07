lista1 = []
lista2 = []
lista3 = []
lista_transporta = []

for i in range(3):
    for j in range(3):
        lista2.append(int(input('Digite um número: ')))
    lista1.append(lista2)
    lista2 = []

print()
print('Matriz normal')
print()
for c in lista1:
    print(c)

for i in range(3):
    for j in range(3):
        lista3.append(lista1[j][i])
    lista_transporta.append(lista3)
    lista3 = []
print()
print('Matriz transporta')
print()
for c in lista_transporta:
    print(c)
