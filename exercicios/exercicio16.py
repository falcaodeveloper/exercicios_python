#Faça uma função que recebe por parâmetro um valor inteiro e positivo e retorna o valor lógico Verdadeiro caso o valor seja primo e Falso em caso contrário: https://www.computersciencemaster.com.br/exercicios-funcoes/#google_vignette
#Desenvolvido por Ulisses F. Falcão em 08/12/2023

mensagem = 'Digite um número inteiro e positivo para saber se é primo:\n'
valor = int(input(mensagem))

divisor = 3

def primo(valor, divisor):
    match valor:
        case 0:
            return 'Falso'
        case 1:
            return 'Falso'
        case 2:
            return 'Verdadeiro'
        case 3:
            return 'Verdadeiro'
    if valor > 3:
        resto = valor % 2
        if resto == 0: return 'Falso'
    if valor > 3:
        resto = valor % 2
        if resto != 0:
            while resto != 0:
                quociente = valor / divisor
                resto = valor % divisor
                divisor += 1
            if resto == 0 and quociente == 1:
                return 'Verdadeiro'
            else:
                return 'Falso'
print(primo(valor, divisor))