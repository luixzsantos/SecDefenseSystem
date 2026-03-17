""" Calculadora usando While """

print('=== Calculadora Python Simpels - Básica ===')

while True:
    num1 = input('Digite o número 1: ')
    num2 = input('Digite o número 2: ')
    operador = input('Digite um operador Válido (+-*/): ')

    try:
        num1 = float(num1)
        num2 = float(num2)
    except:
        print('Um dos seu números é inválido, digite-os novamente !')
        continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('Você digitou um operdor inválido!')
        continue

    if len(operador) > 1:
        print('Você so pode digitar somente 1 operador!')
        continue

    if operador == '/' and num2 == 0:
        print('Error, divisão por 0!')
        continue
    
    if operador == '+':
        print(f'{num1} + {num2} = ', num1 + num2)

    elif operador == '-':
        print(f'{num1} - {num2} = ', num1 - num2)

    elif operador == '*':
        print(f'{num1} * {num2} = ', num1 * num2)

    elif operador == '/':
        print(f'{num1} / {num2} = ', num1 / num2)

    sair = input('Deseja Sair [s/n]: ').lower().strip()
    
    if sair == 's':
        print('Obrigado por usar minha calculadora!!')
        break
    elif sair == 'n':
        print('okay, vamos para mais alguns cálculos')
        continue
    else:
        print('Digite alguma opção válida ')