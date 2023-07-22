#Calculo de fatorial
from math import factorial
num = int(input('Digite o valor a ser calculado: '))
n = num
while n > 0:
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    n -= 1
print(factorial(num))