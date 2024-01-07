#Faça um procedimento que recebe por parâmetro os valores necessário para o cálculo da fórmula de báskara e retorna, também por parâmetro, as suas raízes, caso seja possível calcular: https://www.computersciencemaster.com.br/exercicios-funcoes/#google_vignette
#Explicação: https://www.todamateria.com.br/formula-de-bhaskara/
#Desenvolvido por Ulisses F Falcão em 08/12/2023

mensagemA = 'Digite o valor de "a":\n'
mensagemB = 'Digite o valor de b:\n'
mensagemC = 'Digite o valor de c:\n'

a = float(input(mensagemA))
b = float(input(mensagemB))
c = float(input(mensagemC))

#Se o valor de Δ for maior que zero (Δ > 0), a equação terá duas raízes reais e distintas.
#Se o valor de Δ for igual a zero (Δ = 0), a equação apresentará uma raiz real. (Raízes iguais)
#Se o valor de Δ for menor que zero (Δ<0), a equação não possui raízes reais.

def baskara(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta > 0 or delta == 0:
        #return (-b + delta ** (1/2)) / (2 * a)
        #return (-b - delta ** (1/2)) / (2 * a)
        return 'Delta = {}\nx1 = {}\nx2 = {}' .format(delta, (-b + delta ** (1/2)) / (2 * a), (-b - delta ** (1/2)) / (2 * a))
    else:
        return 'Delta = {}. Não há raízes reais.' .format(delta)

print(baskara(a, b, c))