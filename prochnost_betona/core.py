from config_data.PROCHNOST import KICK_UP, KICK_DOWN, KICK_SIDE


def str_in_list(number_str: str) -> list:
    """
    Переводит строку значений в список чисел
    :param number_str: строка значений
    :type number_str: str
    :return: список значений
    """
    try:
        number_str_list = number_str.split()
        number_list = [int(x) for x in number_str_list]
        return number_list
    except ValueError:
        print('Введены некорректные данные.')


def average_list(number_list: list) -> float:
    """
    Подсчитывает срелнее значение
    :param number_list: список значений
    :type number_list: list[int]
    :return: среднее значение
    """
    return round(sum(number_list) / len(number_list), 1)


number_str = input('Введите значение через пробел: ')
number_list = str_in_list(number_str)
average_number = average_list(number_list)


print(average_number)
