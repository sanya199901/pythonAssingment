x=int(input('enter five digit no.'))
#y=str(x)
#if len(x)==5:
a=0
while(x>0):
    b=x%10
    a=a+b
    x=x//10
print("The total sum of digits is:",a)
#else:
    #print('not a five digit no.')
              
          
