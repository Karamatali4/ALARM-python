from tkinter import *
import tkinter as tk
from tkinter import messagebox
from utilities import set_alarm


def create_gui():
    window = tk.Tk()
    window.title("Alarm Clock")
    window.geometry("400x300")

   
    tk.Label(window, text="Alarm Clock")
    tk.Label(window, text="Hour (HH):").grid(row=0, column=0)
    hour_input = tk.Entry(window)
    hour_input.grid(row=0, column=1)

    tk.Label(window, text="Minute (MM):").grid(row=1, column=0)
    minute_input = tk.Entry(window)
    minute_input.grid(row=1, column=1)

    period = tk.StringVar(value="AM")
    tk.Radiobutton(window, text="AM", variable=period, value="AM").grid(row=2, column=0)
    tk.Radiobutton(window, text="PM", variable=period, value="PM").grid(row=2, column=1)

    set_alarm_button = tk.Button(window, text="Set Alarm", command=lambda: set_alarm(hour_input.get(), minute_input.get(), period.get(), window))
    set_alarm_button.grid(row=3, column=0)

    exit_button = tk.Button(window, text="Exit", command=window.quit)
    exit_button.grid(row=3, column=1)

    window.mainloop()



