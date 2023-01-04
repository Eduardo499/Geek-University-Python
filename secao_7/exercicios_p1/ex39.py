n = int(input('Digite um número: '))

if n > 0:
    linha = list(range(n + 1))

    for i in linha:
        print(f'Linha {i}: ', end=' ')
        for j in range(0, i + 1):

            if j == 0 or j == i:
                print(1, end='  ')
            else:
                n_fatorial = 1
                p_fatorial = 1

                for c in range(1, i + 1):
                    n_fatorial *= c

                for k in range(1, j + 1):
                    p_fatorial *= k

                n_p_factorial = i - j

                resultado_denominador = 1

                for l in range(1, n_p_factorial + 1):
                    resultado_denominador *= l

                denominador = p_fatorial * resultado_denominador

                resultado_final = int(n_fatorial / denominador)
                print(resultado_final, end='  ')
        print()

else:
    print('Digite um número maior que zero.')
