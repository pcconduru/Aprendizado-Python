#PA V2.0
n = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
parada = 0
while parada != 10:
    print('{} → '.format(n), end='')
    n += r
    parada += 1
print('ACABOU!')