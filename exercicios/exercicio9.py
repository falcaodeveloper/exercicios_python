#Tabuada de um número: Crie um programa que peça ao usuário para inserir um número e imprima a tabuada desse número: https://horadecodar.com.br/exercicios-de-logica-de-programacao/
#Desenvolvido por Ulisses F Falcão em 29/11/2023

mensagem = 'Digite um número para saber sua tabuada: '
numero = int(input(mensagem))
cont = 1

while cont <= 10:
    print('{} x {} = {}' .format(numero, cont, numero * cont))
    cont += 1