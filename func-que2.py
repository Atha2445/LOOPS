#Write a program to create a function using following conditions

#It should accept employer name and salary and display both
#If salary is missing then assign the defualt value as 10000 to salary

def prg(name,salary='10000'):
    print(name ,salary)

prg('Ben',12000)
prg('Mike',15000) 
prg('Bob',)   
prg('Sunny',1000000)