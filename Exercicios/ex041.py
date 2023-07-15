#Confederação
from datetime import datetime
data = int(input('Ano de nascimento: '))
idade = datetime.today().year - data
print('A idade do atleta é {}.'.format(idade))
if idade <= 9:
    print('CLASSIFICAÇÃO: Mirim')
elif 14 >= idade > 9:
    print('CLASSIFICAÇÃO: Infantil')
elif 19 >= idade > 14:
    print('CLASSIFICAÇÃO: Junior')
elif 25 >= idade > 19:
    print('CLASSIFICAÇÃO: Sênior')
elif idade > 25:
    print('CLASSIFICAÇÃO: Master')