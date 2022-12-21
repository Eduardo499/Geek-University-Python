n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite o último número: '))
if n1 > n2 > n3:
    print(f'{n1}, {n2}, {n3}')
elif n2 > n1 > n3:
    print(f'{n2}, {n1}, {n3}')
elif n3 > n2 > n1:
    print(f'{n3}, {n2}, {n1}')
