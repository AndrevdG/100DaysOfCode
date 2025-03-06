import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGEFONT = ("Ariel", 40, "italic")
WORDFONT = ("Ariel", 60, "bold")


def wrong():
    pass


def right():
    pass


window = tk.Tk()
window.title("Flashy")
window.geometry("900x700")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = tk.PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
button_wrong_image = tk.PhotoImage(file="./images/wrong.png")
button_wrong = tk.Button(image=button_wrong_image, highlightthickness=0, command=wrong)
button_wrong.grid(column=0, row=1)
button_right_image = tk.PhotoImage(file="./images/right.png")
button_right = tk.Button(image=button_right_image, highlightthickness=0, command=right)
button_right.grid(column=1, row=1)

# Labels
label_language = tk.Label(text="French", font=LANGUAGEFONT, bg="white")
label_language.place(x=400, y=150, anchor="center")
label_word = tk.Label(text="trouve", font=WORDFONT, bg="white")
label_word.place(x=400, y=263, anchor="center")

window.mainloop()
