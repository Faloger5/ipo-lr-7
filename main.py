from collision import isCorrectRect, isCollisionRect, RectCorrectError

def get_rectangle(prompt):
    while True:
        try:
            print(prompt)
            x1 = float(input("  Координата X левого нижнего угла: "))
            y1 = float(input("  Координата Y левого нижнего угла: "))
            x2 = float(input("  Координата X правого верхнего угла: "))
            y2 = float(input("  Координата Y правого верхнего угла: "))
            rect = [(x1, y1), (x2, y2)]
            if isCorrectRect(rect):
                print(f"Вы ввели корректный прямоугольник: {rect}")
                return rect
            else:
                print("Некорректные координаты. Верхний правый угол должен быть правее и выше нижнего.")
        except ValueError:
            print("Некорректный ввод числа. Попробуйте еще раз.")

def main():
    rect1 = get_rectangle("Введите координаты первого прямоугольника")
    rect2 = get_rectangle("Введите координаты второго прямоугольника")
    print("\nПроверка пересечения прямоугольников...")
    try:
        result = isCollisionRect(rect1, rect2)
        if result:
            print("Прямоугольники пересекаются.")
        else:
            print("Прямоугольники не пересекаются.")
    except RectCorrectError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
