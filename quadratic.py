#QUADRATIC EQUATION's ROOTS USING FUNCTIONS IN PYTHON:
def roots(a,b,c):
    print(f"your quadratic equation is --> {a}x^2 + {b}x + {c} = 0")
    print("Its roots are as follow:")
    r1 = (b*b - 4*a*c)
    sqrt = r1**0.5
    first_root = ((-b) + (sqrt))/(2*a)
    sec_root = ((-b) - (sqrt))/(2*a)
    print(f"1st root ---> {first_root}")
    print(f"2nd root ---> {sec_root}")
a = int(input("Enter the coefficient of x^2: "))
b = int(input("Enter the coefficient of x: "))
c = int(input("Enter the constant term: "))
roots(a,b,c)
print("Thnq")

    