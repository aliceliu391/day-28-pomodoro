from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    global reps, checkmark_string
    reps = 0
    checkmark_string = ""
    checkmarks.config(text=checkmark_string)


# ---------------------------- TIMER MECHANISM ------------------------------- #

work_sec = WORK_MIN * 60
short_break_sec = SHORT_BREAK_MIN * 60
long_break_sec = LONG_BREAK_MIN * 60


def start_timer():
    global reps, checkmark_string
    reps += 1

    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps, checkmark_string
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 != 0:
            checkmark_string += "✔"
            checkmarks.config(text=checkmark_string)
        if reps % 8 == 0:
            checkmark_string = ""
            checkmarks.config(text=checkmark_string)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, padx=0, pady=0, width=4, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, padx=0, pady=0, width=4, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark_string = ""
checkmarks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "normal"))
checkmarks.grid(column=1, row=3)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "normal"))
title_label.grid(column=1, row=0)

window.mainloop()
