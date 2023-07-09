#lista aleatória
from random import shuffle
pa = str(input('Qual o primeiro aluno: '))
sa = str(input('Qual o segundo aluno: '))
ta = str(input('Qual o terceiro aluno: '))
qa = str(input('Qual o quarto aluno: '))
lista = [pa, sa, ta, qa]
shuffle(lista)
print('A ordem dos alunos escolhidos foi: {}'.format(lista))