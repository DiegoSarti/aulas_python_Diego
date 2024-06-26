
#=========================================================================
#Autor: Diego Sarti
#Data: 23/05/2024
#Versão:1.0
#Descrição: Algoritimo que recebe o nome do usuario
#           e exibe uma frase de saudação concatenada com
#           a entrada do usuario.
#=========================================================================
#observações:
#           a)para iniciar um comentario utuliza-se '#'
#           b) no visual studio utilizar o comando ctrl+;
#               para comentar o bloco
#=========================================================================
#inicio 
dadovazio = ''#var atribuida com valor vazio
# entrada
nome = input("Qual é o seu nome?")
# processamento
mensagem = 'olá, seja bem-vindo! '
frase = mensagem + nome
# saida
print(frase)
# fim 