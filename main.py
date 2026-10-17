import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
root = tk.Tk()
file_name = "main.txt"
code = "1"

def on():
    name = entr1.get()
    mark = entr2.get()  
    with open(file_name, 'a', encoding="utf-8") as e:
        e.write(f"Имя: {name}, Заметка  {mark}\n")
        messagebox.showinfo("Успешно", "Данные успешно внесены")

        entr1.delete(0, tk.END)
        entr2.delete(0, tk.END)


def ok(): 
    code1 = simpledialog.askstring("Проверка доступа", "Введите код доступа для безопасности", show="*")
    if code1 is None:
        return


    if code1 == code:
        confirm = messagebox.askyesno("Подтвердите", "Вы уверены, что хотите очистить все данные?\nДанное действие необратимо!")
        
        if confirm:
            with open(file_name, 'w', encoding="utf-8") as e:
                pass 
            
            messagebox.showinfo("Успешно", "Данные успешно удалены")
            entr1.delete(0, tk.END)
            entr2.delete(0, tk.END)
    else:
        messagebox.showerror("Ошибка безопасности", "Доступ запрещен!")
        root.destroy()


def dele():
    delete_name = simpledialog.askstring("Введите имя для удаления", "Имя")
    if delete_name is None:
        return
    delete_name = delete_name.strip()
    try:
        with open(file_name, 'r', encoding="utf=8") as e:
            lines = e.readlines()
            new_lines = []
            found = False

        for line in lines:
            if f"Имя ученика: {delete_name}," in line:
                found = True
            else:
                new_lines.append(line)
        if found:
                with open(file_name, 'w', encoding="utf=8") as e:
                    e.writelines(new_lines)
                    messagebox.showinfo("Успех", " Данные успешно удалены")
        else:
            messagebox.showerror("Ошибка", "Данные не найдены")
    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Файл с данными не найден")

lbl = tk.Label(root, text="Введите имя").pack(pady=10)
entr1 = tk.Entry(root, width=10)
entr1.pack(pady=11)
lbl1 = tk.Label(root, text="Введите заметку").pack(pady=15)
entr2 = tk.Entry(root, width=10)
entr2.pack(pady=16)  

btn1 = tk.Button(root, text="Добавить запись", command=on).pack(pady=17)
btn2 = tk.Button(root, text="Очистить файл с данными", command=ok).pack(pady=18)
btn2 = tk.Button(root, text="Удалить запись из файла", command=dele).pack(pady=19)
root.title("Учет данных")
root.geometry("360x450")
root.mainloop()
