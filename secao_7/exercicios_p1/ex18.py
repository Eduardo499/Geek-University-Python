lista = []

for c in range(1, 11):
    n = int(input(f'Digite o {c}° número: '))
    lista.append(n)

x = int(input('Digite um número: '))
print(f'Os múltiplos de {x} dentro da lista são: ')

for i in range(10):
    print(x * lista[i])
