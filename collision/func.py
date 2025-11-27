class RectCorrectError(Exception):
    """Исключение для некорректных прямоугольников"""
    pass

def isCorrectRect(coords):
    """
    Проверяет корректность прямоугольника.
    Args:
        coords (list): список из двух кортежей [(x1, y1), (x2, y2)]
    Возвращает:
        bool: True если координаты корректны, False иначе
    """
    if not isinstance(coords, list) or len(coords) != 2:
        return False

    bottom_left, top_right = coords

    # Проверка типов
    if not (isinstance(bottom_left, tuple) and isinstance(top_right, tuple)):
        return False
    if not (len(bottom_left) == 2 and len(top_right) == 2):
        return False
    if not (all(isinstance(coord, (int, float)) for coord in bottom_left + top_right)):
        return False

    x1, y1 = bottom_left
    x2, y2 = top_right

    # Проверка, что верхний правый угол правее и выше нижнего
    return x2 > x1 and y2 > y1

def isCollisionRect(rect1, rect2):
    """
    Проверяет, пересекаются ли два прямоугольника.
    Args:
        rect1, rect2 (list): списки из двух кортежей
    Возвращает:
        bool: True если пересекаются, False иначе
    Исключение:
        RectCorrectError — если один из прямоугольников некорректен
    """
    if not isCorrectRect(rect1):
        raise RectCorrectError("1й прямоугольник некоректный")
    if not isCorrectRect(rect2):
        raise RectCorrectError("2й прямоугольник некоректный")

    (x1_min, y1_min), (x1_max, y1_max) = rect1
    (x2_min, y2_min), (x2_max, y2_max) = rect2

    # Проверка пересечения
    if x1_max < x2_min or x2_max < x1_min:
        return False
    if y1_max < y2_min or y2_max < y1_min:
        return False
    return True
