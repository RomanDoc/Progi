from prochnost_betona.utils.CRUD import kick_up, kick_down, kick_side


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
    return int(round(sum(number_list) / len(number_list)))


def prochnost(target: int, kick: str) -> None:
    if kick == 'вверх':
        print(kick_up(target))
    elif kick == 'вниз':
        print(kick_down(target))
    elif kick == 'вбок':
        print(kick_side(target))
    else:
        print('Ошибка в данных')


kick = input('Введит направление удара (вверх, вниз или вбок): ').lower()
number_str = input('Введите значение через пробел: ')
number_list = str_in_list(number_str)
average_number = int(average_list(number_list))
prochnost(average_number, kick)


# print(type(average_number))
