"""
Lista dentro de Listas
"""

salas = [
    #   0         1
    ['Maria', 'Helena',], # 0
    #   0         1
    ['Matheus',], # 1
    #   0       1         2
    ['Luiz', 'João', 'Alberto',] # 2
]

# print(salas[2][3][3])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)


