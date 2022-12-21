num = int(input('Digite um número: '))
if num % 3 == 0 and num % 5 == 0:
    print('Número inválido')
elif num % 3 == 0:
    print('Esse número é divisível por 3')
elif num % 5 == 0:
    print('Esse número é divisível por 5')
else:
    print('Número inválido')
