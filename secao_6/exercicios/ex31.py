s = 0

numerador = range(1, 100, 2)
denominador = range(1, 51)

for i in range(0, 50):
    s += numerador[i] / denominador[i]

print(s)
