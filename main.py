from collision.rect_utils import (
    isCorrectRect, isCollisionRect,
    intersectionAreaRect, intersectionAreaMultiRect
)
from collision.errors import RectCorrectError

def main():
    print("Программа для работы с прямоугольниками")

    rect1 = [tuple(map(float, input("Введите координаты левого нижнего угла первого прямоугольника (x y): ").split())),
             tuple(map(float, input("Введите координаты правого верхнего угла первого прямоугольника (x y): ").split()))]

    rect2 = [tuple(map(float, input("Введите координаты левого нижнего угла второго прямоугольника (x y): ").split())),
             tuple(map(float, input("Введите координаты правого верхнего угла второго прямоугольника (x y): ").split()))]

    print(f"Корректность первого прямоугольника: {isCorrectRect(rect1)}")
    print(f"Корректность второго прямоугольника: {isCorrectRect(rect2)}")

    try:
        print(f"Пересекаются ли прямоугольники: {isCollisionRect(rect1, rect2)}")
        print(f"Площадь пересечения: {intersectionAreaRect(rect1, rect2)}")
    except RectCorrectError as e:
        print(f"Ошибка: {e}")
    except ValueError as e:
        print(f"Ошибка: {e}")

    rectangles = [rect1, rect2]
    try:
        print(f"Уникальная площадь пересечения всех прямоугольников: {intersectionAreaMultiRect(rectangles)}")
    except RectCorrectError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
