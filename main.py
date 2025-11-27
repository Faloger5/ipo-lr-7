# main.py

from collision.collision import (
    isCorrectRect, 
    isCollisionRect, 
    intersectionAreaRect, 
    intersectionAreaMultiRect,
    RectCorrectError
)

def main():
    # Примеры использования
    print("=== Примеры функций collision ===")
    # isCorrectRect
    rect1 = [(-3.4, 1), (9.2, 10)]
    rect2 = [(-7, 9), (3, 6)]
    print(f"isCorrectRect({rect1}) -> {isCorrectRect(rect1)}")
    print(f"isCorrectRect({rect2}) -> {isCorrectRect(rect2)}")  # False

    # isCollisionRect
    rect3 = [(-3.4, 1), (9.2, 10)]
    rect4 = [(-7.4, 0), (13.2, 12)]
    try:
        print(f"isCollisionRect({rect3}, {rect4}) -> {isCollisionRect(rect3, rect4)}")
    except RectCorrectError as e:
        print(f"Ошибка: {e}")

    rect5 = [(1, 1), (2, 2)]
    rect6 = [(3, 0), (13, 1)]
    try:
        print(f"isCollisionRect({rect5}, {rect6}) -> {isCollisionRect(rect5, rect6)}")
    except RectCorrectError as e:
        print(f"Ошибка: {e}")

    # intersectionAreaRect
    rect7 = [(-3, 1), (9, 10)]
    rect8 = [(-7, 0), (13, 12)]
    print(f"Площадь пересечения: {intersectionAreaRect(rect7, rect8)}")
    rect9 = [(1, 1), (2, 2)]
    rect10 = [(3, 0), (13, 1)]
    print(f"Площадь пересечения: {intersectionAreaRect(rect9, rect10)}")  # 0

    # intersectionAreaMultiRect
    rectangles = [
        [(-3, 1), (9, 10)],
        [(-7, 0), (13, 12)],
        [(0, 0), (5, 5)],
        [(2, 2), (7, 7)]
    ]
    print("Общая площадь пересечения всех прямоугольников:")
    print(intersectionAreaMultiRect(rectangles))
    # Некорректный случай
    incorrect_rects = [
        [(-3, 1), (9, 10)],
        [(3, 17), (13, 1)]  # некорректный
    ]
    try:
        intersectionAreaMultiRect(incorrect_rects)
    except RectCorrectError as e:
        print(f"Обнаружена ошибка: {e}")

if __name__ == "__main__":
    main()
