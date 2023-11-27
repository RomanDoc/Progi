from prochnost_betona.config_data.PROCHNOST import KICK_UP, KICK_DOWN, KICK_SIDE


def kick_up(number: int) -> str:
    """
    Показывает прочность бетона при ударе вверх
    :param number: значение удара
    :type number: int
    :return: возвращает прочность бетона
    """
    if 20 <= number <= 50:
        return 'Прочность бетона: {res} Мпа'.format(res=KICK_UP[number])
    elif number < 20:
        return 'Прочность бетона меньше 10.3 Мпа'
    elif number > 50:
        return 'Прочность бетона больше 56.8 Мпа'


def kick_down(number: int) -> str:
    """
    Показывает прочность бетона при ударе вниз
    :param number: значение удара
    :type number: int
    :return: возвращает прочность бетона
    """
    if 20 <= number <= 45:
        return 'Прочность бетона: {res} Мпа'.format(res=KICK_DOWN[number])
    elif number < 20:
        return 'Прочность бетона меньше 14.9 Мпа'
    elif number > 45:
        return 'Прочность бетона больше 59.5 Мпа'


def kick_side(number: int) -> str:
    """
    Показывает прочность бетона при ударе вбок
    :param number: значение удара
    :type number: int
    :return: возвращает прочность бетона
    """
    if 20 <= number <= 48:
        return 'Прочность бетона: {res} Мпа'.format(res=KICK_SIDE[number])
    elif number < 20:
        return 'Прочность бетона меньше 10.3 Мпа'
    elif number > 45:
        return 'Прочность бетона больше 60 Мпа'