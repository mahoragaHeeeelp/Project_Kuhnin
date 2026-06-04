""" Вариант 5. Даны два целых числа: A,B.
 Проверить истинность высказывания: "Справедливы неравенства A>0 или B<-2" """

import tkinter as tk
from tkinter import messagebox


def check_condition():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        result = (a > 0) or (b < -2)
        label_result.config(text=f"Результат: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите целые числа!")


root = tk.Tk()
root.title("Вариант 5 - Проверка неравенств")
root.geometry("350x200")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Введите A:").grid(row=0, column=0, sticky="w", pady=5)
entry_a = tk.Entry(frame, width=20)
entry_a.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Введите B:").grid(row=1, column=0, sticky="w", pady=5)
entry_b = tk.Entry(frame, width=20)
entry_b.grid(row=1, column=1, pady=5)

btn_check = tk.Button(frame, text="Проверить", command=check_condition)
btn_check.grid(row=2, column=0, columnspan=2, pady=15)

label_result = tk.Label(frame, text="Результат: ", font=("Arial", 11, "bold"))
label_result.grid(row=3, column=0, columnspan=2)

root.mainloop()
