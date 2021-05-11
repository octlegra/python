print('-----------------------------')
print('##### APRENDENDO PYTHON #####')
print('-----------------------------')
print(' ')
nome = input('Primeiramente... Qual é o seu nome? ')
print('Olá {}! Gratidão por conhecer meu primeiro programa em Python!'.format(nome))
idade = input('Quantos anos você tem? ')
print('Que bacana! Então você tem {} anos. Eu tenho 30!'.format(idade))
dia = input('Me conte um pouco mais: que dia você nasceu? ')
mes = input('De qual mês? ')
ano = input('E o ano? ')
print('Ah, entendi! Você é de {}/{}/{}! Vou me lembrar disso!'.format(dia, mes, ano))
num1 = int(input('Agora vamos brincar de matemática! Diga um número qualquer: '))
num2 = int(input('Escolha outro número: '))
num3 = num1+num2
num4 = num1-num2
num5 = num1*num2
num6 = num1/num2
print('Hummm... Acho que a soma desses números é', num3)
print('E a diferença desses números é', num4)
print('Vou mais longe! O produto desses números é', num5)
print('E, por fim, a divisão desses números é', num6)
print('Espero que eu tenha acertado dessa vez! Volte sempre {}! :)'.format(nome))
