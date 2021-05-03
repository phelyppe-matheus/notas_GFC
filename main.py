import re

def q_academico(data):
    code, *grade = map(int, data.split())

    final_grade = (grade[0]*3 + grade[1]*3 + grade[2]*3 + max(grade))/(10)

    print(f'''
    Aluno {code}
        nota 1 {grade[0]}
        nota 2 {grade[1]}
        nota 3 {grade[2]}
    Resultado: {final_grade} >>''', end='')

    if final_grade < 5:
        print('REPROVADO')
    else:
        print('APROVADO')
