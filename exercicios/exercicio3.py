#Verificação de divisibilidade: Crie um programa que peça ao usuário para inserir dois números e verifique se o primeiro número é divisível pelo segundo: https://horadecodar.com.br/exercicios-de-logica-de-programacao/
#Desenvolvido por Ulisses F Falcão em 28/11/2023

mensagem1 = 'Por favor, digite um número: '
mensagem2 = 'Digite outro número: '

n1 = int(input(mensagem1))
n2 = int(input(mensagem2))
n3 = n1 % n2

print('O número {} é divisível por {}.' .format(n1, n2)) if n3 == 0 else print('O número {} não é divisível por {}' .format(n1, n2))