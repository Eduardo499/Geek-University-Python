n = int(input('Digite um número: '))

s1 = 0
s2 = 0
s3 = 0

for i in range(1, n + 1):
    s1 += i
    if i % 2 == 1:
        s3 += i
    elif i % 2 == 0:
        s2 -= i

s2 += s3

print(f'Primeira sequência: {s1}')
print(f'Segunda sequência: {s2}')
print(f'Terceira sequência: {s3}')
