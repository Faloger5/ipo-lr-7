from .errors import RectCorrectError  # Импортирование исключения RectCorrectError из модуля errors

def isCorrectRect(rect):
    if len(rect) != 2:  # Проверка, что список содержит ровно два элемента
        return False
    (x1, y1), (x2, y2) = rect  # Распаковка координат точек прямоугольника
    return x1 < x2 and y1 < y2  # Проверка, что первая точка левее и ниже второй

