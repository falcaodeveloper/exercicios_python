#Faça um programa que verifique (usando if e else) se uma letra digitada é vogal ou consoante:
#Desenvolvido por Ulisses F. Falcão em 10/01/2024

mensagem1 = 'Digite apenas uma letra para saber se é "vogal" ou "consoante":\n'
mensagem2 = 'Digite "APENAS UMA" letra.'
vogal = 'é vogal'
consoante = 'é consoante'
letra = str(input(mensagem1)).strip().upper()
seLetra = letra.isalpha()
match seLetra:
    case True:
        if len(letra) == 1:
            if letra == 'A' or letra == "E" or letra == "I" or letra == "O" or letra == "U":
                print('{} {}'.format(letra, vogal))
            else:
                print('{} {}'.format(letra, consoante))
        else:
            print(mensagem2)
    case _:
        print(mensagem2)