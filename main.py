from tkinter import *
import math
import os
import sys


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer) #Now I can cancel the timer
    # to change a canvas element we need to type to the particular canvas I want to change
    canvas.itemconfig(timer_text, text="00:00")  # text the element I want to change
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    global reps
    reps= 0 # Without it, it continues with the reps that were before



# ---------------------------- TIMER MECHANISM ------------------------------- # 
print(reps)
def star_timer():
    global reps
    reps += 1


    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60



    #If it's the 8th rep:
    if reps % 8 == 0:
        timer_label.config(text="break", fg=PINK, bg=YELLOW)
        count_down(long_break_sec)


    #If it's 2nd/4th/6th prep
    elif reps % 2 ==0:
        timer_label.config(text="Break", fg=RED, bg=YELLOW)
        count_down(short_break_sec)
    #If it's the 1st/3rd/5th/7th rep:
    else:
        count_down(work_sec)
        timer_label.config(text="Work")



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count/ 60) # 4.8 ---> 4
    count_sec = count % 60 #remainder



    if count_sec < 10:
        count_sec = f"0{count_sec}"

    #to change a canvas element we need to type to the particular canvas I want to change
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}") # text the element I want to change
    if count > 0 :
        global timer
        timer = window.after(1000, count_down, count -1 )
    else:
        star_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"

        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
#Set Up the window
window= Tk()
window.title("Pomodoro")
#bg= Background hex code
window.config(padx=100, pady=50, bg=YELLOW)

#Funtion to determine the correct path to the resource file
def resource_path(relative_path):
    # If running as a PyInstaller bundle, look in the _MEIPASS directory
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    # Otherwise, look in the same directory as the script
    return os.path.join(os.path.abspath("."), relative_path)


image_path=resource_path("tomato.png")



#remove the line - highlightthickness
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0 )
#Read through a file to get hold of a particula image
photo= PhotoImage(file=image_path)
#                          x    y
canvas.create_image(100, 112, image=photo)
#Create text
#Fill color of the text

timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold")) #To change the text in te canvas I assign the text to a variable
canvas.grid(column=1, row=1)



#Label
#fg= foreground
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)
check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)


#Buttons
star_button = Button(text="Star", font=(FONT_NAME, 10,),highlightthickness=0, command=star_timer)
star_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 10,),  highlightthickness=0, command= reset_timer)
reset_button.grid(column=2, row=2)




#Keep the window open
window.mainloop()

