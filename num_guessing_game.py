import random
import math
import tkinter as tk

window = tk.Tk()

window.title("Number Guessing Game")
window.geometry("400x400")


#Functions:
def Range():
     uL = int(entry_1.get())
     lL = int(entry_2.get())
     chances = str(round(math.log(uL-lL+1, 2)))
     p = "The number of attempts\nyou have are:"   
     return p + chances



def popup():
    global window
    pop = Range()
    pop_display = tk.Text(master=window, height=5, width=25)
    pop_display.place(relx=0.5, rely=0.4, anchor="center")
    pop_display.insert(tk.END, pop)
    



def fin():  
    actual_value = int(entry_3.get())
    user_value = int(entry_4.get())
    if actual_value==user_value:
        ret = "YESSSSIRRRR :)"
    elif user_value>actual_value:
        ret = "You're too high, kiddo.."
    elif user_value<actual_value:
        ret = "You're too low kid!!"
    else:
        ret = "DUMB OR WHAT?"
    label_result["text"] = ret




label_1 = tk.Label(text="U_LIMIT --> ")
label_1.place(relx=0, rely=0, anchor="nw", x=10, y=5)

entry_1 = tk.Entry(window, relief="groove", width=5, bd=2, justify="center")
entry_1.place(relx=0.1, rely=0, anchor="nw", x=40, y=5)

label_2 = tk.Label(text="L_LIMIT --> ")
label_2.place(relx=0, rely=0.1, anchor="nw", x=10, y=10)

entry_2 = tk.Entry(window, relief="groove", width=5, bd=2, justify="center")
entry_2.place(relx=0.1, rely=0.1, anchor="nw", x=40, y=10)

Play_button = tk.Button(window, text="PLAY", fg="black", bg="white", activebackground="black", activeforeground="white", bd=4, height=2, width=20, command= popup)
Play_button.place(relx=1, rely=0, anchor="ne")

label_3 = tk.Label(text="uValue --> ")
label_3.place(relx=0, rely=0.65, anchor="sw", x= 10)

entry_3 = tk.Entry(window, relief="groove", width=5, bd=2, justify="center",show="*")
entry_3.place(relx=0.1, rely=0.65, anchor="sw", x=40)

Check_button = tk.Button(window, text="CHECK", fg="black", bg="white", activebackground="black", activeforeground="white", bd=2, height=2, width=20, command=fin)
Check_button.place(relx=1, rely=0.67, anchor="se")

label_4 = tk.Label(text="GUESS --> ")
label_4.place(relx=0, rely=0.7, anchor="sw", x=10, y=10)

entry_4= tk.Entry(window, relief="groove", width=5, bd=2, justify="center")
entry_4.place(relx=0.1, rely=0.69, anchor="sw", x=40, y=20)


label_result = tk.Label(text="Good Luck!")
label_result.place(relx=0.45, rely=0.8, anchor="center")


window.mainloop()

# lL = int(input("Enter the lower limit: "))
# uL = int(input("Enter the upper limit: "))

# actual_number = random.randint(lL, uL)

# chances = round(math.log(uL-lL+1, 2))
# print(f"You have {chances} attempts in total")


# Attempts = 0
# print("\n\t\tLETS PLAY")
# while Attempts < chances:
#     Attempts += 1
    
#     print(f"\n\tAttempt number ---> {Attempts}")
    
#     user_guess = int(input("Guess the number: "))

#     if user_guess==actual_number:
#         if Attempts==1:
#             print(f"Congratulations buddy you have guessed the number in {Attempts}st attempt")  
#         else:  
#             print(f"Congratulations buddy you have guessed the number in {Attempts} attempts")
#         break
#     elif user_guess>actual_number:
#         print("Oof! Too high bro")
#     elif user_guess<actual_number:
#         print("Oof! Too small bro")
#     else:
#         print("Seems like you went outside the range or something")

# print(f"Sorry,You lost the number was {actual_number}")
# print("Better luck nxt time!")
