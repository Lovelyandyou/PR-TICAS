salario = float(input('qual é o seu salario R$ ? '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
   novo = salario + (salario * 10 / 100)
print('Quem ganha R${:.2F} passa a ganhar R${:.2f} agora'.format(salario, novo))   