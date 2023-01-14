def triangulo(a, b, c):
    """Função que recebe três valores representando a medida dos lados e retorna se esse triângulo é possível e o seu
    tipo """

    # Verifica se o triângulo é possível

    if a < b + c and b < c + a and c < a + b:

        # Verfica o tipo do triângulo

        if a == b == c:
            return 'Esse triângulo é Equilátero!'
        elif a == b and a != c and b != c or b == c and b != a and c != a or a == c and a != b and c != b:
            return 'Esse triângulo é Isósceles'
        elif a != b != c:
            return 'Esse triângulo é Escaleno'

    else:
        return 'Esse triângulo é impossível!'


lado_a = int(input('Digite o valor do lado a: '))
lado_b = int(input('Digite o valor do lado b: '))
lado_c = int(input('Digite o valor do lado c: '))

if lado_a > 0 and lado_b > 0 and lado_c > 0:
    print()
    print(triangulo(lado_a, lado_b, lado_c))
else:
    print('Valores inválidos, os valores devem ser maiores que zero')
