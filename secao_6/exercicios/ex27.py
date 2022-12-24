num = int(input('Digite um número inteiro e positivo: '))
serie = 0
soma_serie = 0

if num > 0:
    for i in range(1, num + 1):
        serie = 1/i
        soma_serie += serie
else:
    print('O número deve ser positivo!')

print(f'H({num}) = {soma_serie}')
