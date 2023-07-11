#Separando digitos de um número
n = int(input('Escolha um número: '))
int = str(n)
print('unidade: {}'.format(int[3]))
print('dezena: {}'.format(int[2]))
print('centena: {}'.format(int[1]))
print('milhar: {}'.format(int[0]))