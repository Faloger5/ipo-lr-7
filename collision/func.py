# collision/collision.py

# Определяем исключение для некорректных прямоугольников
class RectCorrectError(Exception):
    pass

def isCorrectRect(rect):
    """
    Проверяет корректность определения прямоугольника.
    rect: список из двух кортежей: [ (x1, y1), (x2, y2) ]
    Возвращает True, если левый нижний угол действительно меньше верхнего правого.
    """
    if not isinstance(rect, list) or len(rect) != 2:
        return False
    lower_left, upper_right = rect
    if not (isinstance(lower_left, tuple) and isinstance(upper_right, tuple)):
        return False
    if len(lower_left) != 2 or len(upper_right) != 2:
        return False
    
    x1, y1 = lower_left
    x2, y2 = upper_right
    return x1 < x2 and y1 < y2

def isCollisionRect(rect1, rect2):
    """
    Проверяет, пересекаются ли два прямоугольника.
    Возвращает True или False.
    """
    # Проверка корректности прямоугольников
    if not isCorrectRect(rect1):
        raise RectCorrectError("1й прямоугольник некорректный")
    if not isCorrectRect(rect2):
        raise RectCorrectError("2й прямоугольник некорректный")
    
    (x1_min, y1_min), (x1_max, y1_max) = rect1
    (x2_min, y2_min), (x2_max, y2_max) = rect2

    # Проверка пересечения по горизонтали и вертикали
    if x1_max < x2_min or x2_max < x1_min:
        return False
    if y1_max < y2_min or y2_max < y1_min:
        return False
    return True

def intersectionAreaRect(rect1, rect2):
    """
    Вычисляет площадь пересечения двух прямоугольников.
    Если пересечения нет – возвращает 0.
    """
    # Проверка корректности
    if not isCorrectRect(rect1):
        raise ValueError("Некорректный первый прямоугольник")
    if not isCorrectRect(rect2):
        raise ValueError("Некорректный второй прямоугольник")
    (x1_min, y1_min), (x1_max, y1_max) = rect1
    (x2_min, y2_min), (x2_max, y2_max) = rect2

    # Вычисляем границы пересечения
    x_overlap = max(0, min(x1_max, x2_max) - max(x1_min, x2_min))
    y_overlap = max(0, min(y1_max, y2_max) - max(y1_min, y2_min))

    return x_overlap * y_overlap

def intersectionAreaMultiRect(rects):
    """
    Вычисляет объединённую площадь пересечения всех прямоугольников.
    """
    # Проверка корректности каждого прямоугольника
    for idx, rect in enumerate(rects):
        if not isCorrectRect(rect):
            raise RectCorrectError(f"Некорректный прямоугольник по индексу {idx}")

    # Начинаем с первого прямоугольника
    overlap_x_min, overlap_y_min = rects[0][0]
    overlap_x_max, overlap_y_max = rects[0][1]
    
    for rect in rects[1:]:
        (x_min, y_min), (x_max, y_max) = rect
        # Находим пересечение по горизонтали
        overlap_x_min = max(overlap_x_min, x_min)
        overlap_x_max = min(overlap_x_max, x_max)
        # Находим пересечение по вертикали
        overlap_y_min = max(overlap_y_min, y_min)
        overlap_y_max = min(overlap_y_max, y_max)
        # Если пересечение не существует, возвращаем 0
        if overlap_x_max <= overlap_x_min or overlap_y_max <= overlap_y_min:
            return 0

    return (overlap_x_max - overlap_x_min) * (overlap_y_max - overlap_y_min)
