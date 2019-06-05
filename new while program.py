name = ""
while not name:
    print("What is your name ?")
    name = input()
print("How many guest do you have?")
NoOfGuest = int(input())
if NoOfGuest:
    print("Be sure to have enough room for " + str(float(NoOfGuest)) + " guests.")
print("Done.")