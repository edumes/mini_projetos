#cores no terminal
class cores:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua Altura: '))

imc = peso/(altura**2)

if imc < 17.0:
    print(cores.WARNING+'Seu IMC é {:.2f}! Vc está muito abaixo do peso!'.format(imc))
elif imc >= 17.0 and imc <= 18.5:
    print(cores.WARNING+'Seu IMC é {:.2f}! Vc está muito abaixo do peso normal!'.format(imc))
elif imc >= 18.5 and imc <= 25.0:
    print(cores.OKGREEN+'Seu IMC é {:.2f}! Vc está dentro do peso normal!'.format(imc))
elif imc >= 25.0 and imc <= 30.0:
    print(cores.WARNING+'Seu IMC é {:.2f}! Vc está acima do peso!'.format(imc))
else:
    print(cores.WARNING+'Seu IMC é {:.2f}! Vc está acima do peso!'.format(imc))

