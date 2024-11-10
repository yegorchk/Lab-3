import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import random

# Весовые коэффициенты для символов
weights = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
    'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
    'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
    'Z': 26, '0' : 0, '1': 1, '2': 2, '3': 3, 
    '4': 4, '5' : 5, '6': 6, '7': 7, '8': 8, '9': 9
} 

# Интервал весов для блоков
weight_min = 30
weight_max = 35

# Функция генерации одного блока из четырех символов
def generate_block():
    while True:
        block = ''.join(random.choice(list(weights.keys())) for _ in range(4))
        block_weight = sum(weights[char] for char in block)
        if weight_min <= block_weight <= weight_max:
            return block

# Функция генерации ключа в формате XXXX-XXXX-XXXX
def generate_key():
    blocks = [generate_block() for _ in range(3)]
    key = '-'.join(blocks)
    key_label.configure(text=key)

# Настройка темы CustomTkinter
ctk.set_appearance_mode("light")  # Светлая тема

# Создание основного окна
window = ctk.CTk()
window.geometry('686x386')
window.resizable(width=False, height=False)

# Загрузка изображения
bg_img = Image.open('hq720-2.png')  # Убедитесь, что файл изображения существует
bg_img = bg_img.resize((686, 386))  # Изменение размера изображения
bg_img = ImageTk.PhotoImage(bg_img)  # Преобразование в PhotoImage

# Создание Canvas
canvas = ctk.CTkCanvas(window, width=1562, height=886)
canvas.place(x=0, y=0)


# Установка фона
canvas.create_image(0, 0, anchor="nw", image=bg_img)

# Метка для отображения ключа
key_label = tk.Label(canvas, text="", font=("Arial", 16), width=20, height=1, bg="#353b31", relief="solid")
key_label.place(x=46, y=90)

# Создание кнопки
button = ctk.CTkButton(window, text="Generate Key", font=("Comfortaa", 12), text_color="black", 
                       fg_color="#353b31", bg_color="#353b31", hover_color="grey", command=generate_key, border_width=2, border_color="black")
button_window = canvas.create_window(70, 130, anchor="nw", window=button)  # Размещение кнопки на Canvas

# Запуск главного цикла приложения
window.mainloop()