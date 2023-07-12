#Analisando Triangulos v1.0
from time import sleep
print('=' * 24)
print('Analisador de Triângulos')
print('=' * 24)
l1 = float(input('Linha-1: '))
l2 = float(input('Linha-2: '))
l3 = float(input('Linha-3: '))
print('ANALISANDO...')
sleep(1.5)
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print('Com os valores aplicados SE CONSEGUE formar um triângulo.')
else:
    print('Com os valores aplicados NÃO SE CONSEGUE formar um triângulo.')
