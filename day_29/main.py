import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


LABELFONT = ("Courier", 12, "bold")
PWDFILE = "./password.txt"
DEFAULTEMAIL = "myemail@provider.org"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(0, randint(8, 10))]
    password_list += [choice(numbers) for _ in range(0, randint(2, 4))]
    password_list += [choice(symbols) for _ in range(0, randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    pyperclip.copy(password)
    password_field.delete(0, tk.END)
    password_field.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_field.get()
    username = username_field.get()
    password = password_field.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo("Empty fields!", "Don't leave fields empty!")
        return

    saveOk = messagebox.askokcancel(website, f"Save password for user {username}?")
    if saveOk:
        with open(PWDFILE, mode="a") as file:
            file.write(f"{website} | {username} | {password}\n")
        website_field.delete(0, tk.END)
        password_field.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas
canvas = tk.Canvas(width=147, height=200)
lock_image = tk.PhotoImage(file="./logo.png")
canvas.create_image(74, 100, image=lock_image)
canvas.grid(column=1, row=0)

# labels
website_label = tk.Label(text="Website:", font=LABELFONT)
website_label.grid(column=0, row=1, sticky='e')
username_label = tk.Label(text="Email/Username:", font=LABELFONT)
username_label.grid(column=0, row=2, sticky='e')
password_label = tk.Label(text="Password:", font=LABELFONT)
password_label.grid(column=0, row=3, sticky='e')

# form fields
website_field = tk.Entry(width=35)
website_field.grid(column=1, row=1, columnspan=2, sticky='w')
website_field.focus()
username_field = tk.Entry(width=35)
username_field.grid(column=1, row=2, columnspan=2, sticky='w')
username_field.insert(0, DEFAULTEMAIL)
password_field = tk.Entry(width=21)
password_field.grid(column=1, row=3, sticky='w')

# form buttons
button_new_password = tk.Button(text="Generate Password", justify='left', command=generate_password)
button_new_password.grid(column=2, row=3)
button_add_file = tk.Button(text="Add", width=36, command=save)
button_add_file.grid(column=1, row=4, columnspan=2, sticky='w')

window.mainloop()
