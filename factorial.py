def fac(n):
    ans = 1
    if n>0:       
        for i in range(1, n+1):
            ans = i*ans
        print(f"Fact is {ans}")    
    elif n == 0:
        print(f"Factorial is {ans}")
    else:
        pass    
    
n = int(input("Enter your num: "))
fac(n)
print("Thnq")