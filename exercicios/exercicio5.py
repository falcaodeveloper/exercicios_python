#Verificação de notas: Crie um programa que peça ao usuário para inserir sua nota em uma prova e imprima se ele foi aprovado ou reprovado (considerando que a nota mínima para aprovação é 7): https://horadecodar.com.br/exercicios-de-logica-de-programacao/
#Desenvolvido por Ulisses F Falcão em 29/11/2023

mensagem = 'Digite sua nota: '
aprovado = 'Parabéns! Você está "aprovado".'
reprovado = 'Infelizmente, você está "reprovado".'
nota = float(input(mensagem))

print(aprovado) if nota >= 7 else print(reprovado)