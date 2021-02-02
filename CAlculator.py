
# Author Ilya Bilyi
import math
RESPONCE="\t Що виконати?\n*******************************\n 1 додавання \n 2 Віднімання \n 3 Ділення \n 4 множення \n 5 до степеня\n 6 сінус \n 7 косинус \n 8 аргсінус \n 9 аргкосинус \n*******************************\n   "


print ('$$$ Вітаю це я калькулятор! $$$')
# loop while  precheck input data
flag = True
while(flag == True):
    print(RESPONCE)
    variant = input('Ваш варіант: ')
    # TODO: handle input is not float 
    
    if(variant.isdigit() == True):
        variant = int(variant)
    else:
        print("\nВведено літеру: {}! Ведіть цифру \n".format(variant))
        continue          
    
    if variant in range(1,11):
        flag = False
    else:
        print("\nНекоректно введене значення: {} \n".format(variant))
        continue
flag2 = True       
while(flag2 == True):
    first_number = input('Введіть число 1: ')
    if(first_number.isdigit() == True):
        first_number = int(first_number)
        flag2 = False
    else:
        print("\nВведено літеру: {}! Ведіть цифру \n".format(first_number))
        continue
 
 
 
if variant in range(1,7):              
    flag3 = True
    while(flag3 == True):
       second_number = input('Введіть число 2: ')
       if(second_number.isdigit() == True) :
            second_number = int(second_number)
            flag3 = False 
       else:
           print("\nВведено літеру: {}! Ведіть цифру \n".format(second_number))
           continue     
    

if variant == 1:
    r = first_number + second_number
    t = 'додавання: {} + {}'.format(first_number, second_number)
if variant == 2:
    r = first_number - second_number
    t = ('віднімання {} - {} '.format(first_number, second_number ) )
if variant == 3:
    r = float(first_number / second_number)
    t = 'ділення: {} / {}'.format(first_number, second_number)
if variant == 4:
    r = first_number * second_number
    t = 'множення: {} * {}'.format(first_number, second_number)
if variant == 5:
    r = (first_number ** second_number) 
    t = 'піднесення до степення: {} ^ {}'.format(first_number, second_number)  
if variant == 6:
    r = math.sin(math.radians(first_number))
    t = 'сінус числа: {}'.format(first_number)
if variant == 7:
    r = math.cos(math.radians(first_number))
    t = 'косинус числа: {}'.format(first_number)
if variant == 8:
    r = math.asin(math.radians(first_number))
    t = 'арксінус числа: {}'.format(first_number)        
print ('Результат ',t,' = ',r)

