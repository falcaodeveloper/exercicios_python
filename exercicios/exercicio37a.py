'''Inversão da Ordem do Nome do Usuário
Desenvolva um programa em Python que receba o primeiro e último nome do usuário, e então os imprima em ordem reversa, separados por um espaço.'''
#https://www.usandopy.com/pt/artigo/exercicios-intermediarios-em-python-01/
#Desenvolvido por Ulisses F. Falcão em 13/02/2024

msnNome = 'Digite seu primeiro e último nome:\n'
nome = input(msnNome).strip()

nome = nome.split()

print('{} {}' .format(nome[1], nome[0]))