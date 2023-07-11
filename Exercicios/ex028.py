#Jogo de adivinhação v1.0
import random
nu = int(input('Digite um número: '))
nl = [0, 1, 2, 3, 4, 5]
nm = random.choice(nl)
if nu == nm:
    print('Párabens, você ganhou!')
else:
    print('Mais sorte da próxima vez, você perdeu')
print('número sorteado pela máquina: {}'.format(nm))