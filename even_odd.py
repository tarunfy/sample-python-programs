def s_even(n):
    a = 0
    for i in range(n+1):
        if i%2 == 0:
            a = i+a
        else:
            pass    
    print(a)    
n = int(input("Enter the number upto which you want the sum of even numbers: "))
s_even(n)        

