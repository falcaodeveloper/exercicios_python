#Faça uma função que recebe por parâmetro o tempo de duração de uma fábrica expressa em segundos e retorna também por parâmetro esse tempo em horas, minutos e segundos: https://www.computersciencemaster.com.br/exercicios-funcoes/

mensagem = 'Digite o valor em segundos:\n'
segundos = int(input(mensagem))

def tempo(segundos):
    minutos = segundos / 60
    horas = minutos / 60
    return '{} segundos = {:.2f} hora(s) ou {:.2f} minutos' .format(segundos, horas, minutos)

print(tempo(segundos))