def ans(n):
    if n<=1:
        return n
    elif n>1:
        return n + ans(n-1)
    else:
        pass
num = int(input("Enter the nth number: "))
for i in range(1,num+1):
    print(ans(i))