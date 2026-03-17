"""
Enumerate - enumera uma lista
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'Matheus')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('Matheus')

for indice, nome in enumerate(lista):
    print(indice, nome)

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

# for item in enumerate(lista):
#     for valor in item:
#         print(valor)
