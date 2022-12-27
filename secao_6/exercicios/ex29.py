from math import factorial

s = 0

for i in range(1, 6):
    s = i / factorial(2 * i)
print(s)
