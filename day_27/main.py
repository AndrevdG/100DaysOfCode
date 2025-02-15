import tkinter as tk


def button_clicked():
    my_label.config(text=input.get())


window = tk.Tk()
window.title("My very first GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tk.Label(text="I Am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


# Button
button = tk.Button(text="Click me", command=button_clicked)
button.grid(row=1, column=1)

new_button = tk.Button(text="Don't Push")
new_button.grid(row=0, column=2)


# Entry
input = tk.Entry(width=10)
input.grid(row=2, column=3)

# Keeps the window running / should be at the end of code
window.mainloop()
