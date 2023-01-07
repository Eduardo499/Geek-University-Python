from random import randint
lista1 = []
lista2 = []
gabarito = []

# Gera respostas aleatórias
while len(gabarito) < 10:
    n = randint(1, 4)

    if n == 1:
        gabarito.append('a')
    elif n == 2:
        gabarito.append('b')
    elif n == 3:
        gabarito.append('c')
    elif n == 4:
        gabarito.append('d')

print('Gabarito:')
# Imprime todas as respostas
for alternativa in range(10):
    print(f'{alternativa + 1}ª: {gabarito[alternativa].upper()}')
print()

# Matriz 5X10
# Usei o while para o loop acabar apenas quando tudo tiver correto

while len(lista1) < 5:
    while len(lista2) < 10:
        resp = str(input('Digite a alternativa: '))
        if resp.lower() == 'a' or resp.lower() == 'b' or resp.lower() == 'c' or resp.lower() == 'd':
            lista2.append(resp.lower())
        else:
            print('Alternativa inválida, apenas digite "a", "b", "c" ou "d"')
    lista1.append(lista2)
    lista2 = []

print()

# Imprime a matriz
for linha in lista1:
    for letra in linha:
        print(letra, end=' ')
    print()

print()

# Verifica a pontuação de cada aluno
for i in range(5):
    pont = 0
    for j in range(len(lista1[i])):
        if lista1[i][j] == gabarito[j]:
            pont += 1
    if pont == 10:
        print(f'O aluno {i + 1} gabaritou a prova!')
    else:
        print(f'O aluno {i + 1} acertou {pont} questões!')
