print('-------------------------')
print('DETERMINAR NÚMEROS PRIMOS')
print('-------------------------\n')

n = int(input('Digite um número inteiro para checar se é um número primo: '))

i     = 2
primo = True

while i < n and primo:
    x = n % i
    if x == 0:
        primo = False
    else:
        i += 1

if primo:
    print('O número digitado é primo!')
else:
    print('O número digitado não é primo...')
    print('Ele também pode ser dividido por {}, por exemplo.'.format(i))
