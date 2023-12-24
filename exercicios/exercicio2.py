#Comparações de números: Crie um programa que peça ao usuário para inserir dois números e diga qual deles é maior, ou se são iguais: https://horadecodar.com.br/exercicios-de-logica-de-programacao/
#Desenvolvido por Ulisses F Falcão em 28/11/2023

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

if numero1 > numero2:
    print('Número {} é maior que o número {}' .format(numero1, numero2))
elif numero1 < numero2:
    print('Número {} é maior que o número {}' .format(numero2, numero1))
else:
    print('Os números são iguais')