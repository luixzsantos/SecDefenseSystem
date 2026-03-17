# Desempacotamento em chamadas
# de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    #   0         1
    ['Maria', 'Helena',], # 0
    #   0         1
    ['Matheus',], # 1
    #   0       1         2
    ['Luiz', 'João', 'Alberto',] # 2
]

# a, b, *_, p, u = lista
# print(p, u)

# print(*lista) # print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*string) # print('A B C D')
# print(*tupla) # print('Python', 'é', 'legal')

print(*salas, sep='\n')