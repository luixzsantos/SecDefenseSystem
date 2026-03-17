"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40, 50]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])

lista.append(60)
lista.pop()
lista.append(70)
lista.append(80)
lista.pop(3)
print(lista)
