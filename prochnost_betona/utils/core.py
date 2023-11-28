from prochnost_betona.utils.line_kick.kick import kick_up, kick_down, kick_side
from prochnost_betona.utils.num_operations.average_calculation import str_in_list, average_list


def prochnost(target: int, kick: str) -> None:
    """
    Логика работы программы
    :param target: показатель прибора (среднее)
    :type target: int
    :param kick: Направление удара
    :type kick: str
    """
    if kick == 'вверх':
        print(kick_up(target))
    elif kick == 'вниз':
        print(kick_down(target))
    elif kick == 'вбок':
        print(kick_side(target))
    else:
        print('Ошибка в данных')


def interface():
    ansver = 'да'
    while ansver == 'да':
        kick = input('Введит направление удара (вверх, вниз или вбок): ').lower()
        number_str = input('Введите значение через пробел: ')
        number_list = str_in_list(number_str)
        average_number = int(average_list(number_list))
        prochnost(average_number, kick)
        ansver = input('Хотите ввести еще значение (да/нет): ').lower()