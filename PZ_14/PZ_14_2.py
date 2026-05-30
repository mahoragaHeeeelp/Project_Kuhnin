import tkinter as tk
from tkinter import messagebox
 
root = tk.Tk()
root.title("Расстояние между автомобилями")
root.geometry("360x280")
root.resizable(False, False)
 
fields = {}
 
for i, label in enumerate(["Скорость 1-го авто (км/ч)", "Скорость 2-го авто (км/ч)", "Начальное расстояние (км)", "Время движения (часы)"]):
    tk.Label(root, text=label, anchor="w").grid(row=i, column=0, padx=16, pady=8, sticky="w")
    e = tk.Entry(root, width=14)
    e.grid(row=i, column=1, padx=16, pady=8)
    fields[label] = e
 
result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, fg="blue", wraplength=320, justify="left").grid(row=5, column=0, columnspan=2, padx=16, pady=4)
 
def calculate():
    try:
        vals = list(map(lambda e: float(e.get()), fields.values()))
        V1, V2, S, T = vals
        distance = abs(S - (V1 + V2) * T)
        result_var.set(f"Расстояние через {T} ч: {distance:.2f} км")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")
 
tk.Button(root, text="Рассчитать", command=calculate, width=16).grid(row=4, column=0, columnspan=2, pady=10)
 
root.mainloop()
