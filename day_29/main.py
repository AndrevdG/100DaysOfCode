import tkinter as tk

LABELFONT = ("Courier", 12, "bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas
canvas = tk.Canvas(width=147, height=200)
lock_image = tk.PhotoImage(file="./logo.png")
print(lock_image)
canvas.create_image(75, 100, image=lock_image)
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
username_field = tk.Entry(width=35)
username_field.grid(column=1, row=2, columnspan=2, sticky='w')
password_field = tk.Entry(width=21)
password_field.grid(column=1, row=3, sticky='w')

# form buttons
button_new_password = tk.Button(text="Generate Password")
button_new_password.grid(column=2, row=3, sticky='w')
button_add_file = tk.Button(text="Add", width=36)
button_add_file.grid(column=1, row=4, columnspan=2, sticky='w')

window.mainloop()
