#Promoção
produto = float(input('Qual o valor do produto?: R$'))
desconto = (produto * 5) / 100
print('O valor do seu produto após o desconto de 5% será: R${}'.format(produto - desconto))