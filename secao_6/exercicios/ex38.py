for i in range(1, 1000):
    a = 0
    b = 0
    c = 0
    for j in range(1, 1000):
        a = j
        b = i
        c = (a ** 2 + b ** 2) ** 0.5

        if b > a:
            if (a + b + c) == 1000:
                print(f'a: {a}')
                print(f'b: {b}')
                print(f'c: {int(c)}')
