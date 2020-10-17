def hcf(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if((x%i==0) & (y%i==0)):
            hcf = i
    return hcf

x = int(input("Enter num1: "))
y = int(input("Enter num2: "))


print(f"The HCF of {x} & {y} is", hcf(x,y))
