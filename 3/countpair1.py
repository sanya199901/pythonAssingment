def printpair(arr,arr_size,sum):
    s=set()
    for i in range (0,arr_size):
        temp=sum-arr[i]
        if (temp in s):
            print("pair with given sum"+"is ("+str(arr[i])+","+str(temp)+","+")")
        s.add(arr[i])

A=[1,4,5,7,8,9]
n=17
printpair(A,len(A),n)
