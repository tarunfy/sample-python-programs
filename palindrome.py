def pal(str):
    a = str
    b = "" 
    for i in a:
        b = i + b
    print(b)

    if a == b:
        print("palindrome")
    else:
        print("not a palindrome")

x = input("enter your word: ")
pal(x)



