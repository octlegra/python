print('-----------------------------')
print('SOLUÇÕES EQUAÇÃO SEGUNDO GRAU')
print('-----------------------------')
print(' ')

a = float(input('Qual o valor de a? '))
b = float(input('Qual o valor de b? '))
c = float(input('Qual o valor de c? '))

delta = b**2 - 4*a*c
e = delta**0.5
r = -b / (2*a)
r1 = (-b + e) / (2*a)
r2 = (-b - e) / (2*a)

if delta < 0:
    print('Não há raízes reais para esta equação')

if delta == 0:
    print('A única raiz real para esta equação é ', r)

if delta > 0:
    print('A primeira raiz real é ', r1) 
    print('A segunda raiz real é ', r2)
