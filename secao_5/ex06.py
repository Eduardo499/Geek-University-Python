n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print(f'{n1} é maior que {n2}')
    print(f'A diferença entre {n1} e {n2} é {n1 - n2}')
else:
    print(f'{n2} é maior que {n1}')
    print(f'A diferença entre {n2} e {n1} é {n2 - n1}')
