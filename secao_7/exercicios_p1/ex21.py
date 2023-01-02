a = []
b = []
c = []

for i in range(1, 11):
    n1 = int(input(f'Digite o {i}° número para a lista A: '))
    n2 = int(input(f'Digite o {i}° número para a lista B: '))
    a.append(n1)
    b.append(n2)

for j in range(10):
    c.append(a[j] - b[j])

print()
print(c)
