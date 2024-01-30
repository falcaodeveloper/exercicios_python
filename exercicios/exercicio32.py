#Soma dos números em uma lista: Crie um programa que some todos os números em uma lista.
#https://horadecodar.com.br/exercicios-de-logica-de-programacao/
#Desenvolvido por Ulisses F. Falcão em 23/01/2024

mensagem = '''Digite quantos números quiser para somar.
Tecle ENTER para cada número.
Para sair do programa, não digite nada e tecle ENTER.'''
numero = []
msnRecebe = 'Digite o número: '
saiu = 'Você saiu do programa, com sucesso!'
cont = soma = 0
print(mensagem)
while True:
    numero.append(input(msnRecebe))
    if numero[cont] == '':
        numero.remove('')
        print(saiu)
        cont -= 1
        break
    else:
        converte = str(numero[cont])
        converte = converte.replace(',', '.')
        converte = float(converte)
        soma += converte
    cont += 1

print(soma)