# Faça um programa que verifique (usando if e else) se uma letra digitada é vogal ou consoante: https://www.computersciencemaster.com.br/exercicios-if-e-else/
#Desenvolvido por Ulisses F. Falcão em 10/01/2024

letra = input('Digite uma letra: ').strip().lower()
seLetra = letra.isalpha()
match seLetra:
    case True:
        if len(letra) == 1:
            if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
                print('{} é vogal'.format(letra))
            else:
                print('{} é consoante'.format(letra))
        else:
            print('Você tem que digitar APENAS uma letra')
    case _:
        print('Você tem que digitar APENAS uma letra')