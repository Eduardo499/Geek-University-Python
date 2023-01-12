def quadrado_perfeito(num):
    """Função que verifica se um número é um quadrado perfeito, ou seja, tem uma raiz quadrada exata"""

    if 0 < num == (num ** 0.5) ** 2:
        print(f'Esse número é um quadrado perfeito')
    else:
        print(f'Esse número não é um quadrado perfeito')


quadrado_perfeito(5)
