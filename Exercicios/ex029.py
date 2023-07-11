#Radar eletrônico
velocidade = int(input('Qual é a velocidade do carro: '))
limite = 80
multa = 7
if velocidade > limite:
    print('MULTADO, seu carro ultrapassou o limite permitido de 80KM/h.')
    print('VALOR DA MULTA A SER PAGO: R${}'.format((velocidade - limite) * multa))
print('Está tudo okay!, você segue o limite permitido da via.')