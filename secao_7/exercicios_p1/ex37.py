a = []
vetor = []

for i in range(10):
    a.append(int(input('Digite um número: ')))

a.sort()
vetor += a[0:6].copy()

a.reverse()
vetor += a[0:5].copy()

print()
print(vetor)
