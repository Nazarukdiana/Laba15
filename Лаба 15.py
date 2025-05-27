from tkinter import *
from tkinter import filedialog, messagebox, colorchooser, simpledialog

def new_file():
    text_area.delete(1.0, END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_area.delete(1.0, END)
            text_area.insert(END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get(1.0, END))

def exit_app():
    if messagebox.askokcancel("Вихід", "Ви дійсно хочете вийти?"):
        root.destroy()

def change_text_color():
    color = colorchooser.askcolor()[1]
    if color:
        text_area.config(fg=color)

def change_background_color():
    color = colorchooser.askcolor()[1]
    if color:
        text_area.config(bg=color)

def cut_text():
    text_area.event_generate("<<Cut>>")

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

def show_about():
    messagebox.showinfo("Про програму", "Це текстовий редактор на Python з використанням tkinter")

def show_help():
    messagebox.showinfo("Про автора", "Автор: Назарук Діана")

# Головне вікно
root = Tk()
root.title("Текстовий редактор")
root.geometry("800x600")

# Текстова область
text_area = Text(root, undo=True)
text_area.pack(fill=BOTH, expand=True)

# Меню
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Меню "Файл"
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Новий", command=new_file)
file_menu.add_command(label="Відкрити", command=open_file)
file_menu.add_command(label="Зберегти", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Вийти", command=exit_app)
menu_bar.add_cascade(label="Файл", menu=file_menu)

# Меню "Редагувати"
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Вирізати", command=cut_text)
edit_menu.add_command(label="Копіювати", command=copy_text)
edit_menu.add_command(label="Вставити", command=paste_text)
menu_bar.add_cascade(label="Редагувати", menu=edit_menu)

# Меню "Формат"
format_menu = Menu(menu_bar, tearoff=0)
format_menu.add_command(label="Колір тексту", command=change_text_color)
format_menu.add_command(label="Колір фону", command=change_background_color)
menu_bar.add_cascade(label="Формат", menu=format_menu)

# Меню "Довідка"
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Про програму", command=show_about)
help_menu.add_command(label="Про автора", command=show_help)
menu_bar.add_cascade(label="Довідка", menu=help_menu)

# Контекстне меню
context_menu = Menu(root, tearoff=0)
context_menu.add_command(label="Колір тексту", command=change_text_color)
context_menu.add_command(label="Колір фону", command=change_background_color)
context_menu.add_command(label="Зберегти", command=save_file)

def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

text_area.bind("<Button-3>", show_context_menu)

root.mainloop()
