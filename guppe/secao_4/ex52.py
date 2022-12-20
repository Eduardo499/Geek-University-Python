n1 = int(input('Digite o valor pago pelo primeiro amigo: '))
n2 = int(input('Digite o valor pago pelo segundo amigo: '))
n3 = int(input('Digite o valor pago pelo terceiro amigo: '))
premio = int(input('Digite o valor do prêmio: '))
total = n1 + n2 + n3
total_n1 = n1 / total
total_n2 = n2 / total
total_n3 = n3 / total
print(f"""O primeiro amigo irá receber {total_n1 * premio} reais;
O segundo amigo irá receber {total_n2 * premio} reais;
O terceiro amigo irá receber {total_n3 * premio} reais.
""")
