#Estatisticas em produtos
txtInicio = '\033[35;41;1m'
txtFim = '\033[35;47m'
txtSem = '\033[0m'

print(f'{txtInicio}Lista de Compras{txtSem}')
print('-=-' * 15)

preco = contador = produto = qtd1k = baratoNome = vlrTotal = 0
sair = "S"

while sair not in 'N':
    produto = input('Nome do produto: ')
    preco = float(input('Preço do Produto: R$'))
    sair = input('Deseja continuar? [S/N] ').upper().strip()[0]
    while sair not in "NS":
        print('Opção invalida. Digite novamente:')
        sair = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print('-=-' * 7)

    vlrTotal += preco
    contador += 1

    if preco > 999.99:
        qtd1k += 1
    aguarde = preco

    if contador == 1:
        baratoPreco = preco
        baratoNome = produto
    else:
        if preco < baratoPreco:
            baratoPreco = preco
            baratoNome = produto

print('-=-' * 15)
print(f'{txtFim}Compra finalizada...{txtSem}')
print(f'''{contador} produtos adicionados. Valor total da compra = R${vlrTotal:.2f}
{qtd1k} produtos ultrapassam R$1.000,00.
{baratoNome} é o produto mais barato e custa R${baratoPreco:.2f}.''')