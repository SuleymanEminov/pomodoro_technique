"""
Author: Suleyman Eminov

Program name: pomodoro technique timer

Description: this program helps students to keep
track of their pomodoro study sessions.

Concept: Pomodoro technique is a study technique
where student studies for certain amount of time and then
takes a break. This repeats multiples times. For example,
a student studies for 45 minutes and then takes 5 minute break.
Then he/she studies for 45 minutes, again.

Personally I find this technique very helpful.
"""

from tkinter import *
import math
import winsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
marks = ''


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    label.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    global reps
    reps = 0
    global marks
    marks = ''


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        label.config(fg=RED, text="LONG BREAK")
    elif reps % 2 == 0:
        countdown(short_break_sec)
        label.config(fg=PINK, text="SHORT BREAK")
    else:
        countdown(work_sec)
        label.config(fg=GREEN, text="WORK")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    print(count_min, count_sec)

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            global marks
            marks = ""
            work_sessions = math.floor(reps/2)
            for _ in range(work_sessions):
                marks += "✔"
                check_label.config(text=marks)
            for i in range(3):
                winsound.Beep(500, 500)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.grid(column=2, row=2)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, "bold"))

# Top label
label = Label(window, text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 26, 'bold'))
label.grid(column=2, row=1)

# start button
start_button = Button(text="Start", height=1, width=5, command=start_timer)
start_button.grid(column=1, row=3)

# reset button
reset_button = Button(text="Reset", height=1, width=5, command=reset)
reset_button.grid(column=3, row=3)

# check label
check_label = Label(fg=GREEN, bg=YELLOW, font=24)
check_label.grid(column=2, row=4)

window.mainloop()
