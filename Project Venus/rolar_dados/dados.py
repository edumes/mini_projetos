from random import randint

qual_dado = str(input('''Escolha qual dado quer rolar: 

        D6, D10 e D100: ''')).upper()

if qual_dado == 'D6':
    print('você escolheu o dado D6')
    print('O numero do dado é:', randint(1,6))

if qual_dado == 'D10':
    print('você escolheu o dado D10')
    print('O numero do dado é:', randint(1,10))

if qual_dado == 'D100':
    print('você escolheu o dado D100')
    print('O numero do dado é:', randint(1,100))