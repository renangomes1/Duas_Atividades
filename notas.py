materias = ['Português', 'Inglês', 'Matemática']
nome = input('Digite o nome do aluno: ')
print(materias)

total_nota_mat = []
total_nota_por = []
total_nota_ing = []

n1, n2,n3 = float(input('Por =')), float(input('Por=')), float(input('Por='))
n4, n5, n6  = float(input('Mat=')), float(input('Mat=')), float(input('Mat='))
n7, n8, n9  = float(input('Ing=')), float(input('Ing=')), float(input('Ing='))

total_nota_por += (n1,n2,n3)
total_nota_mat += (n4,n5,n6)
total_nota_ing += (n7,n8,n9)


MEDIA1 = sum(total_nota_por)/len(total_nota_por)
MEDIA2 = sum(total_nota_mat)/len(total_nota_mat)
MEDIA3 = sum(total_nota_ing)/len(total_nota_ing)

print(f'''

Média Português: {MEDIA1}
Situação: {MEDIA1 >= 7}
Notas: {total_nota_por}
Maior nota: {max(total_nota_por)}
Menor nota: {min(total_nota_por)}



Média Matemática: {MEDIA2}
Situação: {(MEDIA3 >= 7)}
Notas: {total_nota_mat}
Maior nota:  {max(total_nota_mat)}
Menor nota: {min(total_nota_mat)}



Média Inglês: {MEDIA3}
Situação: {(MEDIA3 >= 7)}
Notas:  {total_nota_ing}
Maior nota: {max(total_nota_ing)} 
Menor nota:{min(total_nota_ing)}

''')