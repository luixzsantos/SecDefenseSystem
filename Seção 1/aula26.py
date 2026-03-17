"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

letra = 'ABC'
num = 123621783.12388312

print(f'{letra}')
print(f'{letra: >10}.')
print(f'{letra: <10}')
print(f'{letra: ^10}.')
print(f'{num:+.2f}')
print(f'{450:08X}')
print(f'{letra!r}')

