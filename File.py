import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Сладкие слова)")
window.geometry("300x150")

label = tk.Label(window, text="Введите ваше имя (только 1 слово):", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(window, width=30)
entry.pack(pady=5)

def greet():
    name = entry.get()
    if name:
        messagebox.showinfo("Приветствие", f"Привет, {name}! твоя мать шлюха :)")
    else:
        messagebox.showwarning("Ошибка", "Поле не должно быть пустым!")

button = tk.Button(window, text="Поздороваться", command=greet)
button.pack(pady=10)

window.mainloop()
