def factorial(num):
    if num==1:
        return num
    return num*factorial(num-1) 

ans = factorial(10)
print(ans)       