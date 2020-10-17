# Recurion ---> when a function calls itself.

# import sys
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())
# i = 0
def greet():
    # global i 
    # i = i + 1
    print("Hello")
    greet()

greet()