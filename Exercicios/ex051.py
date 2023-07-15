#PA
num = int(input('Primero Termo: '))
r = int(input('Razão: '))
décimo = num + (10 - 1) * r
for c in range(num, décimo + r, r):
    print(c, end=" → ")
print('ACABOU!')