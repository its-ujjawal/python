a=int(input("enter the value of a:"))
f=0
s=1
if(a>1):
    print("enter the valid number")
else:
    print("fabinocci series is",f,s,end=" ")
    for i in range(2,n):
        next=f+s
        print(next,end=" ")
        f=s
        s=next