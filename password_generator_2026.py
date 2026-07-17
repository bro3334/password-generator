import customtkinter as ctk
import random
import string
import tkinter as tk
from tkinter import messagebox, scrolledtext

# Настройка темы
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Генератор паролей 2026")
        self.geometry("700x700")
        self.resizable(False, False)

        # Заголовок
        self.label = ctk.CTkLabel(self, text="Генератор паролей", font=("Arial", 24, "bold"))
        self.label.pack(pady=20)

        # Основная рамка
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(fill="both", expand=True, padx=30, pady=20)

        # Длина пароля
        self.length_label = ctk.CTkLabel(self.frame, text="Длина пароля:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)
        self.length_entry = ctk.CTkEntry(self.frame, placeholder_text="12")
        self.length_entry.insert(0, "12")
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        # Количество паролей
        self.count_label = ctk.CTkLabel(self.frame, text="Количество:")
        self.count_label.grid(row=1, column=0, padx=10, pady=10)
        self.count_entry = ctk.CTkEntry(self.frame, placeholder_text="1")
        self.count_entry.insert(0, "1")
        self.count_entry.grid(row=1, column=1, padx=10, pady=10)

        # Чекбоксы
        self.use_lower = ctk.IntVar(value=1)
        self.use_upper = ctk.IntVar(value=1)
        self.use_digits = ctk.IntVar(value=1)
        self.use_symbols = ctk.IntVar(value=1)

        ctk.CTkCheckBox(self.frame, text="Строчные (a-z)", variable=self.use_lower).grid(row=2, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkCheckBox(self.frame, text="Заглавные (A-Z)", variable=self.use_upper).grid(row=2, column=1, padx=10, pady=5, sticky="w")
        ctk.CTkCheckBox(self.frame, text="Цифры (0-9)", variable=self.use_digits).grid(row=3, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkCheckBox(self.frame, text="Спецсимволы", variable=self.use_symbols).grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Кнопки
        self.btn_frame = ctk.CTkFrame(self.frame)
        self.btn_frame.grid(row=4, column=0, columnspan=2, pady=20)

        self.generate_btn = ctk.CTkButton(self.btn_frame, text="Генерировать", command=self.generate)
        self.generate_btn.pack(side="left", padx=10)

        self.clear_btn = ctk.CTkButton(self.btn_frame, text="Очистить", command=self.clear_output, fg_color="#e67e22")
        self.clear_btn.pack(side="left", padx=10)

        self.save_btn = ctk.CTkButton(self.btn_frame, text="Сохранить", command=self.save_to_file, fg_color="#3498db")
        self.save_btn.pack(side="left", padx=10)

        # Поле вывода
        self.output_frame = ctk.CTkFrame(self.frame)
        self.output_frame.grid(row=5, column=0, columnspan=2, pady=20, sticky="nsew")

        self.output_text = scrolledtext.ScrolledText(
            self.output_frame,
            wrap=tk.WORD,
            font=("Courier", 12),
            bg="#2b2b2b",
            fg="#00ffaa",
            insertbackground="white"
        )
        self.output_text.pack(fill="both", expand=True, padx=10, pady=10)

        self.frame.grid_rowconfigure(5, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

    def generate(self):
        try:
            length = int(self.length_entry.get())
            count = int(self.count_entry.get())
            if length < 1 or count < 1:
                messagebox.showerror("Ошибка", "Длина и количество должны быть > 0")
                return

            chars = ""
            if self.use_lower.get():
                chars += string.ascii_lowercase
            if self.use_upper.get():
                chars += string.ascii_uppercase
            if self.use_digits.get():
                chars += string.digits
            if self.use_symbols.get():
                chars += string.punctuation

            if not chars:
                messagebox.showerror("Ошибка", "Выберите хотя бы один тип символов")
                return

            passwords = [''.join(random.choice(chars) for _ in range(length)) for _ in range(count)]

            self.output_text.delete(1.0, tk.END)
            if count == 1:
                self.output_text.insert(tk.END, passwords[0])
            else:
                for i, pwd in enumerate(passwords, 1):
                    self.output_text.insert(tk.END, f"{i:2}. {pwd}\n")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные числа")

    def clear_output(self):
        self.output_text.delete(1.0, tk.END)

    def save_to_file(self):
        content = self.output_text.get(1.0, tk.END).strip()
        if not content:
            messagebox.showwarning("Внимание", "Нет паролей для сохранения")
            return
        with open("passwords.txt", "w", encoding="utf-8") as f:
            f.write(content)
        messagebox.showinfo("Успех", "Пароли сохранены в файл passwords.txt")

if __name__ == "__main__":
    app = App()
    app.mainloop()