from tkinter import *
from tkinter import ttk

from prochnost_betona.config_data.program_data import KICK_UP, KICK_DOWN, KICK_SIDE, direction_kick
from prochnost_betona.utils.num_operations.average_calculation import int_res


def kick_up(res) -> None:
    """
    Показывает прочность бетона при ударе вверх
    # :param number: значение удара
    # :type number: int
    """
    if 20 <= res <= 50:
        header_res.config(text='Прочность бетона: {res} Мпа'.format(res=KICK_UP[res]))
    elif res < 20:
        header_res.config(text='Прочность бетона меньше 10.3 Мпа')
    elif res > 50:
        header_res.config(text='Прочность бетона больше 56.8 Мпа')


def kick_down(res) -> None:
    """
    Показывает прочность бетона при ударе вниз
    # :param number: значение удара
    # :type number: int
    """
    if 20 <= res <= 45:
        header_res.config(text='Прочность бетона: {res} Мпа'.format(res=KICK_DOWN[res]))
    elif res < 20:
        header_res.config(text='Прочность бетона меньше 14.9 Мпа')
    elif res > 45:
        header_res.config(text='Прочность бетона больше 59.5 Мпа')


def kick_side(res) -> None:
    """
    Показывает прочность бетона при ударе вбок
    # :param number: значение удара
    # :type number: int
    """
    if 20 <= res <= 48:
        header_res.config(text='Прочность бетона: {res} Мпа'.format(res=KICK_SIDE[res]))
    elif res < 20:
        header_res.config(text='Прочность бетона меньше 10.3 Мпа')
    elif res > 45:
        header_res.config(text='Прочность бетона больше 60 Мпа')


root = Tk()
root.title("Beton Pro CONDTROL")
root.geometry("300x400")

position = {"padx": 20, "pady": 6, "anchor": NW}

kick = StringVar(value='Направление удара')
kick_data = StringVar(value='Введите значения через пробел')

header_data = ttk.Label(textvariable=kick_data)
header_data.pack(**position)

entry = ttk.Entry(width=150)
entry.pack(**position)

header_btn = ttk.Label(textvariable=kick)
header_btn.pack(**position)

up_btn = ttk.Button(text=direction_kick[0], command=lambda: kick_up(int_res(entry.get())))
up_btn.pack(**position)

down_btn = ttk.Button(text=direction_kick[1], command=lambda: kick_down(int_res(entry.get())))
down_btn.pack(**position)

side_btn = ttk.Button(text=direction_kick[2], command=lambda: kick_side(int_res(entry.get())))
side_btn.pack(**position)

header_res = ttk.Label()
header_res.pack(**position)

root.mainloop()