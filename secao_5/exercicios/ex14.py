nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
nota_3 = float(input('Digite a terceira nota: '))
media = (nota_1 * 2 + nota_2 * 3 + nota_3 * 5) / 3
if 0 <= media <= 2.9:
    print('Reprovado')
elif 3 <= media <= 4.9:
    print('Recuperação')
else:
    print('Aprovado')
