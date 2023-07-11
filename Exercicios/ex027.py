#Discecando um nome
nome = str(input('Escreva seu nome: '))
n = nome.split()
print('Seu primeiro nome é {}.'.format(n[0]))
print('Seu último nome é {}.'.format(n[len(n)-1]))