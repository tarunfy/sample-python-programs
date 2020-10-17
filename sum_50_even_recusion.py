#n%2==0 --> even --> return n
#n%2!=0 --> odd --> return even(n-1)

def even(n):
    if n==1:
        return 2
    elif n%2==0:
        return n + even(n-1)
    else:
        return even(n-1)
num = int(input("Enter your num: "))        
print(even(num)) 
