"""
Iterando strings com while
"""

#       0123456
nome = 'Matheus' # Iteráveis
#       7654321

# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])

# Exercício -> Iterar coisas no nome tipo #M#a#t#h#e#u#s#

indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)