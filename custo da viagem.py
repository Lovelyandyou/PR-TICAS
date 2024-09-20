distancia = float(input(' Qual é a distancia da sua viagem? '))
print('Você está preste a começar uma viagem de {}km'.format(distancia))
preço = distancia *0.50 if distancia <= 200 else distancia * 0.45
print(' É o preço da sua passagem será de R${:.2f}'.format(preço))
