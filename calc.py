# pip install customtkinter
import customtkinter as ctk

# Создаем главное окно
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("+800+300")
app.title("Калькулятор")
app.resizable(False, False)

# Список кнопок и их текстов
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('00', 4, 1), ('.', 4, 2), ('+', 4, 3),
]


# Функция для обновления текста в поле ввода
def click(s):
    calc_entry.configure(state="normal")
    calc_entry.insert(len(calc_entry.get()), s)
    calc_entry.configure(state="readonly")


# Функция для очистки поля ввода
def clear_entry():
    calc_entry.configure(state="normal")
    calc_entry.delete(0, "end")
    calc_entry.configure(state="readonly")


# Функция для выполнения вычислений
def calculate():
    try:
        calc_entry.configure(state="normal")
        result = eval(calc_entry.get())
        calc_entry.delete(0, "end")
        calc_entry.insert(0, result)
        calc_entry.configure(state="readonly")
    except Exception as e:
        print(e)
        calc_entry.configure(state="normal")
        calc_entry.delete(0, "end")
        calc_entry.insert(0, "Error")
        calc_entry.configure(state="readonly")


# Создаем фреймы для размещения кнопок
frame_1 = ctk.CTkFrame(app, fg_color="transparent")
frame_1.grid(row=0, column=0, sticky="nsew")

frame_2 = ctk.CTkFrame(app, fg_color="transparent")
frame_2.grid(row=1, column=0, padx=3, sticky="nsew")

frame_3 = ctk.CTkFrame(app, fg_color="transparent")
frame_3.grid(row=2, column=0, padx=3, sticky="nsew")

# Создаем поле ввода для отображения результатов вычислений
calc_entry = ctk.CTkEntry(frame_1, width=232, height=60, font=("Arial", 24), state="readonly", justify=ctk.RIGHT)
calc_entry.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

# Создаем кнопки и их расположение в сетке
for (text, row, col) in buttons:
    btn = ctk.CTkButton(frame_2, text=text, command=lambda t=text: click(t), width=55, height=55, font=("Arial", 20))
    btn.grid(row=row, column=col, padx=2, pady=2)
    if text in ["+", "-", "*", "/"]:
        btn.configure(fg_color="#335616", hover_color="#4D6F05")

# Создаем кнопки для операций "C" и "="
button_clear = ctk.CTkButton(frame_3, text="C", width=114, height=50, font=("Arial", 20), fg_color="#BC0951",
                             hover_color="#FB3E6D", command=clear_entry)
button_clear.grid(row=0, column=0, padx=2, pady=(2, 5))

button_calc = ctk.CTkButton(frame_3, text="=", width=114, height=50, font=("Arial", 20), fg_color="#263541",
                            hover_color="#315565", command=calculate)
button_calc.grid(row=0, column=1, padx=2, pady=(2, 5))

if __name__ == '__main__':
    # Запускаем цикл обработки событий приложения
    app.mainloop()
