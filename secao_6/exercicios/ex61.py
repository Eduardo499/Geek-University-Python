for i in range(999, 100, -1):
    palindromo = ''

    for j in range(i, 100, -1):
        palindromo = str(i * j)

        if palindromo == palindromo[::-1]:
            break
    if palindromo == palindromo[::-1]:
        print(palindromo)
        break
