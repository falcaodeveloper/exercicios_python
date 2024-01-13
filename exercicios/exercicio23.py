#Faça um programa que leia uma string do teclado e diga se ela é palíndromo. Uma string é palíndromo quando pode ser lida tanto de trás pra frente quanto de frente para trás e possui exatamente a mesma sequência de caracteres. Considere no desenvolvimento apenas palavras palíndromos: https://www.respondeai.com.br/conteudo/strings/exercicios/faca-programa-leia-string-teclado-diga-palindromo-string-palindromo-pode-10903

#https://www.dicio.com.br/lista-palindromos/
#Palavras com aspas ("") não funcionam: Aí, Lima falou: “Olá, família”.

string = input('Digite uma palavra ou frase:\n').strip().lower()
string = string.replace(' ', '')
string = string.replace('!', '')
string = string.replace('?', '')
string = string.replace(':', '')
string = string.replace(';', '')
string = string.replace('.', '')
string = string.replace(',', '')
string = string.replace('-', '')
string = string.replace('_', '')
string = string.replace('í', 'i')
string = string.replace('á', 'a')
string = string.replace('ã', 'a')
string = string.replace('à', 'a')
string = string.replace('ô', 'o')
string = string.replace('é', 'e')
string = string.replace('ê', 'e')

caracteres = len(string) - 1
invertida = ''
while caracteres >= 0:
    invertida = invertida + string[caracteres]
    caracteres -= 1

print(invertida)
print(string.endswith(invertida))