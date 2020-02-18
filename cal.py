import math
number = float(input('type a number: '))
number1 = float(input('type a number: '))
print('''\
o que voce deseja fazer com estes valores?
[ 1 ] adição 
[ 2 ] subtração 
[ 3 ] multiplicação
[ 4 ] divisão 
[ 5 ] poteciação 
''')
escolha = int(input('type the opction: '))
print('')

if escolha == 1:
    adicionar = number + number1
    print(adicionar)
elif escolha == 2:
    subtrair = number - number1
    print(subtrair)
elif escolha == 3:
    multiplique = number * number1 
    print(multiplique)
elif escolha == 4:
    dividir = number / number1
    print(dividir)
elif escolha == 5:
    potencia = number ** number1 
    print(potencia)
# elif escolha == 6: 
#      radici = math.sqrt(number)
#      print(radici)	
else: 
    print('this command no corresponds as the options above')