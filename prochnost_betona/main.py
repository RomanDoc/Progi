from tkinter import *
from tkinter import ttk

from prochnost_betona.config_data.PROCHNOST import KICK_UP, KICK_DOWN, KICK_SIDE
from prochnost_betona.utils.num_operations.average_calculation import int_res


def kick_up():
    res = int_res(entry.get())
    """
    Показывает прочность бетона при ударе вверх
    # :param number: значение удара
    # :type number: int
    :return: возвращает прочность бетона
    """
    if 20 <= res <= 50:
        print('Прочность бетона: {res} Мпа'.format(res=KICK_UP[res]))
        # return 'Прочность бетона: {res} Мпа'.format(res=KICK_UP[result])
    elif res < 20:
        return 'Прочность бетона меньше 10.3 Мпа'
    elif res > 50:
        return 'Прочность бетона больше 56.8 Мпа'


def kick_down():
    res = int_res(entry.get)
    """
    Показывает прочность бетона при ударе вниз
    # :param number: значение удара
    # :type number: int
    :return: возвращает прочность бетона
    """
    if 20 <= res <= 45:
        return 'Прочность бетона: {res} Мпа'.format(res=KICK_DOWN[res])
    elif res < 20:
        return 'Прочность бетона меньше 14.9 Мпа'
    elif res > 45:
        return 'Прочность бетона больше 59.5 Мпа'


def kick_side() -> str:
    res = int_res(entry.get)
    """
    Показывает прочность бетона при ударе вбок
    # :param number: значение удара
    # :type number: int
    :return: возвращает прочность бетона
    """
    if 20 <= res <= 48:
        return 'Прочность бетона: {res} Мпа'.format(res=KICK_SIDE[res])
    elif res < 20:
        return 'Прочность бетона меньше 10.3 Мпа'
    elif res > 45:
        return 'Прочность бетона больше 60 Мпа'


root = Tk()
root.title("METANIT.COM")
root.geometry("300x400")

position = {"padx": 20, "pady": 6, "anchor": NW}

up = "Вверх"
down = "Вниз"
side = "Вбок"
# res = 'Результат'
kick = StringVar(value='Направление удара')
kick_data = StringVar(value='Введите значения через пробел')

header_data = ttk.Label(textvariable=kick_data)
header_data.pack(**position)

entry = ttk.Entry(width=150)
entry.pack(**position)

result_str = '22 33 44'

header_btn = ttk.Label(textvariable=kick)
header_btn.pack(**position)

up_btn = ttk.Button(text=up, command=kick_up)
up_btn.pack(**position)

down_btn = ttk.Button(text=down, command=kick_down)
down_btn.pack(**position)

side_btn = ttk.Button(text=side, command=kick_side)
side_btn.pack(**position)

# header_res = ttk.Label()
# header_res.pack(**position)

root.mainloop()