A=[1,2,3,4,5]
B=[6,7,8,9,0]
c=int(input('enter sum here '))
for i in A:
    temp=c-i
    if c in B:
        print(i,temp)
