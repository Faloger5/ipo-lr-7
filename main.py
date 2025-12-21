print("start code …")

# Импортируем всё из пакета (название пакета укажи своё, например rectpack или просто rectpkg)
from rectpkg import isCorrectRect, isCollisionRect, intersectionAreaRect, intersectionAreaMultiRect, RectCorrectError

#Примеры использования:

# 1. Проверка корректности прямоугольника
rect1 = [(0, 0), (5, 5)]
rect2 = [(3, 3), (7, 7)]
rect_invalid = [(5, 5), (2, 2)]

print("Прямоугольник rect1 корректный?", isCorrectRect(rect1))  # True
print("Прямоугольник rect_invalid корректный?", isCorrectRect(rect_invalid))  # False

# 2. Проверка пересечения двух прямоугольников
try:
    print("rect1 и rect2 пересекаются?", isCollisionRect(rect1, rect2))  # True
except RectCorrectError as e:
    print("Ошибка:", e)

# 3. Площадь пересечения двух прямоугольников
try:
    area = intersectionAreaRect(rect1, rect2)
    print("Площадь пересечения rect1 и rect2 =", area)  # 4
except ValueError as e:
    print("Ошибка:", e)

# 4. Площадь пересечения нескольких прямоугольников
rect3 = [(4, 4), (6, 6)]
rectangles = [rect1, rect2, rect3]
try:
    multi_area = intersectionAreaMultiRect(rectangles)
    print("Площадь пересечения rect1, rect2 и rect3 =", multi_area)  # 1
except RectCorrectError as e:
    print("Ошибка:", e)

print("end code …")
