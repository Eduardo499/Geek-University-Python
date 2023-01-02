lista = []

while len(lista) < 6:
    n = int(input('Digite um número par: '))
    if n % 2 == 0:
        lista.append(n)
    else:
        print('Esse número não é par!')
        print()

print()
print(lista[::-1])
