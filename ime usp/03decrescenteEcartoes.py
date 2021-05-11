print('--------------------------------------')
print('DETERMINANDO UMA SEQUÊNCIA DECRESCENTE')
print('--------------------------------------\n')

print('Vou avaliar se uma sequência tem apenas números em ordem decrescente.\n')

decrescente = True
n     = int(input('Digite o primeiro número da sequência: '))
valor = 1
    
while (valor != 0) and decrescente:
    valor = int(input('Digite o próximo número da sequência, ou [0] se já tiver terminado: '))
    if valor > n:
        decrescente = False
    n = valor

if decrescente:
    print('A sequência está em ordem decrescente! =) \n\n')
else:
    print('A sequência não está em ordem decrescente! =( \n\n')


print('------------------------------------------')
print('ENCONTRANDO SEU CARTÃO DE CRÉDITO NA LISTA')
print('------------------------------------------\n')

meuCartão  = int(input('Digite o número do seu cartão de crédito: '))

novoCartão = 1
encontreiMeuCartão = False

while (novoCartão != 0) and not encontreiMeuCartão:
    novoCartão = int(input('Digite o número do cartão que você quer comparar, ou [0] se já tiver terminado: '))
    if novoCartão == meuCartão:
        encontreiMeuCartão = True

if encontreiMeuCartão:
    print('Encontramos seu cartão nesta lista!')
else:
    print('Não encontramos seu cartão entre os números digitados.')
