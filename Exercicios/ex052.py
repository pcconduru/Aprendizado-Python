#Número Primo
colors = {
    'Default':'\033[m',
    'Red':'\033[31m',
    'Yellow':'\033[33m',
    'Green':'\033[32m',
    'Reverse':'\033[7:30:47m',
}

n = int(input('Digite um número inteiro: '))
x = 0
count = 0
if n > 0:
    for c in range(1, n+1):
        x = n % c
        if x == 0:
            print(f'{colors["Green"]}{c}{colors["Default"]}', end=' ')
            count += 1
        else:
            print(f'{colors["Red"]}{c}{colors["Default"]}', end=' ')
print(f'\nSeu número foi divído {count} VEZES.')
if count <= 2:
    print(f'O {n} É UM NÚMERO PRIMO')
else:
    print(f'O {n} NÃO É UM NÚMERO PRIMO')