#Tratando vários valores v1.0
n, soma, cont = 0, 0, 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    soma += n
    cont += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont - 1, soma - 999))