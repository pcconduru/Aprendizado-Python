#Alistamento
import datetime
from datetime import datetime
data = int(input('Ano de nascimento: '))
idade = datetime.today().year - data
print('Quem nasceu no ano {} hoje tem {} anos.'.format(data, idade))
if idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(datetime.today().year - (idade-18)))
elif idade < 18:
    print('Ainda faltam {} anos pro alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format((idade - 18) - datetime.today().year))
else:
    print('Você deve se alistar.')
    print('Seu prazo é até 31/12')