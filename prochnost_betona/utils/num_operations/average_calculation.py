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
    Подсчитывает среднее значение
    :param number_list: список значений
    :type number_list: list[int]
    :return: среднее значение
    """
    return int(round(sum(number_list) / len(number_list)))