c = int(input('Digite o comprimento do terreno em metros: '))
l = int(input('Digite a largura do terreno em metros: '))
p = int(input('Digite o preço do metro quadrado da tela: '))
area = c * l
print(f'Para cobrir com tela {area} m² é preciso de R$ {area * p}')
