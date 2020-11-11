'''
LEGB
Local, Enclosing, Global, Built-in
'''

# import builtins

# print(dir(builtins))

# def my_min():
#     pass

# m = min([4,2,1,5,3])
# print(m)


x = "global x"

# def test(z):
#     x = "local x"
#     # print(y)
#     print(z)

# test('local z')
# print(x)

def outer():
    # x = 'outer x'

    def inner():
        # nonlocal x
        # x = 'inner x'
        print(x)
    inner()
    print(x)

outer()
print(x)