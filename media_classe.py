# algoritimo "media turma"
# Descrição : Faça um programa que receba duas notas de seis alunos
            #  calcule e mostre:
            # A media aritimetica das notas de cada aluno; e
            #  A mensagem que esta na tabela a seguir:
                # media Aritmetica  Mensagem
                # até 3             Reprovado
                # entre 4 e 7       exame
                # De 8 pra cima     aprovado

            #O total de alunos aprovados;
            #O total de alunos de exame;
            #O total de alunos reprovados;
            #A média de classe.
# =====================================================================================
# alunox
aluno = 0
qtdAlunos = 0

while aluno < qtdAlunos:
    aluno = aluno + 1

nota_um = 0
nota_dois = 0
media = 0
alunosReprovados = 0
alunosExame = 0
alunosAprovados = 0

nota_um = float(input(f'insira a nota 1 do aluno {aluno}: '))
nota_dois = float(input(f'insira a nota 2 do aluno {aluno}: '))

media = (nota_um + nota_dois)/2

if(media <= 3):
    print('reprovado')
    alunosReprovados += 1
elif( media >= 4 and media <= 7):
    print('Exame')
    alunosExame += 1
else:
    print('Aprovado')
    alunosAprovados += 1

print(f'Quantidade de alunos aprovados: {alunosAprovados}')
print(f'Quantidade de alunos reprovados: {alunosReprovados}')
print(f"Quantidade de alunos exame: {alunosExame}")






