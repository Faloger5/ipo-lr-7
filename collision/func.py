from .errors import RectCorrectError

def isCorrectRect(rect):
    """
    Проверяет корректность прямоугольника.
    rect: список из двух кортежей [(x1, y1), (x2, y2)]
    """
    if len(rect) != 2:
        return False
    (x1, y1), (x2, y2) = rect
    return x1 < x2 and y1 < y2


def isCollisionRect(rect1, rect2):
    """
    Проверяет пересечение двух прямоугольников.
    """
    if not isCorrectRect(rect1):
        raise RectCorrectError("1й прямоугольник некоректный")
    if not isCorrectRect(rect2):
        raise RectCorrectError("2й прямоугольник некоректный")

    (x1, y1), (x2, y2) = rect1
    (a1, b1), (a2, b2) = rect2

    return not (x2 < a1 or a2 < x1 or y2 < b1 or b2 < y1)


def intersectionAreaRect(rect1, rect2):
    """
    Возвращает площадь пересечения двух прямоугольников.
    """
    if not isCorrectRect(rect1) or not isCorrectRect(rect2):
        raise ValueError("Некорректный прямоугольник")

    if not isCollisionRect(rect1, rect2):
        return 0

    (x1, y1), (x2, y2) = rect1
    (a1, b1), (a2, b2) = rect2

    x_overlap = min(x2, a2) - max(x1, a1)
    y_overlap = min(y2, b2) - max(y1, b1)

    return x_overlap * y_overlap if x_overlap > 0 and y_overlap > 0 else 0


def intersectionAreaMultiRect(rectangles):
    """
    Возвращает уникальную площадь пересечения всех прямоугольников.
    """
    for rect in rectangles:
        if not isCorrectRect(rect):
            raise RectCorrectError("Некорректный прямоугольник")

    # Начинаем с первого прямоугольника
    inter = rectangles[0]
    for rect in rectangles[1:]:
        if not isCollisionRect(inter, rect):
            return 0
        (x1, y1), (x2, y2) = inter
        (a1, b1), (a2, b2) = rect
        inter = [(max(x1, a1), max(y1, b1)), (min(x2, a2), min(y2, b2))]

    return intersectionAreaRect(inter, inter)
