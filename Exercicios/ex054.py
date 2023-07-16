#Grupo da maior idade
from datetime import datetime
nasc = 0
valorx = 0
valory = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}° pessoa nasceu?: '.format(c)))
    nasc = datetime.today().year - ano
    if nasc >= 18:
        valorx += 1
    else:
        valory += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(valorx))
print('E tivemos {} pessoas menores de idade'.format(valory))