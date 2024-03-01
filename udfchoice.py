import UDF

while True:
    print("*"*50)
    print("1. Odd Even")
    print("2. Max Of Two")
    print("3. Max Of Three")
    print("4. Fibonacci")
    print("5. Prime")
    print("6. Exit")
    print("*"*50)

    choice=int(input("Enter Your Choice : "))
    print("*"*50)

    if choice==1:
        a=int(input("Enter Value : "))
        UDF.oddeven(a)
        print("*"*50)
    elif choice==2:
        a=int(input("Enter Value : "))
        b=int(input("Enter Value : "))
        UDF.maxoftwo(a,b)
        print("*"*50)
    elif choice==3:
        a=int(input("Enter Value : "))
        b=int(input("Enter Value : "))
        c=int(input("Enter Value : "))
        UDF.maxofthree(a,b,c)
        print("*"*50)
    elif choice==4:
        n=int(input("Enter Value : "))
        UDF.fibonacci(n)
        print("*"*50)
    elif choice==5:
        n=int(input("Enter Value : "))
        UDF.prime(n)
        print("*"*50)
    elif choice==6:
        print("Thank you")
        print("*"*50)
        break
    else:
        print("Invalid")
        print("*"*50)
    
        
               
