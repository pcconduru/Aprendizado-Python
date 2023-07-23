#PA v3.0
n = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
parada = 0
m = 10
cont = 10
while parada != m:
    print('{} → '.format(n), end='')
    n += r
    parada += 1
    if parada == m:
        print('PAUSA')
        m = int(input('Quantos termos você quer mostrar a mais? '))
        cont += m
        parada = 0
print('Progressão finalizada com {} termos mostrados.'.format(cont))