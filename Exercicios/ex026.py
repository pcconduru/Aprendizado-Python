#Contando e analisando uma sting
p = str(input('Digite o algo: ')).lower().strip()
print('A letra A aparece {} vezes.'.format(p.count('a')))
print('A primeira vez que A aparece é na posição {}.'.format(p.find('a')+1))
print('A última vez que A aparece é na posição {}'.format(p.rfind('a')+1))