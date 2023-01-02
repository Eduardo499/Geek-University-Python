lista = []

for c in range(1, 6):
    n = int(input(f'Digite o {c}° número: '))
    lista.append(n)

op = int(input("""Escolha a opção:
0 - Finalizar o progama
1 - Mostrar os números na ordem digitada
2 - Mostrar os números na ordem inversa da digitada
"""))

if op == 0:
    pass
elif op == 1:
    print(lista)
elif op == 2:
    print(lista[::-1])
else:
    print('Código inválido')
