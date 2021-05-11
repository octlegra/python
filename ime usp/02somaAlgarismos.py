print('-------------------------------')
print('SOMANDO ALGARISMOS DE UM NÚMERO')
print('-------------------------------')
print(' ')

print('Vou somar os algarismos do número inteiro que você digitar.')
n = int(input('Digite um número qualquer: '))

n2   = n
div  = 1
rest = 0
soma = 0

while (div != 0):
    div  = n // 10
    rest = n % 10
    n    = div
    soma = soma + rest

print('A soma dos algarismos de [{}] é: {}'.format(n2,soma))
