# ==================================================================================================
# Autor:Diego Sarti Araujo Viana
# Data: 24/05/2024
# versao: 1.0
# Descrição: faça um algoritimo que receba as notas e imprima 
#           a media final do aluno
# =====================================================================================================
        # exemplo de execuão
        # Nota 1: 10
        # Nota 2: 10
        # Nota 3: 10
        # Nota 4: 10
        # Nota 5: 10
        # Media final: 10
# ====================================================================================================

#casting => para converter o valor de string para inteiro
# 5 = int('s')
Nota1 = float(input("Nota 1: "))
Nota2 = float(input("Nota 2: "))
Nota3 = float(input("Nota 3: "))
Nota4 = float(input("Nota 4: "))
Nota5 = float(input("Nota 5: "))
Mediafinal = Nota1 + Nota2 + Nota3 + Nota4 + Nota5 
resultado = Mediafinal / 5
print('Sua Media final é: ',resultado)
# ======================================================================================================
