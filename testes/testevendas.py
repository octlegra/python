print('---------------------------')
print('AUDITORIA DA LOJA DE DISCOS')
print('---------------------------')
print(' ')

maior_venda = int
dia         = int

i           = 1
maior_venda = 0
  
while i <= 5:

    qtd_vendida = int(input("Informe a quantidade de discos vendidos: "))

    if(qtd_vendida > maior_venda):
        maior_venda = qtd_vendida 
        dia = i
        
    i += 1; 

print("A maior quantidade de discos vendidos foi: {} discos".format(maior_venda))
print("A maior quantidade de vendas foi feita dia: {}/MAR".format(dia))
