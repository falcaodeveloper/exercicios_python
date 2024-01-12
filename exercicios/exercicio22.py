#Desenvolva um programa capaz de verificar se duas strings são iguais: https://www.respondeai.com.br/conteudo/strings/exercicios/desenvolva-programa-capaz-verificar-duas-strings-sao-iguais-nao-utilize-10900
#Desenvolvido por Ulisses F. Falcão em 29/12/2023

string1 = input('Digite uma palavra ou frase.\n').strip()
string2 = input('Digite outra palavra ou frase.\n').strip()
print(string1.endswith(string2))