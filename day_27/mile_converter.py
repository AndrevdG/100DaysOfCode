import tkinter as tk


def press_button():
    miles = float(input.get())
    km = round(miles * 1.609, 1)
    label_result.config(text=f"{km}")


FONT = ("Arial Black", 10)

# Setup window
window = tk.Tk()
window.title("Mile to KM Converter")
window.config(height=200, width=400, padx=30, pady=30)

# Create labels
label_miles = tk.Label(text="Miles", font=FONT)
label_miles.config(padx=5, pady=5)
label_miles.grid(row=0, column=2)

label_km = tk.Label(text="Km", font=FONT)
label_km.config(padx=5, pady=5)
label_km.grid(row=1, column=2)

label_equal = tk.Label(text="is equal to", font=FONT)
label_equal.config(padx=5, pady=5)
label_equal.grid(row=1, column=0)

label_result = tk.Label(text="0", font=FONT)
label_result.grid(row=1, column=1)
label_result.config(padx=5, pady=5)

# Create input
input = tk.Entry()
input.config(width=10)
input.grid(row=0, column=1)

# Create button
button = tk.Button(text="Calculate", command=press_button, font=FONT)
button.grid(row=2, column=1)

window.mainloop()
