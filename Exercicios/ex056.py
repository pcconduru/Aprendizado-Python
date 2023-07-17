#Analisador Completo
mi = 0
mn = 0
ijunta = 0
cont_m = 0
med = 0
for analisador in range(1, 5):
    print('=' * 7, '{}° Pessoa'.format(analisador), '=' * 7)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).upper()
    ijunta += idade
    med = ijunta / 4
    if idade > mi and sexo == 'M':
        mi = idade
        mn = nome
    if sexo == 'F' and idade <= 19:
        cont_m += 1
print('A média de idade do grupo é de {} anos'.format(med))
print('O homem mais velho tem {} e se chama {}.'.format(mi, mn))
print('Ao todo são {} mulheres com menos de 20 anos'.format(cont_m))