lista = []
impar = []

while len(lista) < 3:
    n = int(input('Digite um número: '))

    if 0 <= n <= 50:
        lista.append(n)
    else:
        print('Número inválido!')
        print()

for i in lista:
    if i % 2 == 1:
        impar.append(i)

print()

print(lista)
print(impar)
