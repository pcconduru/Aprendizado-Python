#Tábuada v3.0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n >= 0:
        v = r = 0
        print('=' * 35)
        for tab in range(10):
            v += 1
            r = v * n
            print(f'{v} x {n} = {r}')
        print('=' * 35)
    else:
        break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')