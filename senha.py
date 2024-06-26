# Data:07/06/2024
# versao: 1.0
# algoritimos: senha
# Descrição: Faça um progama que solicite para o usuario a senha de acesso ao sistema,
#            ele terá no maximo tres tentativas para inserir a correta
#            cadastrada (senai115),caso passe desse limite uma mensagm de erro deve aparecer
# tentativas = ""

# while tentativas > 0:
#         senha = input("Digite a senha: ")
#         if senha == 'senai115':
#             print("Senha correta. Acesso concedido!")
#             break;
#         else:
#             tentativas -= 1
#             print(f"Senha incorreta. Você tem tentativas tentativas restantes.")
# else:
#         print("Você excedeu o número máximo de tentativas. Acesso bloqueado.")


senha = ''
senhaPadrao = 'senai115'
tentativas = 3
while True:
    senha = input('Digite a sua senha: ')
    if senha == senhaPadrao:
        print('Acesso Liberado')
        break
    else:
        tentativas = tentativas - 1
        print('Voce só possui', tentativas, 'tentativas')

    if(tentativas <= 0):
        print('voce nao posui mais tentativas')
        break




