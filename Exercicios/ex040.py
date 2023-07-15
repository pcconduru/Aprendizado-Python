#Notas v2.0
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f} a média do aluno é {:.1f}'.format(n1, n2, media))
if media >= 7:
    print('O aluno está APROVADO.')
elif 5 <= media <= 6.9:
    print('O aluno está de RECUPERAÇÃO.')
elif 0 <= media <= 4.9:
    print('O aluno está REPROVADO.')