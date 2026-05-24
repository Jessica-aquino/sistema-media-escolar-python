aluno = input('Digite seu nome: ')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media >= 7:
    print(f'Aluno(a): {aluno} | Média: {media:.1f} | Aprovado(a)')

elif media >= 5:
    print(f'Aluno(a): {aluno} | Média: {media:.1f} | Recuperação')

else:
    print(f'Aluno(a): {aluno} | Média: {media:.1f} | Reprovado(a)')
