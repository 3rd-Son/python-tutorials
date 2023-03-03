x = input('Enter number 1: ')
y = input('Enteer number 2: ')

try:
    z = int(x)  / int (y)
except ZeroDivisionError() as e:
    print('Division by zero exception')
    z = None
except TypeError() as e:
    print('type error exception')
    z = None
print(f'Division is : {z}') 