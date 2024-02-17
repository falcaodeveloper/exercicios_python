'''Escreva um programa em Python para encontrar números entre 2000 e 3200 (inclusive) que são divisíveis por 7, mas não são múltiplos de 5. Exiba os números em uma sequência separada por vírgulas em uma única linha.
Saída Esperada:
2002, 2009, 2016, 2023, ... (todos os números que atendem às condições)'''
#https://www.usandopy.com/pt/artigo/exercicios-intermediarios-em-python-01/
#Desenvolvido por Ulisses F. Falcão em 13/02/2024

cont = 2000
valores = list()

while cont <= 3200:
    resto = cont % 7
    if resto == 0:
        resto = cont % 5
        if resto != 0:
            valores.append(cont)
    cont += 1

print(valores)