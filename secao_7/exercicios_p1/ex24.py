alunos = []

for c in range(3):
    alunos.append(int(input(f'Digite a altura do aluno {c}: ')))

print()
print(f'O maior aluno é o número {alunos.index(max(alunos))} e ele mede {max(alunos)} metros')
print(f'O menor alunos é o número {alunos.index(min(alunos))} e ele mede {min(alunos)} metros')
