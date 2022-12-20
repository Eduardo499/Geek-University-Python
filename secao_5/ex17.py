b_M = int(input('Digite o comprimento da base maior: '))
b_m = int(input('Digite o comprimento da base menor: '))
h = int(input('Digite a altura: '))
if b_M > 0 and b_m > 0:
    print(f'A área do trápezio é {((b_m + b_M) * h) / 2}')
else:
    print('Trapézio impossível')
