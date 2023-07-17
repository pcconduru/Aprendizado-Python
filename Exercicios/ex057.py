#Validação de dados
sexo = 0
while sexo != "M" and sexo != "F":
    sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()
    if sexo != "M" and sexo != "F":
        print('Dados inválidos. Porfavor insira seus dados corretamente.')
print('Sexo registrado com sucesso!')