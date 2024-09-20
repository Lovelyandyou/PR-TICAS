r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceito segmento: '))

print('-=-' * 20)
print('Analisador do Triângulo')
print('-=-' * 20)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print(' Os segmento acima podem formar triângulo! ')
else:
    print('Os segmentos acima  não podem forma triângulos!')