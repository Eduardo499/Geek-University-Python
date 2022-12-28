soma_quadrados = 0
quadrado_somas = 0

for i in range(1, 101):
    soma_quadrados += i ** 2
    quadrado_somas += i

quadrado_somas = quadrado_somas ** 2

print(f'Soma dos quadrados: {soma_quadrados} \nQuadrado das somas: {quadrado_somas}')
print(f'A diferença entre a soma dos quadrados e o quadrado da soma é {quadrado_somas - soma_quadrados}')
