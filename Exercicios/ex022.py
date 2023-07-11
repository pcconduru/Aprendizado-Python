#Manipulando Sting para nome
nome = str(input('Digite seu nome completo: '))
primeiro = nome.split()
print('Maiusculo: {}'.format(nome.upper()))
print('Minusculo: {}'.format(nome.lower()))
print('Quantidade de letras do nome: {}'.format(len(nome) - nome.count(' ')))
print('O seu nome é {} e ele tem ao todo {} letras'.format(primeiro[0], len(primeiro[0])))