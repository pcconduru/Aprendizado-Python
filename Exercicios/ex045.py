# JOKENPÔ
from random import choice
from time import sleep
escolha = int(input('Suas escolhas: \n[ 0 ]Pedra\n[ 1 ]Papel\n[ 2 ]Tesoura\nQual é a sua jogada? '))
lista = 'Pedra', 'Papel', 'Tesoura'
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!')
maquina = choice(lista)
print('=-=' * 20)
print('A máquina escolheu {}\nO jogador escolheu {}'.format(maquina, lista[escolha]))
print('=-=' * 20)
if maquina == lista[escolha]:
    print('O JOGO DEU EMPATE!')
elif maquina == 'Pedra' and escolha == 1:
    print('Papel ganha de pedra, O jogador ganhou!')
elif escolha == 0 and maquina == 'Papel':
    print('Papel ganha de pedra, A máquina ganhou!')
elif maquina == 'Tesoura' and escolha == 1:
    print('Tesoura ganha de Papel, A máquina ganhou!')
elif escolha == 2 and maquina == 'Papel':
    print('Tesoura ganha de Papel, O jogador ganhou!')
elif maquina == 'Pedra' and escolha == 2:
    print('Pedra ganha de tesoura, A máquina ganhou!')
elif escolha == 0 and maquina == 'Tesoura':
    print('Pedra ganha de tesoura, O jogador ganhou!')