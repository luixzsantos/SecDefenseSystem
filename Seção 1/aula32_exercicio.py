"""
1 - Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero = input('Digite um número > ')

# try:
#     numero_int = int(numero)
#     par_impar = numero_int % 2 == 0

#     if par_impar:
#         print(f'{numero_int} é par')
#     else:
#         print(f'{numero_int} é impar')           
# except:
#     print(f'{numero} número não é um inteiro')

"""
2 - Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# usuario = input('Digite seu nome > ') 
# hora = input(f'{usuario} digite o horário do dia (h) > ')

# hora_do_dia = int(hora)

# if hora_do_dia <= 11:
#     print('Bom dia')
# elif hora_do_dia <= 17:
#     print('Boa Tarde')
# elif hora_do_dia <= 23:
#     print('Boa Noite')

"""
3 - Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# user = input('Digite o seu nome > ')
# tamanho_user = len(user)

# if tamanho_user <= 4:
#     print('Seu nome é Curto!')
# elif tamanho_user <= 6:
#     print('Seu nome é Normal!')
# elif tamanho_user > 6:
#     print('Seu nome é "Grande"')