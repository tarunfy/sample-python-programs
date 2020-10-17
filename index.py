#fibonacci series:
def fibo(n):
    a = 0 #0 1 1 2 3
    b = 1
    print(a)
    print(b)
    for i in range(2,n):
        c = a + b
        a = b
        b = c
        print(c)
fibo(5)