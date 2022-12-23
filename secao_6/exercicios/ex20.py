num = 0
numeros_lidos = 0
numeros_pares = 0

while num != 1000:
    num = int(input('Digite um número: '))

    if num % 2 == 0:
        numeros_pares += 1

    numeros_lidos += 1
print(f'Foram lidos {numeros_lidos}, dentre eles {numeros_pares} eram pares')
