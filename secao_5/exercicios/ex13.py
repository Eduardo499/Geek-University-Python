nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
nota_3 = float(input('Digite a terceira nota: '))
media = (nota_1 + nota_2 + nota_3 * 2) / 3
if media > 6:
    print('Aprovado')
else:
    print('Reprovado')
