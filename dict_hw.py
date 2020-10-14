l1 = []
l1_len = int(input("Enter the num of friends you want to have in your data: "))
for i in range(1, l1_len+1):
    name = input(f"{i}). Enter name: ")
    l1.append(name)

dict_info = {}

for x in l1:
    number = int(input(f"Enter {x}'s phone number: "))
    dict_info[x] = number
print(f"The finalized dictionary is: {dict_info}")

p_num = list(dict_info.values())
print(f"The Phone numbers are {p_num}")

Name = list(dict_info.keys())
print(f"The Names are {Name}")

ques = input("Do you want to add a new friend in the dictionary? ")

if ques=="Yes" or ques=="yes":
    n_key = input("Enter his/her name: ")
    n_value = int(input("Enter his/her phone number: "))
    dict_info[n_key] = n_value
elif ques=="No" or ques=="no":
    print("Never mind :)")
else:
    print("Wrong input")

print(f"The Updated dictionary is {dict_info}")

ques2 = input("Do you want to delete any friend's info from the dictionary? ")

if ques2=="Yes" or ques2=="yes":
    d_name = input("Enter his/her name: ")
    if d_name in dict_info:
        del dict_info[d_name]
    else:
        print("Oops check the spelling or capitalization") 
elif ques2=="No" or ques2=="no":
    print("Never mind :)")
else:
    print("Wrong input")

print(f"The updated dictionary is {dict_info}")

ques3 = input("Do you want to modify anyone's phone number in your dictionary: ")

if ques3=="Yes" or ques3=="yes":
    m_name = input("Enter his/her name: ")
    if m_name in dict_info:
        m_num = int(input(f"Enter {m_name}'s new number: "))
        dict_info[m_name] = m_num
    else:
        print("Oops check the spelling or capitalization") 
elif ques3=="No" or ques3=="no":
    print("Never mind :)")
else:
    print("Wrong input")

print(f"The updated dictionary is {dict_info}")


ques4 = input("Hey, do you wanna check if someone's missing from the dictionary? ")

if ques4=="Yes" or ques4=="yes":
    c_name = input("Enter his/her name: ")
    if c_name in dict_info:
        print("He's alr in it.")
    elif c_name not in dict_info:
        print("Rip, he's not in.. #PAIN")    
    else:
        print("Oops check the spelling or capitalization") 
elif ques4=="No" or ques4=="no":
    print("Never mind :)")
else:
    print("Wrong input")

print(f"The updated dictionary is {dict_info}")

print(f"The dictionary after sorting by alphabetical order is:")
for j in sorted(dict_info):
    print((j, dict_info[j]), end = "")

