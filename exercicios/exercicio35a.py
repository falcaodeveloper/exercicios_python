'''Criação de um Padrão com Laços de Repetição Aninhados:
    Implemente um programa em Python utilizando laços de repetição aninhados para criar o seguinte padrão:'''
#https://www.usandopy.com/pt/artigo/exercicios-intermediarios-em-python-01/

cont = 1
while cont <= 5:
    print('* ' * cont)
    cont += 1
    if cont == 6:
        cont = 5
        while cont >= 1:
            print('* ' * (cont - 1))
            cont -= 1
        break