#Ask the user for the sentence
#checking the length of the characters in that sentence
#asking for the file name
#converting the file to .txt format
#writing on the file
#runnin the file with terminal

#LETS GOOOOOOOOOOOO #gg bye


sen = input("Enter your sentence: ")

length = len(sen)
print(length)

file_name = input("Enter the name of your file: ")
file_name = f"{file_name}.txt"

with open(file_name, "w") as f:
    f.write(sen)
    f.close()
print(f"Congo! You've sucessfully created a file named {file_name} and the number of characters are {length}")

