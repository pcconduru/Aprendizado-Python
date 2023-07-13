#Empréstimo
casa = float(input('Qual o valor da casa: R$'))
salário = float(input('Quanto você ganha de salário: R$'))
tempo = float(input('Tempo de financiamento: '))
prestação = (casa / 12) / tempo
print('Financiando por {:.0f} anos, uma casa com o valor R${:.2f}, a prestação mensal será R${:.2f}'.format(tempo, casa, prestação))
if salário < prestação - (30/100):
    print('Empréstimo negado.')
else:
    print('Empréstimo aprovado!')