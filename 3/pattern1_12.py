def pattern(n):
    for i in range(1,n+1):
        for j in range(i,n+1):
            print("*",end="")
        print()
    for i in range(2,n+1):
        for j in range(2,i+1):
            print("*",end="")
        print("")
n=int(input('enter number '))
pattern(n)            
