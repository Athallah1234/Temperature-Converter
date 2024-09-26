import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from datetime import datetime
import time

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def celsius_to_reaumur(celsius):
    return celsius * 4/5

def reaumur_to_celsius(reaumur):
    return reaumur * 5/4

def convert_temperature():
    try:
        temperature = float(entry.get())
        if var_input.get() == "Celsius":
            if var_output.get() == "Fahrenheit":
                result_value = celsius_to_fahrenheit(temperature)
            elif var_output.get() == "Kelvin":
                result_value = celsius_to_kelvin(temperature)
            elif var_output.get() == "Réaumur":
                result_value = celsius_to_reaumur(temperature)
            else:
                result_value = temperature
        elif var_input.get() == "Fahrenheit":
            if var_output.get() == "Celsius":
                result_value = fahrenheit_to_celsius(temperature)
            elif var_output.get() == "Kelvin":
                result_value = fahrenheit_to_celsius(temperature) + 273.15
            elif var_output.get() == "Réaumur":
                result_value = celsius_to_reaumur(fahrenheit_to_celsius(temperature))
            else:
                result_value = temperature
        elif var_input.get() == "Kelvin":
            if var_output.get() == "Celsius":
                result_value = kelvin_to_celsius(temperature)
            elif var_output.get() == "Fahrenheit":
                result_value = celsius_to_fahrenheit(kelvin_to_celsius(temperature))
            elif var_output.get() == "Réaumur":
                result_value = celsius_to_reaumur(kelvin_to_celsius(temperature))
            else:
                result_value = temperature
        elif var_input.get() == "Réaumur":
            if var_output.get() == "Celsius":
                result_value = reaumur_to_celsius(temperature)
            elif var_output.get() == "Fahrenheit":
                result_value = celsius_to_fahrenheit(reaumur_to_celsius(temperature))
            elif var_output.get() == "Kelvin":
                result_value = celsius_to_kelvin(reaumur_to_celsius(temperature))
            else:
                result_value = temperature

        # Update result and history
        result.set(f"{result_value:.{decimal_precision.get()}f} {var_output.get()}")
        history_text.insert(tk.END, f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: "
                                     f"{temperature:.2f} {var_input.get()} -> {result_value:.2f} {var_output.get()}\n")
        history_text.yview(tk.END)  # Auto-scroll to the bottom of the history

        # Copy result to clipboard
        root.clipboard_clear()
        root.clipboard_append(result.get())

        # Set timeout for error message
        root.after(3000, lambda: result.set(""))  # Clear result after 3 seconds

    except ValueError:
        result.set("Invalid input")

def clear_fields():
    entry.delete(0, tk.END)
    result.set("")

def swap_units():
    current_input = var_input.get()
    current_output = var_output.get()
    var_input.set(current_output)
    var_output.set(current_input)

# Create the main window
root = ThemedTk(theme="equilux")
root.title("Temperature Converter")
root.resizable(True, True)  # Allow resizing

# Variables
var_input = tk.StringVar(value="Celsius")
var_output = tk.StringVar(value="Celsius")
result = tk.StringVar()
decimal_precision = tk.IntVar(value=2)

# GUI Components
frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label = ttk.Label(frame, text="Enter Temperature:")
label.grid(column=0, row=0, sticky=tk.W)

entry = ttk.Entry(frame, width=20)
entry.grid(column=1, row=0, padx=(0, 10))

unit_label = ttk.Label(frame, text="Select Unit:")
unit_label.grid(column=0, row=1, sticky=tk.W)

input_unit_combobox = ttk.Combobox(frame, values=("Celsius", "Fahrenheit", "Kelvin", "Réaumur"), textvariable=var_input)
input_unit_combobox.grid(column=1, row=1, sticky=tk.W)

output_unit_combobox = ttk.Combobox(frame, values=("Celsius", "Fahrenheit", "Kelvin", "Réaumur"), textvariable=var_output)
output_unit_combobox.grid(column=1, row=2, sticky=tk.W)

precision_label = ttk.Label(frame, text="Decimal Precision:")
precision_label.grid(column=0, row=3, sticky=tk.W)

precision_entry = ttk.Entry(frame, width=5, textvariable=decimal_precision)
precision_entry.grid(column=1, row=3, sticky=tk.W)

convert_button = ttk.Button(frame, text="Convert", command=convert_temperature)
convert_button.grid(column=0, row=4, columnspan=2, pady=(10, 0))

clear_button = ttk.Button(frame, text="Clear", command=clear_fields)
clear_button.grid(column=0, row=5, columnspan=2, pady=(10, 0))

swap_button = ttk.Button(frame, text="Swap Units", command=swap_units)
swap_button.grid(column=0, row=6, columnspan=2, pady=(10, 0))

copy_button = ttk.Button(frame, text="Copy to Clipboard", command=lambda: root.clipboard_append(result.get()))
copy_button.grid(column=0, row=7, columnspan=2, pady=(10, 0))

result_label = ttk.Label(frame, textvariable=result)
result_label.grid(column=0, row=8, columnspan=2, pady=(0, 10))

# History Text
history_text = tk.Text(frame, height=6, width=40, wrap=tk.WORD)
history_text.grid(column=2, row=0, rowspan=8, padx=(10, 0), pady=(0, 10))
history_text.insert(tk.END, "Conversion History:\n")

# Start the main loop
root.mainloop()

