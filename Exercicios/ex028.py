#Jogo de adivinhação v1.0
from random import randint
from time import sleep
print('-=-' * 20)
print('JOGO DE ADIVINHAÇÃO, ESCOLHA UM NÚMERO ENTRE 0 e 5')
print('-=-' * 20)
nu = int(input('Digite um número: '))
nm = randint(0, 5)
print('PROCESSANDO...')
sleep(2.5)
if nu == nm:
    print('Párabens, você ganhou!')
else:
    print('Mais sorte da próxima vez, você perdeu')
print('número sorteado pela máquina: {}'.format(nm))