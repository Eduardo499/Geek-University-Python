from random import randint

cont = 0
numero_gerado = randint(1, 1000)

while True:
    numero_digitado = int(input('Digite um número: '))

    cont += 1

    if numero_gerado == numero_digitado:
        print(f'Você acertou o número em {cont} tentativas')
        break
    else:
        if numero_digitado > numero_gerado:
            print('O número é  menor')
        elif numero_digitado < numero_gerado:
            print('O número é maior')
