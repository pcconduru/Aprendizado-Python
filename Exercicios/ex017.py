#Hipotenusa Calculo
from math import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hi = hypot(co, ca)
print('O valor da hipotenusa: {:.1f}'.format(hi))