# Conversor de Unidades: Graus Celsius, Fahrenheit e Kelvin


def menu_inicial():
    print('**********BEM-VINDO AO CONVERSOR DE TEMPERATURA DA BITWAY**********')
    print('1. Converter de Celsius para Fahrenheit')
    print('2. Converter de Fahrenheit para Celsius')
    print('3. Converter de Celsius para Kelvin')
    print('4. Converter de Kelvin para Celsius')
    print('5. Converter de Fahrenheit para Kelvin')
    print('6. Converter de Kelvin para Fahrenheit') 

    print(' ')

def cel_fahr():
 while True:
  try:
    C = float(input('\nEntre com a temperatura em graus Celsius: '))
    F = C * (9 / 5) + 32
    if C < -273.15:
        print('Valor não permitido! Tente entrar com valores acima de -273.15')
    else:
        print('Valor em Fahrenheit: {0}°F'.format(F))
        break
  except ValueError:
      print('Valor não permitido! Só aceitamos números')

def fahr_cel():
 while True:
  try:
    F = float(input('\nEntre com a temperatura em graus Fahrenheit: '))
    C = (F - 32) * (5 / 9)
    if F < -459.67:
        print('Valor não permitido! Tente entrar com valores acima de -459.67')
    else:
        print('Valor em Celsius: {0}°C'.format(C))
        break
  except ValueError:
      print('Valor não permitido! Só aceitamos números')

def cel_kel():
 while True:
  try:
    C = float(input('\nEntre com a temperatura em graus Celsius: '))
    K = C + 273.15
    if C < -273.15:
        print('Valor não permitido!  Tente entrar com valores acima de -273.15')
    else:
        print('Valor em Kelvin: {0}°K'.format(K))
        break
  except ValueError:
      print('Valor não permitido! Só aceitamos números')

def kel_cel():
 while True:
  try:
    K = float(input('\nEntre com a temperatura em graus Kelvin: '))
    C = K - 273.15
    if K < 0:
        print('Valor não permitido!  Tente entrar com valores acima de 0')
    else:
        print('Valor em Celsius: {0}°C'.format(C))
        break
  except ValueError:
      print('Valor não permitido! Só aceitamos números')

def fahr_kel():
 while True:
  try:
    F = float(input('\nEntre com a temperatura em graus Fahrenheit: '))
    K = (F - 32) / (9 / 5) + 273.15
    if F < -459.67:
        print('Valor não permitido!  Tente entrar com valores acima de -459.67')
    else:
        print('Valor em Kelvin: {0}°K'.format(K))
        break
  except ValueError:
      print('Valor não permitido! Só aceitamos números')

def kel_fahr():
 while True:
  try:
    K = float(input('\nEntre com a temperatura em graus Kelvin: '))
    F = (K - 273.15) * (9 / 5) + 32
    if K < 0:
        print('Valor não permitido!  Tente entrar com valores acima de 0')
    else:
        print('Valor em Fahrenheit: {0}°F'.format(F))
        break
  except ValueError:
      print('Valor não permitido! Só aceitamos números')


if __name__=='__main__':
    menu_inicial()
    escolha = input('Escolha o tipo de conversão que deseja realizar: ')

    if escolha == '1':
        cel_fahr()

    if escolha == '2':
        fahr_cel()
    
    if escolha == '3':
        cel_kel()

    if escolha == '4':
        kel_cel()

    if escolha == '5':
        fahr_kel()

    if escolha == '6':
        kel_fahr()

