#Escreva um procedimento que recebe as 3 notas de um aluno por parâmetro e uma letra. Se a letra for A o procedimento calcula a média aritmética das notas do aluno, se for P, a sua média ponderada (pesos: 5, 3 e 2) e se for H, a sua média harmônica. A média calculada também deve retornar por parâmetro: https://www.computersciencemaster.com.br/exercicios-funcoes/#google_vignette
#Desenvolvido por Ulisses F. Falcão em 07/12/2023

#Explicação: Média Ponderada - https://www.todamateria.com.br/media-ponderada/ e média harmônica - https://statorials.org/pt/media-harmonica/

mensagem1 = 'Digite sua 1ª nota: '
mensagem2 = 'Digite sua 2ª nota: '
mensagem3 = 'Digite sua 3ª nota: '
mensagem4 = 'Digite a letra correspondente: '

nota1 = float(input(mensagem1))
nota2 = float(input(mensagem2))
nota3 = float(input(mensagem3))
letra = input(mensagem4)

def calculo(nota1, nota2, nota3, letra):
    match letra:
        case 'a':
            return((nota1 + nota2 + nota3) / 3)
        case 'p':
            return((nota1 * 5 + nota2 * 3 + nota3 * 2) / (5 + 3 + 2))
        case 'h':
            return(3 / (1 / nota1 + 1 / nota2 + 1 / nota3))
        case _:
            return('Você digitou uma "letra inválida"')

print(calculo(nota1, nota2, nota3, letra))