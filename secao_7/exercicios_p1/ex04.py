lista = []

for i in range(1, 9):
    n = int(input(f'Digite o {i}° número: '))
    lista.append(n)

x = int(input('Digite um número X referente a posição do índice da lista: '))
y = int(input('Digite um número Y referente a posição do índice da lista: '))

print(f'A soma dos valores dessas duas posições é {lista[x] + lista[y]}')
