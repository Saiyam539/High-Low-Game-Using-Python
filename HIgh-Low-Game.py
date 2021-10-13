# Importing all modules 
from tkinter import *
import random

# For making blank GUI
window = Tk()
window.title("High Low Game")
window.minsize(600, 500)
window.maxsize(600, 500)

# Main function for the game
def check_ans(arg):
    global rand_num, real_rand_num

    if arg == "low":
        if real_rand_num < rand_num:
            message2.config(text=f"Yes, You are correct!!\nYou Won!!\nNumber is {real_rand_num}",fg="green")
        else:
            message2.config(text=f"No,You are wrong!!!\nYou loose!\nNumber is {real_rand_num}",fg="red")

    elif arg == "jackpot":
        if real_rand_num == rand_num:
            message2.config(text=f"Yes, You are correct!!\nYou Won!!\nNumber is {real_rand_num}",fg="green")
        else:
            message2.config(text=f"No,You are wrong!!!\nYou loose!\nNumber is {real_rand_num}",fg="red")
            
    elif arg=="high":
        if real_rand_num>rand_num:
            message2.config(text=f"Yes, You are correct!!\nYou Won!!\nNumber is {real_rand_num}",fg="green")
        else:
            message2.config(text=f"No,You are wrong!!!\nYou loose!\nNumber is {real_rand_num}",fg="red")
            

# Heading
heading = Label(window,text="High Low Game",bg="light blue",font=("bold",50))
heading.pack(fill=X)

# For display of main message for the game
rand_num=random.randint(1,100)
real_rand_num=random.randint(1,100)
message = Message(window,text=f"I just chose a secret number between 1 and 100.\nIs the secret number higher or lower than {rand_num}",font=("normal",30),width=600)
message.pack()

# For display of the result of the game
message2 = Message(window,font=("bold",30),width=600)
message2.pack()

# This are the three buttons for guessing the correct ans
low_button = Button(window,text="Low",font=("bold",45),command=lambda:check_ans("low"))
low_button.place(x=90,y=350)
jackpot_button = Button(window,text="Jackpot",font=("bold",45),command=lambda:check_ans("jackpot"))
jackpot_button.place(x=210,y=350)
high_button = Button(window,text="High",font=("bold",45),command=lambda:check_ans("high"))
high_button.place(x=400,y=350)

window.mainloop()