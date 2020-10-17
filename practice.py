#Numerics(int, float, complex numbers)
#Booleans(Yes/No or True/False)
#sequences(list, tuple, sets, string)
#Dictionaries(key:value)
#mutable --> can be modified, example: List, set, dictionary
#immutable --> can't be modified example: tuple, string, int, float, boolean


# a = input("Pls enter your name: ")
# b = int(input("Pls enter your age: "))
# c = int(input("pls enter you class: "))

# print("Hi {}, your age is {} and you're in {} standard".format(a,b,c))

# print("Hi {a.upper()}, your age is {b} and you're in {c} standard.")

# course = {
#     'name': 'Python for everybody',
#     'students': 100_000_00,
#     'length': 3.2,
#     'lessons': ["strings", "data type", "Lists", 123]
# }
# print(course)
# print(type(course))
# print(type(course["lessons"]))
# print(course["lessons"])
# print(len(course["lessons"]))
# b = course["lessons"]
# print("b is ",b)

# course['name'] = 'pYthonSUcks'
# print(course)

# course['quality'] = "bad asf"
# print(course)

# del course['length']
# print(course)

# keys = course.keys()
# print(keys)

# values = course.values()
# print(values)

# info_want = input("Enter the name students lesson or subject you want: ")
# data = course.get(info_want,'agagaagagagaga')
# print(data)

# for key, value in course.items():
#     print(key,"--->", value)

# group = ("Tarun", "Velocity", "Shubhi", "Shubhi",)
# a = group.count("Shubhi")
# print(a)

# update = group[0:3]
# print(update)


# for item in update:
#     print(item)


# del group
# print(group)

# colors = {'Blue','Blue', 'red', 'orange', 'pink'}
# print(colors)


# colors.add('Violet')
# print(colors)
# colors.add('Violet')
# print(colors)


# colors.remove("orange")
# print(colors)


# lst = [1,2,2,1,'scsdc','dscsdc']
# s = set(lst)
# print(s)


# Booleans

# a = True
# print(type(a))

# print(a.bit_length())

# b = False
# print(b.bit_length())


# d = "csdd"
# e = ""
# print(bool(d))

# print(bool(e))

# print(bool({'anything'}))


# NONE dataType

# sports = None
# print(type(sports))

# print(bool(sports))

# if sports is None:
#     print("Hi")

# d = {
#     "thing": "thing3"
# }

# a = print(d.get('fsdcs', None))
# print(type(a))

# if a == None:
#     print("Hi")



# with open("230_files_test.txt", "w") as f:
#     f.write("Hello World, this is our first project programmitically created file")
#     f.close()
# with open("230_files_test.txt", "r") as f:
#     print(type(f))
#     contents = f.read()
#     f.close()


# with open("230_files_test.txt", "w") as f:
#     f.write("Updations")
#     f.close()
# print(contents)

# with open("230_files_test.txt", "a") as f:
#     f.write("\n this is line 4")
#     f.close()

# with open("230_files_test.txt", "r") as f:
#     print("f.name -->", f.name)
#     lines = f.readlines()
#     f.close()

# print(lines)
# print(type(lines))

# for line in lines:
#     print(line)

# with open("file_made_with_python.txt", "w") as T:
#     T.write("Youre a Kawaii girl")
#     T.close()

# with open("file_made_with_python.txt", "r") as T:
#     content = T.read()
#     T.close()
# print(content)

# with open("file_made_with_python.txt", "a") as T:
#     T.write("\n THIS IS A NEW LINE")
#     T.close()

# with open("file_made_with_python.txt", "r") as T:
#     line = T.readlines()
#     T.close()
# print(line)
# for i in range(0,5):
#     with open("file_made_with_python.txt", "a") as T:
#         k = i
#         T.write(f"\n {k}")
#         T.close()