lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []

for i in range(4):
    for j in range(4):
        lista2.append(int(input('Digite um número para a primeira matriz: ')))
        lista4.append(int(input('Digite um número para a segunda matriz: ')))
    lista1.append(lista2)
    lista3.append(lista4)
    lista2 = []
    lista4 = []
print()
for c in lista1:
    print(c)
    lista5.append(max(c))
print()
for k in lista3:
    print(k)
    lista5.append(max(k))
print()
print(lista5)
