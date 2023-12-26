#Verificação de temperatura: Crie um programa que peça ao usuário para inserir uma temperatura e verifique se está frio, agradável ou quente: https://horadecodar.com.br/exercicios-de-logica-de-programacao/
#Desenvolvido por Ulisses F Falcão em 28/11/2023

recebeTemp = 'Por favor, digite a temperatura: '

frio = 'Está FRIO'
agradavel = 'Está AGRADÁVEL'
quente = 'Está QUENTE'

temperatura = float(input(recebeTemp))

if temperatura < 16:
    print(frio)
elif temperatura > 15 and temperatura < 31:
    print(agradavel)
else:
    print(quente)