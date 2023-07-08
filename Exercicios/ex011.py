#Algoritimo de pintor
largura = float(input('Defina a largura:'))
altura = float(input('Defina a altura:'))
área = largura*altura
pin = área / 2
print('Sua parede tem uma dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, área))
print('Para pintar uma parede com essas proporções é necessário {} litros de tinta'.format(pin))