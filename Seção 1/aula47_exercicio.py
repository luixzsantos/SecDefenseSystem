"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = 'amor'
letra_acertada = ''
tentativa = 0

while True:

    letra_digitada = input('Digite uma letra: ').lower().strip()

    if len(letra_digitada) != 1:
        print(f'Você digitou mais de uma letra!')
        continue   

    tentativa += 1

    if letra_digitada in palavra_secreta:
        letra_acertada += letra_digitada

    palavra_formada = ''

    for letra in palavra_secreta:
        if letra in letra_acertada:
            palavra_formada += letra
        else:
            palavra_formada += '*'

    if letra_digitada in palavra_secreta:
        print(f'Letra: {letra_digitada} (Tentativa: {tentativa})\n')
    else:
        print(f'Letra: {letra_digitada} (Tentativa: {tentativa})\n')

    print(f'Palavra sendo formada: {palavra_formada}\n')

    if palavra_formada == palavra_secreta:
        print(f'Parabêns, a palavra secreta é {palavra_formada}.\n' \
               'Você é muito bom nesse tipo de jogo')
        break
 