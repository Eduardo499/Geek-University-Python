num = int(input('Digite um número entre 100 e 999: '))

if 100 <= num <= 999:
    lista = str(num)
    for c in lista:
        print(c)
else:
    print('Digite um número entre 100 e 999')
