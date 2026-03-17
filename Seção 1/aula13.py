# Introdrução a f-strings

nome = 'Luiz Otavio'
altura = 1.80
peso = 95
imc = peso / altura ** 2

# Uso das f-strings
linha1 = f'{nome} tem {altura:.2f} de altura'
linha2 = f'pesa {peso} e seu imc é {imc:.2f}'
print(linha1)
print(linha2)