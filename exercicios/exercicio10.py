#Variáveis e tipos de dados: Escreva um programa que declare duas variáveis, “nome” e “idade”, e as imprima em um console em uma frase que diga “Olá, meu nome é [nome] e eu tenho [idade] anos”: https://horadecodar.com.br/exercicios-de-logica-de-programacao-javascript/
#Desenvolvido por Ulisses F Falcão em 29/11/2023

nome = input('Por favor, digite seu nome: ')
idade = input('Digite sua idade: ')

print('Olá, meu nome é {} e eu tenho {} anos.' .format(nome, idade))