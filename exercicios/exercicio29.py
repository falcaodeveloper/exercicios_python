#Faça um programa que leia três números e mostre-os em ordem decrescente: https://www.computersciencemaster.com.br/exercicios-if-e-else/
#Desenvolvido por Ulisses F. Falcão em 11/01/2024

mensagem1 = 'Você deverá digitar 3 números. Aperte ENTER após digitar um número.'
mensagem2 = 'Digite o número: '
numero = []
cont = 0
print(mensagem1)
while cont <= 2:
    numero.append(int(input(mensagem2)))
    cont += 1

#Verificando quem é o maior
if numero[0] > numero[1] and numero[0] > numero[2]:
    maior = numero[0]
elif numero[1] > numero[0] and numero[1] > numero[2]:
    maior = numero[1]
elif numero[2] > numero[0] and numero[2] > numero[1]:
    maior = numero[2]

#Verificando quem é o menor
if numero[0] < numero[1] and numero[0] < numero[2]:
    menor = numero[0]
elif numero[1] < numero[0] and numero[1] < numero[2]:
    menor = numero[1]
elif numero[2] < numero[0] and numero[2] < numero[1]:
    menor = numero[2]

#Verificando o número do meio
if numero[0] > numero[1] and numero[0] < numero[2]:
    meio = numero[0]
elif numero[0] < numero[1] and numero[0] > numero[2]:
    meio = numero[0]
elif numero[1] > numero[0] and numero[1] < numero[2]:
    meio = numero[1]
elif numero[1] < numero[0] and numero[1] > numero[2]:
    meio = numero[1]
elif numero[2] > numero[0] and numero[2] < numero[1]:
    meio = numero[2]
elif numero [2] < numero[0] and numero[2] > numero[1]:
    meio = numero[2]

print(maior)
print(meio)
print(menor)