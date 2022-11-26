# Function for Fibonacci number
def Fibonacci(num):
    if num == 0:
        return 0

    elif num == 1 or num == 2:
        return 1
 
    elif num:
        return Fibonacci(num-1) + Fibonacci(num-2)
    else:
        print('Enter Positive Integer')    
print(Fibonacci(17))
 
