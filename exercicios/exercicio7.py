#Cálculo do fatorial de um número: Crie um programa que peça ao usuário para inserir um número e calcule o fatorial desse número: https://horadecodar.com.br/exercicios-de-logica-de-programacao/
#O que é Fatorial: https://www.todamateria.com.br/fatorial/
#Desenvolvido por Ulisses F Falcão em 29/11/2023

valorNegativo = 'O valor não pode ser "negativo"'
mensagem1 = 'Por favor, digite um número inteiro e positivo: '
mensagem2 = 'O fatorial de {} é {}.'

numero = int(input(mensagem1))
cont = numero
fatorial = numero

if numero < 0:
    print(valorNegativo)
elif numero == 0:
     fatorial = 1
     print(mensagem2.format(numero, fatorial))
else:
    while cont > 1:
        fatorial = fatorial * (cont - 1)
        cont -= 1
    print(mensagem2.format(numero, fatorial))
