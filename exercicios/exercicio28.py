# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre o mais barato: https://www.computersciencemaster.com.br/exercicios-if-e-else/
#Desenvolvido por Ulisses F. Falcão em 10/01/2024

mensagem = 'Informe o preço dos produtos.'
mensagem1 = 'Preço 1: '
mensagem2 = 'Preço 2: '
mensagem3 = 'Preço 3: '
mensagem4 = 'Compre o produto com o preço {:.2f}'
print(mensagem)
preco1 = float(input(mensagem1))
preco2 = float(input(mensagem2))
preco3 = float(input(mensagem3))
if preco1 < preco2 and preco1 < preco3:
    print(mensagem4.format(preco1))
elif preco2 < preco1 and preco2 < preco3:
    print(mensagem4.format(preco2))
elif preco3 < preco1 and preco3 < preco2:
    print(mensagem4.format(preco3))