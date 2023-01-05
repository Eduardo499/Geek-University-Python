lista1 = []
lista2 = []
cont = 0

for i in range(4):
    for j in range(4):
        num = int(input('Digite um número: '))

        lista2.append(num)
        if num > 10:
            cont += 1

    lista1.append(lista2)
    lista2 = []

print(f'Nessa matriz 4X4 o número 10 se repete {cont} vezes')

for c in lista1:
    print(c)
