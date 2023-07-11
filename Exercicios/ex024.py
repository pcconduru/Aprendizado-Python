#Conferindo uma sting
c = str(input('Escolha o nome de uma cidade: '))
print('O nome da cidade contém SANTO: {}'.format(c[:5].upper() == "SANTO"))