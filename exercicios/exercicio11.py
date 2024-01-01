#Operadores: Crie um programa que solicite ao usuário dois números e exiba o resultado da soma, subtração, multiplicação e divisão desses números: https://horadecodar.com.br/exercicios-de-logica-de-programacao-javascript/
#Desenvolvido por Ulisses F Falcão em 29/11/2023

mensagem1 = 'Digite um número: '
mensagem2 = 'Digite outro número: '
numero1 = int(input(mensagem1))
numero2 = int(input(mensagem2))

print('{} + {} = {}' .format(numero1, numero2, numero1 + numero2))
print('{} - {} = {}' .format(numero1, numero2, numero1 - numero2))
print('{} * {} = {}' .format(numero1, numero2, numero1 * numero2))
print('{} / {} = {}' .format(numero1, numero2, numero1 / numero2))