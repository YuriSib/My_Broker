

# # Создаем окно
# window = tk.Tk()
# window.title("Таблица из списка")
#
#
# def desk_window(data_list):
#     # Создаем Treeview (таблицу)
#     tree = ttk.Treeview(window)
#     tree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")  # Указываем количество колонок
#
#     for col_num in range(1, 9):
#         tree.column(f"{col_num}", anchor=tk.W, width=100)
#         tree.heading(f"{col_num}", text=f"Колонка {col_num}", anchor=tk.W)
#     # Добавляем данные из списка в таблицу
#     for i, values in enumerate(data_list, start=1):
#         tree.insert("", "end", iid=i, values=values)
#     # Пакуем таблицу
#     tree.pack()
#     # Запускаем главный цикл событий
#     window.mainloop()
#
#
# def update_table(data_list):
#     new_data = [
#         ("Новое значение 1", "Новое значение 2", "Новое значение 3", "Новое значение 4", "Новое значение 5",
#          "Новое значение 6", "Новое значение 7", "Новое значение 8"),
#         ("Еще одно значение 1", "Еще одно значение 2", "Еще одно значение 3", "Еще одно значение 4",
#          "Еще одно значение 5", "Еще одно значение 6", "Еще одно значение 7", "Еще одно значение 8"),
#         # Другие строки данных...
#     ]
#
#     # Очищаем текущие данные в таблице
#     for item in tree.get_children():
#         tree.delete(item)
#
#     # Добавляем новые данные в таблицу
#     for i, values in enumerate(data_list, start=1):
#         tree.insert("", "end", iid=i, values=values)
#
#     # Запускаем обновление через определенное время
#     root.after(5000, update_table)  # Обновление каждые 5000 миллисекунд (5 секунд)
#
#
# root = tk.Tk()
# root.title("Автоматическое обновление данных")
#
# tree = ttk.Treeview(root)
# tree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")
#
# for col_num in range(1, 9):
#     tree.column(f"{col_num}", anchor=tk.W, width=100)
#     tree.heading(f"{col_num}", text=f"Колонка {col_num}", anchor=tk.W)
import tkinter as tk
from tkinter import ttk
from openpyxl import load_workbook
import threading
import time


def update_table():
    global tree
    while True:
        # тут можно изменить название файла, при замене название также необходимо сменить в модуле main.py
        wb = load_workbook('биржевые данные.xlsx')
        sheet = wb.active
        rows = []
        for row in sheet.iter_rows(values_only=True):
            rows.append(row)
        tree.delete(*tree.get_children())
        for row in rows:
            tree.insert("", "end", values=row)
        time.sleep(10)


def create_gui():
    global tree
    root = tk.Tk()
    root.title("Excel Table Viewer")

    tree = ttk.Treeview(root)
    tree["columns"] = ("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8")

    for i in range(8):
        tree.column(f"#{i + 1}", width=100, anchor='center')
        tree.heading(f"#{i + 1}", text=f"Column {i + 1}")

    tree.pack()

    update_thread = threading.Thread(target=update_table)
    update_thread.daemon = True
    update_thread.start()

    root.mainloop()


