from math import sqrt
a = float(input('Digite o valor do coeficiente a: '))
b = float(input('Digite o valor do coeficiente b: '))
c = float(input('Digite o valor do coeficiente c: '))
delta = (b ** 2) - 4 * a * c
if delta < 0:
    print('Não existe raiz real!')
elif delta == 0:
    print('Raiz única!')
    print(f'x = {(-b + sqrt(delta)) / 2 * a}')
elif delta > 0:
    print('Existem duas raízes!')
    print(f"""x' = {(-b + sqrt(delta)) / 2 * a} \nx" = {(-b - sqrt(delta)) / 2 * a}""")
