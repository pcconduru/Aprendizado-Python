#Jogo de adivinhação v2.0
from random import randint
nu = 0
nm = randint(1, 10)
palpites = 1
while nu != nm:
    print('-' * 40)
    nu = int(input('Dê seu palpite: '))
    palpites += 1
    if nu != nm:
        if nm > nu:
            print('Mais...Tente mais uma vez!')
        else:
            print('Menos...Tente mais uma vez!')
print('=' * 40)
print('O número da máquina foi {}.\nE a quantidade de palpites para o acerto foi {}.'.format(nm, palpites))
print('Parabéns por sua vitória!!!')
print('=' * 40)