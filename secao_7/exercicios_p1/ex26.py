from math import sqrt

vetor = []
soma = 0

for c in range(10):
    vetor.append(int(input('Digite um número: ')))

media = sum(vetor) / 10

for i in vetor:
    soma += (vetor[i] - media) ** 2


print(vetor)
print(f'A média desse vetor é {media}')
print(f'O desvio padrão desse vetor é {sqrt(soma / 10)}')
