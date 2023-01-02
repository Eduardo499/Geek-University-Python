lista = []
impar = []
par = []

for c in range(6):
    lista.append(int(input(f'Digite um número na posição {c}: ')))

for i in lista:

    if i % 2 == 1:
        impar.append(i)
    else:
        par.append(i)

print()
print(f'Números pares digitados: {par}')
print(f'Soma dos números pares: {sum(par)}')
print(f'Números ímpares digitados: {impar}')
print(f'Quantidade de números ímpares digitados: {len(impar)}')
