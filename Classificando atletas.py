from datetime import date

atual = date.today().year

nascimento = int(input('Ano de Nascimento: '))
idade  = atual - nascimento
print('O atetla tem {} anos.'.format(idade))
if idade <=9:
    print('Classificação: Mirim')
elif idade <= 14:
    print('classificação: Infantil')
elif idade <= 19:
    print('Classificação: Junior')
elif idade <= 25:
 print('Classificação: Sênior')

else:
    print('Classificação: Master')