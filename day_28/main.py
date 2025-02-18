import tkinter as tk
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- GLOBAL VARIABLES -------------------------- #
repetitions = 0

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global repetitions
    repetitions = 0
    label_checkmark.config(text="")
    window.after_cancel(counter_id)
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global repetitions
    repetitions += 1

    if repetitions % 2 != 0:
        label_timer.config(text="Work", fg=GREEN)
        count_down(WORK_MIN)
    elif repetitions % 8 == 0:
        label_timer.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN)
    else:
        label_timer.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global counter_id
    minutes = floor(count / 60)
    seconds = count % 60

    canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")
    if count > 0:
        counter_id = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(floor(repetitions/2)):
            marks += "✔"
        label_checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label_timer = tk.Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
label_timer.grid(column=1, row=0)

label_checkmark = tk.Label(textvariable="", font=(FONT_NAME, 10), fg=GREEN, bg=YELLOW)
label_checkmark.grid(column=1, row=3)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_start = tk.Button(text="Start", font=(FONT_NAME, 12), bg="white", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = tk.Button(text="Reset", font=(FONT_NAME, 12), bg="white", highlightthickness=0, command=reset_timer)
button_reset.grid(column=3, row=2)

window.mainloop()
