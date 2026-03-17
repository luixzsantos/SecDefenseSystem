"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = input('Digite seu CPF: ').strip()
cpf = ''.join(ch for ch in cpf if ch.isdigit())  # remove . e -

if len(cpf) != 11 or cpf == cpf[0] * 11:
    print('CPF inválido')
else:
    nove_digitos = cpf[:9]

    # 1º dígito
    contador = 10
    resultado = 0
    for digito in nove_digitos:
        resultado += int(digito) * contador
        contador -= 1

    first_digit = (resultado * 10) % 11
    first_digit = first_digit if first_digit <= 9 else 0

    # 2º dígito
    dez_digitos = nove_digitos + str(first_digit)
    contador2 = 11
    resultado2 = 0
    for digito in dez_digitos:
        resultado2 += int(digito) * contador2  # <- aqui era o bug
        contador2 -= 1

    second_digit = (resultado2 * 10) % 11
    second_digit = second_digit if second_digit <= 9 else 0

    cpf_gerado = nove_digitos + str(first_digit) + str(second_digit)

    if cpf_gerado == cpf:
        print('CPF válido')
    else:
        print('CPF inválido')
