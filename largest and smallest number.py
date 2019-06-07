a = int(input("Enter number a:"))
b = int(input("Enter number b:"))
c = int(input("Enter number c:"))
if a > b and a > c:
    print("a is the largest number")
elif b > c and b > a:
    print("b is the largest number")
else:
    print("c is the largest number")
if a < b and a < c:
    print("a is the smallest number")
elif b < c and b < a:
    print("b is the smallest number")
else:
    print("c is the smallest number")
