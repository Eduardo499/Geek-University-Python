idade = int(input('Digite sua idade: '))
tempo = int(input('Digite seu tempo de serviço: '))
if idade == 65:
    print('Você pode se aposentar')
elif tempo == 30:
    print('Você pode se aposentar')
elif idade == 60 and tempo == 25:
    print('Você pode se aposentar')
else:
    print('Você não pode se aposentar')
