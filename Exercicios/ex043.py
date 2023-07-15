#Calculo IMC
peso = float(input('Qual o seu peso: (KG) '))
altura = float(input('Qual a sua altura: (m) '))
imc = peso / (altura ** 2)
print('O IMC desta pessoa é igual a {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está Abaixo do Peso.')
elif 18.5 <= imc < 25.0:
    print('Parabéns, você está no Peso Ideal.')
elif 25.0 <= imc < 30.0:
    print('Você está em Sobrepeso.')
elif 30.0 <= imc < 40.0:
    print('Você está em Obesidade.')
else:
    print('Você está em Obesidade Mórbida, Procure um médico!')