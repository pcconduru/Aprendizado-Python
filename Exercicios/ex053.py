#palindromo
frase = str(input("Digite uma frase:  "))
frase1 = ''
frase2 = ''

for i in range(len(frase)):
    if frase[i] != ' ':
        frase1 = frase1 + frase[i]
        frase1 = frase1.upper()

for i in range(-1, -len(frase) - 1, -1):
    if frase[i] != ' ':
        frase2 = frase2 + frase[i]
        frase2 = frase2.upper()

if frase1 == frase2:
    print('A frase é um plaíndromo')
else:
    print('A frase não é um palíndromo')