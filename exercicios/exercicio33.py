'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''
#https://wiki.python.org.br/EstruturaSequencial
#Desenvolvido por Ulisses F. Falcão em 30/01/2024

msnNumero1 = 'Digite um número inteiro: '
msnNumero2 = 'Digite outro número inteiro: '
msnNumero3 = 'Digite um número real: '

numero1 = int(input(msnNumero1))
numero2 = int(input(msnNumero2))
numero3 = float(input(msnNumero3))

print('Produto = {}'.format((numero1 * 2) * (numero2 / 2)))
print('Soma = {}'.format((numero1 * 3) + (numero3)))
print('Terceiro Ao Cubo = {}'.format(numero3 ** 3))