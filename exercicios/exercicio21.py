#Faça um programa que leia uma string e armazene-a invertida em outra string. Utilize uma estrutura de repetição para varrer e imprimir a nova string: https://www.respondeai.com.br/conteudo/strings/exercicios/faca-programa-leia-string-armazenea-invertida-outra-string-utilize-estrutura-10901
#Desenvolvido por Ulisses F. Falcão em 29/12/2023

mensagem = 'Digite um nome ou uma frase:'
texto = input('{}\n' .format(mensagem)).strip()
caracteres = len(texto)
cont = caracteres - 1
string = ''

while cont >= 0:
    string += texto[cont]
    cont -= 1
print(string)