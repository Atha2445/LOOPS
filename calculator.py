#Function for addition 
def add(x,y):
    return x + y

#Function for substraction
def sub(x,y):
    return x - y

#Function for multiplication
def multiply(x,y):
    return x * y

#Function for division
def divide(x,y):
    return x/y

print('Select operation.')
print('1.add')
print('2.sub')
print('3.multiply')
print('4.divide')            

#For choice from user
choice = input('Enter choice(1/2/3/4):')
 
if choice in ('1','2','3','4'):
    num1 = float(input('Enter first number:'))
    num2 = float(input('Enter second:'))

    if choice == '1':
        print(num1, '+', num2, '=', add(num1,num2))

    elif choice == '2':
        print(num1, '-', num2, '=', sub(num1,num2))

    elif choice == '3':
        print(num1, '*', num2, '=', multiply(num1,num2))        