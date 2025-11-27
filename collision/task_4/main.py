def getIntersectionRect(rect1, rect2):
    """
    Возвращает прямоугольник пересечения двух прямоугольников, или None, если пересечения нет.
    """
    if not isCorrectRect(rect1) or not isCorrectRect(rect2):
        raise RectCorrectError("Некорректный прямоугольник")
    x_min = max(rect1[0][0], rect2[0][0])
    y_min = max(rect1[0][1], rect2[0][1])
    x_max = min(rect1[1][0], rect2[1][0])
    y_max = min(rect1[1][1], rect2[1][1])

    if x_max <= x_min or y_max <= y_min:
        return None
    return [(x_min, y_min), (x_max, y_max)]
