velocidade = int(input('Qual velocidade o carro estava:'))

if velocidade < 10:
    print('sua multa é de R$ 50,00')
elif velocidade > 11 and velocidade < 30:
    print('sua multa é de R$ 100,00')
elif velocidade > 31:
    print('sua multa é de R$ 200,00')
