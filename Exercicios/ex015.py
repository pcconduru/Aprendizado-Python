#Alugando Carros
d = float(input('Quantos dias foram alugados?:'))
km = int(input('Quantos Km foram rodados?:'))
pgd = d*60
pgkm = km*0.15
print('O total a pagar é de: R${}'.format(pgd+pgkm))