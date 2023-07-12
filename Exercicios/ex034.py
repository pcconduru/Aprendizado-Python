#Aumento salárial proporcional
salário = float(input('Escreva o salário que determinaremos um aumento: R$'))
if salário >= 1250:
    salário = salário * (10 / 100) + salário
else:
    salário = salário * (15/100) + salário
print('O valor do salário com reajuste fica R${}'.format(salário))