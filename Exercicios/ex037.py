#Convertendo para Binário, Octal e Hexadecimal
n = int(input('Escolha um número: '))
tipo = int(input('1.Binário\n2.Octal\n3.Hexadecimal\nEscolha um destes para uma conversão: '))
if tipo == 3:
    print('O valor {} convertido para hexadecimal é {}.'.format(n, hex(n)[2:]))
elif tipo == 2:
    print('O valor {} convertido para octal é {}.'.format(n, oct(n)[2:]))
elif tipo == 1:
    print('O valor {} convertido para binário é {}.'.format(n, bin(n)[2:]))
else:
    print('O valor informado não pode ser convertido.')