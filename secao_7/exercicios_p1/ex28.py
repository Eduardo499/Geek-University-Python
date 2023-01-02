v = []
v1 = []
v2 = []

for c in range(10):
    v.append(int(input(f'Digite um número na posição {c}: ')))

for i in v:

    if i % 2 == 1:
        v1.append(i)
    else:
        v2.append(i)

print()
print(v1)
print(v2)
