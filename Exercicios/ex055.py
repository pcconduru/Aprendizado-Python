#Pesagem
p_maior = 0
p_menor = 99999
for pesagem in range(1, 6):
    p_atual = float(input('Qual o peso da {}° pessoa: KG'.format(pesagem)))
    if p_atual > p_maior:
        p_maior = p_atual
    if p_atual < p_menor:
        p_menor = p_atual
print('O maior peso lido foi {}KG.'.format(p_maior))
print('O menor peso lido foi {}KG.'.format(p_menor))