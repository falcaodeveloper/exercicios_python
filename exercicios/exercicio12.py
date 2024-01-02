#Funções: Escreva uma função que aceite dois números como argumentos e retorne sua soma: https://horadecodar.com.br/exercicios-de-logica-de-programacao-javascript/
#Desenvolvido por Ulisses F. Falcão em 05/12/2023

mensagem1 = 'Digite um valor: '
mensagem2 = 'Digite outro valor: '
a = float(input(mensagem1))
b = float(input(mensagem2))

def soma(a, b):
    return a + b

print(soma(a, b))