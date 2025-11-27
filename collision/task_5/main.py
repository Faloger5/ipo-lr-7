def hasAnyCollision(rects):
    """
    Проверяет, есть ли пересечения хотя бы между двумя прямоугольниками.
    Возвращает True/False.
    """
    n = len(rects)
    for i in range(n):
        for j in range(i+1, n):
            if isCollisionRect(rects[i], rects[j]):
                return True
    return False
