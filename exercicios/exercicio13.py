#2. Elabore  um  algoritmo  para  testar  se  uma  senha  digita  é  igual  a  “Patinho Feio”.  Se  a  senha  estiver  correta escreva “Acesso permitido”, do contrario emita a mensagem “Você não tem acesso ao sistema”: https://www.studocu.com/pt-br/document/universidade-do-extremo-sul-catarinense/introducao-a-programacao/lista-de-exercicios-4-estrutura-condicional/4696405
#Desenvolvido por Ulisses F. Falcão em 05/12/2023

mensagem = 'Digite a senha\n'
senha = input(mensagem)

match senha:
    case 'Patinho Feio':
        print('Acesso permitido')
    case _:
        print('Você não tem acesso ao sistema')