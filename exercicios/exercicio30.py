#Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-vespertino ou N-noturno. Imprima a mensagem “Bom dia!” ou  “Boa Noite” ou “Valor inválido”, conforme o caso: https://www.computersciencemaster.com.br/exercicios-if-e-else/
#Desenvolvido por Ulisses F. Falcão em 11/01/2024

mensagem = 'Em que turno você estuda?\nDigite "M" para matutino, "V" para vespertino ou "N" para noturno: '
matutino = 'Bom dia!'
vespertino = 'Boa tarde!'
noturno = 'Boa noite!'
invalido = 'Valor inválido'
entrada = input(mensagem).strip().upper()
def turnoDeEstudo(entrada):
    verdadeiro = entrada.isalpha()
    match verdadeiro:
        case True:
            if entrada == 'M':
                print(matutino)
            elif entrada == 'V':
                print(vespertino)
            elif entrada == 'N':
                print(noturno)
            else:
                print(invalido)
        case _:
            print(invalido)
turnoDeEstudo(entrada)