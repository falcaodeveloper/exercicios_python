#Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o seu volume (v = 4/3.P .R³): https://www.computersciencemaster.com.br/exercicios-funcoes/
#Desenvolvido por Ulisses F. Falcão em 06/12/2023

import math

mensagem = 'Digite o raio da esfera para saber o volume:\n'
pi = math.pi

raio = float(input(mensagem))
volume = 4 / 3 * pi * raio ** 3

print('O volume é: {}' .format(volume))