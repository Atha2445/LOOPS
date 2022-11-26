def details(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)
details('Saheb',place='Baglan',age=22,contact_no=9090909088) 




a = 10
def func():
    global a 
    print(a)

func()
print(a)    






