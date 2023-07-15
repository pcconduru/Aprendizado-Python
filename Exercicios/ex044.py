#Meios de pagamento
print('=' * 20)
preço = float(input('Valor da Compra: R$'))
print('''Formas de pagamentos
[1] À vista dinheiro
[2] À vista no cartão
[3] 2 x no cartão
[4] De 3 a 4 x no cartão
''')
print('=' * 20)
opção = int(input('Qual a forma de pagamento? '))
if opção == 1:
  total = preço - (preço * 10 / 100)
  print(f'Sua compra teve um desconto de R${(preço * 10 / 100):.2f}, e valor final é de R${total:.2f}.')
elif opção == 2:
  total = preço - (preço * 5 / 100)
  print(f'Sua compra teve um desconto de R${(preço * 5 / 100):.2f}, e o valor final é de R${total:.2f}.')
elif opção == 3:
  total = preço
  parcela = total / 2
  print(f'Sua compra é de R${preço:.2f} e será paga em 2 parcelas de R${parcela:.2f}.')
elif opção == 4:
  total = preço + (preço * 20 / 100)
  parcela = total / 4
  print(f'Sua compra é de R${preço:.2f}, será parcelada em 4x com acréscimo de R${(preço * 20 / 100):.2f}, totalizando R${(preço + (preço * 20 / 100)):.2f}, com parcelas de R${parcela:.2f}.')
else:
  print('Opção invalida. Digite novamente.')
