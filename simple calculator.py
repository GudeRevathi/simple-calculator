def adition(a,b):
    c=a+b 
    print(c)
def subtract(a,b):
    c=a-b 
    print(c) 
def multiplication(a,b):
    c=a*b 
    print(c)
def division(a,b):
    c=a/b 
    print(c)
while True:
    print("1. adition") 
    print("2. subtract")
    print("3. multiplication")
    print("4. division")
    print("5. exits")
    choice=int(input("enter your choice(1-5)"))
    if choice==1:
        n1=int(input("enter a number: "))
        n2=int(input("enter a number: "))
        adition(n1,n2)
    elif choice==2:
        n1=int(input("enter a number: "))
        n2=int(input("enter a number: "))
        subtract(n1,n2)
    elif choice==3:
        n1=int(input("enter a number: "))
        n2=int(input("enter a number: "))
        multiplication(n1,n2)
    elif choice==4:
        n1=int(input("enter a number: "))
        n2=int(input("enter a number: "))
        division(n1,n2)
    elif choice==5:
        print("exits")
        break
    else:
        print("invalid choice please try again")