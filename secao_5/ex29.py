from random import randint
acertos = 0
erros = 0
for c in range(0, 5):
    a = randint(1, 100)
    b = randint(1, 100)
    resposta = a + b
    pergunta = int(input(f'Quanto é {a} + {b}? '))
    if pergunta == resposta:
        acertos += 1
    else:
        erros += 1
print(f'Você acertou {acertos} perguntas')
print(f'Você errou {erros} perguntas')
