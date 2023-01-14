def soma_entre(n1, n2):
    """Função que retorna a soma dos números entre 'n1' e 'n2'"""

    soma = 0
    for i in range(n1, n2 + 1):
        soma += i
    return soma


num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print()

if num1 > 0 and num2 > 0:
    print(f'A soma dos números do intervalor fechado [{num1}, {num2}] é {soma_entre(num1, num2)}')
else:
    print('Números inválidos, digite apenas números positivos')
