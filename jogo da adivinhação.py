from random import randint

computador = randint (0, 5)
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5. Tente Adivinhar...')
print('-=-' *20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO....')

if jogador == computador:
    
    print('Parabéns! você conseguiu me vencer!')
    
else:
    print(' Ganhei! eu pensei no número {} e não no {}'.format(computador, jogador))
    

