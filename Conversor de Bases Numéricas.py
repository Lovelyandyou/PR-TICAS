base = int(input('Digite um número inteiro: '))
print('''Escolha uma das basespara conversão:
[1] converter em Binário
[2] converter em Octal
[3] converter para Hexadecimal''')

opção = int(input('Sua opção:'))

if opção  == 1:
     print('{} convertido para Binário é igual a {}'.format(base, bin(base)[2:]))
elif opção == 2:
    print('{} convertido para Octal é igual a {}'.format(base,oct(base)[2:]))
elif opção == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(base,hex(base)[2:]))

else:
    print('Opção invalida')