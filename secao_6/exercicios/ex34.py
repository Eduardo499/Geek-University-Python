cont = 0
menor = 0

for i in range(1, 99999999):

    for j in range(1, 21):
        if i % j == 0:
            cont += 1

        if cont >= 15:
            menor = i

    if menor > 0:
        print(menor)
        break
    cont = 0
