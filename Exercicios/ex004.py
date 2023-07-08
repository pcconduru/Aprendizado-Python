#Dissecando Váriavel
x = input('Digite algo:')
print('Tipo primitivo:', type(x))
print('É um númerico:', x.isnumeric())
print('É um alpha:', x.isalpha())
print('É um AlphaNúmerico:', x.isalnum())
print('É maiúscula:', x.isupper())
print('É minúscula:', x.islower())
print('É capitalizado:', x.istitle())