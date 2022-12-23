peso = float(input('Digite seu peso (em Kg): '))
altura = float(input('Digite sua altura (em metros): '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Abaixo do Peso')
elif 18.6 <= imc <= 24.9:
    print('Saudável')
elif 25 <= imc <= 29.9:
    print('Peso em Excesso')
elif 30 <= imc <= 34.9:
    print('Obesidade Grau I')
elif 35 <= imc <= 39.9:
    print('Obesidade Grau II (severa)')
elif imc >= 40:
    print('Obesidade Grau III (mórbida')
