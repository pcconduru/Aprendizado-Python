#Multiplos de três
s = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        count = count + 1
        s = s + c
print('A soma entre todos os {} valores solicitados é {}'.format(count, s))