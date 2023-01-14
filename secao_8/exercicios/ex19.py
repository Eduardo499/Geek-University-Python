def maior_fator_primo(n):
    """Função que recebe um número e retorna o maior fator primo"""

    max_primo = -1

    while n % 2 == 0:
        max_primo = 2
        n /= 2

    while n % 3 == 0:
        max_primo = 3
        n /= 3

    for i in range(5, int(n ** 0.5) + 1, 6):
        while n % i == 0:
            max_primo = i
            n /= i

        while n % (i + 2) == 0:
            max_primo = i + 2
            n /= (i + 2)

    if n > 4:
        max_primo = n

    return int(max_primo)


num = int(input('Digite um número: '))
print()
print(maior_fator_primo(num))
