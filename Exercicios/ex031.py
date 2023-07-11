#Velocidade e valor
distância = int(input('Qual é a distância da viagem: '))
valor = distância * 0.50
if distância > 200:
    valor = distância * 0.45
print('O valor a ser pago para seguir a viagem é R${}'.format(valor))