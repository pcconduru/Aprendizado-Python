#Menu de opções
from time import sleep
parada = 0
v1, v2 = 0, 0
while not parada == 1:
    r = 0
    v1 = float(input('Primeiro valor: '))
    v2 = float(input('Segundo valor: '))
    print('=-=' * 10)
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    op = int(input('>>>>> Qual é sua opção? '))
    if op == 1:
        r = v1 + v2
        print('A soma entre {} e {} é {}'.format(v1, v2, r))
    elif op == 2:
        r = v1 * v2
        print('O valor {} multiplicado por {} é {}'.format(v1, v2, r))
    elif op == 3:
        if v1 > v2:
            print('O maior valor entre {} e {} é {}'.format(v1, v2, v1))
        elif v2 > v1:
            print('O maior valor entre {} e {} é {}'.format(v2, v1, v2))
        else:
            print('Os valores são iguais, assim o maior número é {}'.format(v1 or v2))
    elif op == 4:
        print('Certo, informe os novos valores.')
    elif op == 5:
        parada = 1
    print('=-=' * 10)
    sleep(2)