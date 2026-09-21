def operation(a,b):
    return a+b, a-b, a/b, a*b
    '''sum = a+b
    sub = a-b
    div = a/b
    mul = a*b'''
x=int(input("Enter x = "))
y=int(input("Enter y = "))
sum, sub, div, mul = operation(x,y)
print("Sum=",sum)
print("Sub=",sub)
print("Div=",div)
print("Mul=",mul)
#print("result=",operation(x,y))
