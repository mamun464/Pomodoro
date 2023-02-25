import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=1
timer=None



# ---------------------------- TIMER RESET ------------------------------- #

def resetTimer():
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    topLebel.config(text="Timer", fg=GREEN)
    checkMark.config(text="")
    global reps
    reps=1


# ---------------------------- TIMER MECHANISM ------------------------------- #
def startTimer():
    global reps

    workSec=WORK_MIN*60
    shortBrakeSec=SHORT_BREAK_MIN*60
    longBrakeSec=LONG_BREAK_MIN*60
    if reps%2 != 0:
        topLebel.config(text="Work",fg=GREEN)
        #topLebel.config(text="Work")
        countDown(workSec)
        reps+=1
    elif reps % 8 ==0:
        topLebel.config(text="Break",fg=RED)
        countDown(longBrakeSec)
        reps+=1
    else:
        topLebel.config(text="Break", fg=PINK)
        countDown(shortBrakeSec)
        reps += 1



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countDown(count):
    global reps,timer
    countMin= math.floor(count/60)
    countSec = count % 60

    if countSec<10 and  countMin<10:
        canvas.itemconfig(time_text,text=f"0{countMin}:0{countSec}")

    elif countSec<10:
        canvas.itemconfig(time_text, text=f"{countMin}:0{countSec}")

    elif countMin<10:
        canvas.itemconfig(time_text,text=f"0{countMin}:{countSec}")
    else:
        canvas.itemconfig(time_text, text=f"{countMin}:{countSec}")

    if count > 0:
        timer=window.after(1000,countDown,count-1)
    else:
        startTimer()
        marks=""
        for _ in range(math.floor(reps/2)):
            marks+="✔"
        checkMark.config(text=marks)


    # ---------------------------- UI SETUP ------------------------------- #

window= Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,background=YELLOW)
canvas=Canvas(width=200,height=224,background=YELLOW,highlightthickness=0)

topLebel=Label(text="Timer",fg=GREEN,background=YELLOW,font=(FONT_NAME,30,"bold"))
topLebel.grid(column=1,row=0)

btn_start=Button(text="START", highlightthickness=0, command=startTimer)
btn_start.grid(column=0,row=2)

btn_reset=Button(text="RESET",highlightthickness=0,command=resetTimer)
btn_reset.grid(column=2,row=2)

checkMark=Label(background=YELLOW,fg=GREEN,font=(FONT_NAME,15,"bold"))

checkMark.grid(column=1,row=3)


tomato=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)

time_text=canvas.create_text(100,138,text="00:00",font=(FONT_NAME,30,"bold"),fill="white")
canvas.grid(column=1,row=1)



window.mainloop()