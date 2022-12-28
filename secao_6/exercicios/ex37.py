soma = 0

for i in range(1000, 10000):
    num = str(i)
    soma = int(num[0] + num[1]) + int(num[2] + num[3])

    if soma ** 2 == i:
        print(i)
