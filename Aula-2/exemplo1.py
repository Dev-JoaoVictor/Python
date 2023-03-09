import os

os.system('cls')

nome = input('Digite seu nome: ')
disciplina = input('Digite a disciplina: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = int((nota1 + nota2)) / 2

print('Nome:', nome)
print('Disciplina:', disciplina)
print(f'Nota1: {nota1:.2f}')
print(f'Nota2: {nota2:.2f}')
print(f'Média: {media:.2f}')
