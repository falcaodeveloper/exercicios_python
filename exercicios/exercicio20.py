#Implemente um programa que receba um nome completo e apresente apenas o último nome e o primeiro nome na seguinte forma: “1º nome, último nome”. Considere que todas as entradas de nomes completos serão compostas apenas de 3 nomes, por exemplo: José Almeida Barros: https://www.respondeai.com.br/conteudo/strings/exercicios/implemente-programa-receba-nome-completo-apresente-apenas-ultimo-nome-primeiro-10898
#Desenvolvido por Ulisses F. Falcão em 29/12/2023

mensagem = 'Digite seu nome completo:'
nome = input('{}\n' .format(mensagem)).strip().title().split()

print('{} {}' .format(nome[0], nome[2]))
print('1º nome: {}' .format(nome[0]))
print('Último nome: {}' .format(nome[2]))