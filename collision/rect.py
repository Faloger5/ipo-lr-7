from .errors import RectCorrectError  # Импортирование исключения RectCorrectError из модуля errors

def isCorrectRect(rect):
    if len(rect) != 2:  # Проверка, что список содержит ровно два элемента
        return False
    (x1, y1), (x2, y2) = rect  # Распаковка координат точек прямоугольника
    return x1 < x2 and y1 < y2  # Проверка, что первая точка левее и ниже второй

def isCollisionRect(rect1, rect2):
    if not isCorrectRect(rect1):  # Проверка корректности первого прямоугольника
        raise RectCorrectError("1й прямоугольник некоректный")
    if not isCorrectRect(rect2):  # Проверка корректности второго прямоугольника
        raise RectCorrectError("2й прямоугольник некоректный")
    (x1, y1), (x2, y2) = rect1  # Распаковка координат первого прямоугольника
    (a1, b1), (a2, b2) = rect2  # Распаковка координат второго прямоугольника
    return not (x2 < a1 or a2 < x1 or y2 < b1 or b2 < y1)  # Проверка пересечения прямоугольников

