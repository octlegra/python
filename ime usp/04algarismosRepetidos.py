print('----------------------------------------')
print('PROCURANDO ALGARISMOS VIZINHOS IGUAIS...')
print('----------------------------------------\n')

print('Vamos brincar de detetive de algarismos?')
x = input('s/n: ')

if x == 'n':
    print('Então vai tomar no cu e chupar meu piru ..|.,')
else:
    print('Ok! Vamos lá...')

n     = int(input('Digite o número que deseja investigar: '))
n2    = n

div   = 1
restAnt  = 99
alg   = False

while (div != 0) and not alg:
    div  = n // 10
    rest = n % 10
    n    = div

    if rest == restAnt:
        alg = True
    else:
        restAnt = rest
    
if alg:
    print('O número [{}] possui algarismos adjacentes repetidos! [algarismo {}]'.format(n2,rest))
else:
    print('O número [{}] não possui algarismos adjacentes repetidos!'.format(n2))
