'''As organizações CSM resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.  

a. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual;
b. Salários até R$ 280,00 (incluindo): aumento de 20%;
c. Salários entre R$ 280,00 e R$700,00: aumento de 15%;
d. Salários entre R$ 700,00 e R$ 1500,00: aumento de 10%;
e. Salários de R$ 1500,00 em diante: aumento de 5%
Após o aumento ser realizado; informe na tela;

a. O salário antes do reajuste;
b. O percentual de aumento aplicado;
c. O valor do aumento;
d. O novo salário, após o aumento:
https://www.computersciencemaster.com.br/exercicios-if-e-else/'''
#Desenvolvido por Ulisses F. Falcão em 12/01/2024

mensagem = 'Por favor, digite seu salário: '
novoSalario = float
antesDoReajuste = 'Salário antes do reajuste: R$ {:.2f}'
valorDoAumento = 'Valor do aumento: R$ {:.2f}'
percentualDeAumento = 'Percentual de aumento aplicado: {}'
novoSalario = 'Novo salário: R$ {:.2f}'
salario = (input(mensagem)).replace(',', '.')
salario = float(salario)

def reajusteSalarial(salario):
    if salario <= 280:
        print(antesDoReajuste .format(salario))
        print(percentualDeAumento .format('20%'))
        print(valorDoAumento .format(20 / 100 * salario))
        print(novoSalario .format((20 / 100 * salario) + salario))
    elif salario > 280 and salario <= 700:
        print(antesDoReajuste .format(salario))
        print(percentualDeAumento .format('15%'))
        print(valorDoAumento .format(15 / 100 * salario))
        print(novoSalario .format((15 / 100 * salario) + salario))
    elif salario > 700 and salario <= 1500:
        print(antesDoReajuste .format(salario))
        print(percentualDeAumento .format('10%'))
        print(valorDoAumento .format(10 /100 * salario))
        print(novoSalario .format(10 / 100 * salario + salario))
    else:
        print(antesDoReajuste .format(salario))
        print(percentualDeAumento .format('5%'))
        print(valorDoAumento .format(5 / 100 * salario))
        print(novoSalario .format(5 / 100 * salario + salario))
reajusteSalarial(salario)    