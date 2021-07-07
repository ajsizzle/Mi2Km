from tkinter import *

# Main Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(height=200, width=350)
window.config(padx=20, pady=20)


# Kilometer Calculation
def kilo_calc():
    miles = float(miles_input.get())
    kilos = miles * 1.609
    km.config(text=kilos)


# Miles Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Miles Label
mi_label = Label(text="Miles")
mi_label.grid(column=2, row=0)

# Label
is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

# Kilometer Display
km = Label(text="0")
km.grid(column=1, row=1)

# Kilo Label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Calculate Button
button = Button(text="Calculate", command=kilo_calc)
button.grid(column=1, row=2)

window.mainloop()