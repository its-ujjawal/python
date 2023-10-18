num=int(input("enter a value:"))
num2=0
while(num>0):
    b=num%10
    num2=num2*10+b
    num=num//10
print("reverse number", num2)