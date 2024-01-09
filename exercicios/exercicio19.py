#Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade expressa em dias: https://www.computersciencemaster.com.br/exercicios-funcoes/

mensagemAnos = 'Digite quantos anos você tem: '
mensagemMeses = 'Digite quantos meses você tem: '
mensagemDias = 'Digite quantos dias você tem: '

anos = int(input(mensagemAnos))
meses = int(input(mensagemMeses))
dias = int(input(mensagemDias))

def diasDeVida(anos, meses, dias):
    anos *=  365  #calculo com 365 dias
    meses *= 30 #meses de 30 dias
    return anos + meses + dias

print('{} dias' .format(diasDeVida(anos, meses, dias)))
