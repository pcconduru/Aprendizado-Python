#Algoritimo Aleatório
import random
pa = str(input('Primeiro aluno: '))
sa = str(input('Segundo aluno: '))
ta = str(input('Terceiro aluno: '))
qa = str(input('Quarto aluno: '))
list = pa,sa,ta,qa
print('O aluno sorteado foi: {}'.format(random.choice(list)))