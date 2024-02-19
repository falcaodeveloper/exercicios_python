msnNome = 'Digite seu nome completo:\n'
nome = input(msnNome).split()
indice = len(nome) - 1
print('{}, {}' .format(nome[indice], nome[0]))