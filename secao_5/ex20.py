a = int(input('Digite o comprimento do primeiro lado: '))
b = int(input('Digite o comprimento do segundo lado: '))
c = int(input('Digite o comprimento do terceiro lado: '))
if a + b > c and a + c > b and c + b > a:
    print('Triângulo possível!')
    if a == b == c:
        print('Triângulo equilátero')
    elif a == b or c == a or b == c:
        print('Triângulo isósceles')
    elif a != b != c:
        print('Triângulo escaleno')
else:
    print('Triângulo impossível!')
