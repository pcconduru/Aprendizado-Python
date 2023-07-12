n1 = int(input('1.'))
n2 = int(input('2.'))
n3 = int(input('3.'))
maior = n1
menor = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print('O maior número é {}.'.format(maior))
print('O menor número é {}.'.format(menor))