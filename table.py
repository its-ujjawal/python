'''n=int(input("enter the number: "))
print(n)
print(n*2)
print(n*3)
print(n*4)
print(n*5)
print(n*6)
print(n*7)
print(n*8)
print(n*9)
print(n*10)'''
n=int(input("Enter the number to print the tables for:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)