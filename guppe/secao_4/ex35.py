from math import sqrt
c_oposto = int(input('Digite o comprimento do cateto oposto em metros: '))
c_adjacente = int(input('Digite o comprimento do cateto adjacente em metros: '))
hipotenusa = sqrt(c_oposto ** 2 + c_adjacente ** 2)
print(f'A hipotenusa desse triângulo retângulo é {hipotenusa} metros')
