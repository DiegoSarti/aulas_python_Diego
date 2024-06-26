#Autor: Diego Sarti Araujo viana 
#Data: 13/06/2024
#Versão:1.0
#Descrição: Faça um programa que apresente a tabuada 1 ao 10
# ================================================================
print('Bom dia! Aqui esta a tabuada')

for numero in range(1,11):
    for multiiplicador in range(11):
        print(f'{numero} x {multiiplicador} = {numero * multiiplicador}')
