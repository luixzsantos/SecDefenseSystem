# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# entrada = input('[E]ntrar [S]air: ')
# senha = input('Senha: ')

# senha_correta = '1234'

# if (entrada == 'E' or entrada == 'e') and senha == senha_correta:
#     print('Entrou no Sistema !')
# else:
#     print('Saiu do Sistema !')

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem Senha'
print(senha)



    