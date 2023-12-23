#Verificação de idade: Crie um programa que peça ao usuário para inserir a sua idade e verifique se ele é menor de idade, adulto ou idoso: https://horadecodar.com.br/exercicios-de-logica-de-programacao/
#Desenvolvido por Ulisses F Falcão em 28/11/2023

entrada = 'Por favor, digite sua idade: '
menor = 'Você é MENOR de idade.'
maior = 'Você é adulto, MAIOR de idade'
idoso = 'Você é idoso(a)'

idade = int(input(entrada))

if idade < 18:
    print(menor)
elif idade >= 18 and idade < 60:
    print(maior)
else:
    print(idoso)