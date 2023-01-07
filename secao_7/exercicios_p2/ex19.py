alunos = []
matriculas = []
cont1 = 0

while len(alunos) < 5:
    lista2 = []
    cont2 = 0

    while len(lista2) < 3:
        if cont2 == 0:
            matricula = int(input(f'Digite o número da matrícula do aluno {cont1 + 1}: '))

            if matricula not in matriculas:
                matriculas.append(matricula)
                lista2.append(matricula)
            else:
                print('Matrícula já digitada')
                cont2 -= 1
                pass
        elif cont2 == 1:
            media_prova = int(input(f'Digite a média das provas do aluno {cont1 + 1}: '))
            lista2.append(media_prova)
        elif cont2 == 2:
            media_trabalho = int(input(f'Digite a média dos trabalhos do alunos {cont1 + 1}: '))
            lista2.append(media_trabalho)

        cont2 += 1
    cont1 += 1
    alunos.append(lista2)
    print()

for i in range(5):
    nota_final = alunos[i][1] + alunos[i][2]
    alunos[i].append(nota_final)

for i in range(5):
    for j in range(4):
        print(f"{alunos[i][j]}", end=' ')
    print()

notas_finais = []

for i in range(5):
    notas_finais.append(alunos[i][3])

soma_final = sum(notas_finais)
matricula = 0

for i in range(5):
    if alunos[i][3] == max(notas_finais):
        matricula = alunos[i][0]

media = int(soma_final) / len(notas_finais)

print()

print(f'Matrícula do aluno com a maior nota final: {matricula}')
print(f'A média aritmética das notas finais: {media}')
