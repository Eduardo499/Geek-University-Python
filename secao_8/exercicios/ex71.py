def dentro_ret(x1, y1, x2, y2, p1, p2):
    """Função que recebe as posições do vértice inferior esquerdo e superior direito de um retângulo e retorna 1 caso
    as coordenadas estejam dentro do retângulo, caso contrário retorna 0 """

    if x1 <= p1 <= x2:
        if y1 <= p2 <= y2:
            return 1

    return 0


coordenada_x1 = int(input('\nDigite a coordenada x do vértice inferior esquerdo do retângulo: '))
coordenada_y1 = int(input('Digite a coordenada y do vértice inferior esquerdo do retângulo: '))

coordenada_x2 = int(input('\nDigite a coordenada x do vértice superior direito do retângulo: '))
coordenada_y2 = int(input('Digite a coordenada y do vértice superior direito do retângulo: '))

coordenada_p1 = int(input('\nDigite a coordenada x do ponto: '))
coordenada_p2 = int(input('Digite a coordenada y do ponto: '))

print(f'\n{dentro_ret(coordenada_x1, coordenada_y1, coordenada_x2, coordenada_y2, coordenada_p1, coordenada_p2)}')
