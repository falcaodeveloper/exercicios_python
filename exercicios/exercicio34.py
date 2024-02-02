'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.'''
#https://wiki.python.org.br/EstruturaSequencial
#Desenvolvido por Ulisses F. Falcão em 31/01/2024

multa, peso, excesso = 4, 50, 0
msnPeso = 'Digite o total em quilos de peixes: '
msnInvalido = 'Você digitou um valor inválido.'
msnSemExcesso = 'Não à multa a pagar!'
msnExcesso = 'Quilos excedidos: {:.2f}Kg'
msnMulta = 'Multa a pagar: R${:.2f}'

while True:
    try:
        peso = (input(msnPeso)).strip()
        peso = peso.replace(',', '.')
        peso = float(peso)
    except:
        print(msnInvalido)
    else:
        break

if peso <= 50:
    print(msnSemExcesso)
else:
    excesso = peso - 50
    multa *= excesso
    print(msnExcesso.format(excesso))
    print(msnMulta.format(multa))