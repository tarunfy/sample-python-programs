#n%2==0 --> even --> return odd(n-1)
#n%2!=0 --> odd --> return n + odd(n-1)

def odd(n):
    if n%2!=0:
        return n + odd(n-1)
    elif n==0:
        return n
    else:
        return odd(n-1)
num = int(input("Enter your num: "))
print(odd(num))
