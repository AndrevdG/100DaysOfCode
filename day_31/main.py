import tkinter as tk
import pandas as p
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGEFONT = ("Ariel", 40, "italic")
WORDFONT = ("Ariel", 60, "bold")


def flip_card():
    canvas.itemconfig(card_background, image=card_back_image)
    canvas.itemconfig(label_language, text='English', fill='white')
    canvas.itemconfig(label_word, text=current_word['English'], fill='white')


def next_card():
    global current_word
    current_word = choice(words)
    canvas.itemconfig(card_background, image=card_front_image)
    canvas.itemconfig(label_language, text='French', fill='black')
    canvas.itemconfig(label_word, text=current_word['French'], fill='black')
    window.after(3000, flip_card)


# Read words
words = p.read_csv("./data/french_words.csv").to_dict(orient='records')
current_word = {}

# Window
window = tk.Tk()
window.title("Flashy")
window.geometry("900x700")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = tk.PhotoImage(file="./images/card_front.png")
card_back_image = tk.PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)

# Labels
label_language = canvas.create_text(400, 150, text="HELLO!", font=LANGUAGEFONT, fill='black')
label_word = canvas.create_text(400, 263, font=WORDFONT)

# Buttons
button_wrong_image = tk.PhotoImage(file="./images/wrong.png")
button_wrong = tk.Button(image=button_wrong_image, highlightthickness=0, command=next_card)
button_wrong.grid(column=0, row=1)
button_right_image = tk.PhotoImage(file="./images/right.png")
button_right = tk.Button(image=button_right_image, highlightthickness=0, command=next_card)
button_right.grid(column=1, row=1)

next_card()

window.mainloop()
