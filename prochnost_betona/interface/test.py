# from tkinter import *
# from tkinter import ttk  # подключаем пакет ttk
#
# root = Tk()
# root.title("Прочность бетона")
# root.geometry("600x400")
#
# btn = ttk.Button()  # создаем кнопку из пакета ttk
# btn.pack()  # размещаем кнопку в окне
# btn['text'] = 'Прочность бетона'
#
#
# root.mainloop()

from tkinter import *
from tkinter import ttk


def show_masege():
    print(entry.get())

root = Tk()
root.title("METANIT.COM")
root.geometry("300x400")

position = {"padx": 20, "pady": 6, "anchor": NW}

up = "Вверх"
down = "Вниз"
side = "Вбок"
res = 'Результат'
kick = StringVar(value='Направление удара')
kick_data = StringVar(value='Введите значения через пробел')

header_data = ttk.Label(textvariable=kick_data)
header_data.pack(**position)

entry = ttk.Entry(width=150)
entry.pack(**position)

header_btn = ttk.Label(textvariable=kick)
header_btn.pack(**position)

up_btn = ttk.Button(text=up, command=show_masege)
up_btn.pack(**position)

down_btn = ttk.Button(text=down)
down_btn.pack(**position)

side_btn = ttk.Button(text=side)
side_btn.pack(**position)

root.mainloop()