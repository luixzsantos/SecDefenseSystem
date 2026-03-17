"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista
"""

print('--- Lista de Compras em Python ---\n')

lista = []

while True:
    digit = input('Digite uma opção: [I]nserir, [A]pagar, [L]istar: ').upper().strip()

    if digit == 'I':
        inserir = input('Digite um item para inserir na lista : ')
        lista.append(inserir)
        print(f'{inserir} adicionado com sucesso na lista!\n')    

    elif digit == 'L':
        for indice, item in enumerate(lista):
            print(indice, item)    

    elif digit == 'A':
        apagar = input('Digite o índice para remover da lista: ')

        if not apagar.isdigit():
            print('Digite um número!\n')
            continue

        indice = int(apagar)

        if indice < 0 or indice >= len(lista):
            print('índice Inválido!\n')
            continue

        removido = lista[indice]
        lista.pop(indice)
        
        print(f'Índice {indice} ({removido}) removido !\n')
    
    else:
        print('Opção inválida!\n')
  
        
