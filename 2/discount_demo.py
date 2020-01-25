purchase=input('enter the number of packages purchased ')
pakage=99

if purchase<10:
    cost=purchase*package
    #discount=0
    print('the total mount is ',cost)
    print('no discount')
elif purchase in range(10,20):
    cost= purchase*pakage
    discount=0.1*cost
    amount=cost - discount
    print('the amount of discount is ',discount)
    print('the total amount is ',amount)

elif purchase in range(20,50):
    cost= purchase*pakage
    discount=0.2*cost
    amount=cost - discount
    print('the amount of discount is ',discount)
    print('the total amount is ',amount)

elif purchase in range(50,100):
    cost= purchase*pakage
    discount=(3/10)*cost
    amount=cost - discount
    print('the amount of discount is ',discount)
    print('the total amount is ',amount)

else:
    cost= purchase*pakage
    discount=(4/10)*cost
    amount=cost - discount
    print('the amount of discount is ',discount)
    print('the total amount is ',amount)
    
