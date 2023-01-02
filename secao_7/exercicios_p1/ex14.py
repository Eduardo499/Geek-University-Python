lista1 = []
lista2 = []

for c in range(1, 11):
    n = int(input(f'Digite o {c}° número: '))
    lista1.append(n)

for i in lista1:
    if lista1.count(i) > 1:
        if i in lista2:
            pass
        else:
            lista2.append(i)

print()
if len(lista2) > 0:
    print('Os valores repetidos digitados foram: ')

    for j in lista2:
        print(j, end=' ')
else:
    print('Não foi digitado nenhum valor repetido')
