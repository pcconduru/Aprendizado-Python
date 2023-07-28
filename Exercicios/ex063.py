#Sequência de fibonacci v1.0
print('-' * 20)
print('Sequência de Fibonacci')
print('-' * 20)
n = int(input('Quantos termos você quer mostrar? '))
print('~' * 20)
cont = 3
t1, t2 = 0, 1
print('{} → {}'.format(t1, t2), end='')
while cont <= n:
    t3 = t1 + t2
    print('→ {}'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('→ FIM!')