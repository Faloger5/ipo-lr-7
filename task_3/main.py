# Доброва Анна
import json  # Импортируем модуль json для работы с файлами в формате JSON

filename = 'cars.json'  # Имя файла, где хранятся записи
operation_count = 0  # Счётчик выполненных операций (кроме чтения)

# Попытка открыть файл и загрузить из него данные
try:
    with open(filename, 'r') as f:  # Открываем файл для чтения
        data = json.load(f)  # Загружаем содержимое файла (список словарей)
except FileNotFoundError:
    # Если файла не существует, создаём начальные данные
    data = [
        {"id": 1, "name": "Model S", "manufacturer": "Tesla", "is_petrol": False, "tank_volume": 85},
        {"id": 2, "name": "Golf", "manufacturer": "Volkswagen", "is_petrol": True, "tank_volume": 50},
        {"id": 3, "name": "Civic", "manufacturer": "Honda", "is_petrol": True, "tank_volume": 47},
        {"id": 4, "name": "Mustang", "manufacturer": "Ford", "is_petrol": True, "tank_volume": 61},
        {"id": 5, "name": "Model 3", "manufacturer": "Tesla", "is_petrol": False, "tank_volume": 54}
    ]
    # Записываем эти начальные данные в файл, чтобы он существовал для следующих запусков
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)  # Запись с отступами для читаемости

# Основной цикл программы — бесконечное меню
while True:
    print("\nМеню:")  # Выводим меню для пользователя
    print("1. Вывести все записи")  # Пункт 1
    print("2. Вывести запись по полю")  # Пункт 2
    print("3. Добавить запись")  # Пункт 3
    print("4. Удалить запись по полю")  # Пункт 4
    print("5. Выйти из программы")  # Пункт 5
    choice = input("Введите номер пункта: ")  # Ввод выбора пользователя

    if choice == '1':  # Если выбрано '1'
        # Вывод всех записей
        print("\nВсе записи:")
        try:
            with open(filename, 'r') as f:  # Открываем файл для чтения
                data = json.load(f)  # Загружаем актуальные данные
            # Проходим по каждой записи в списке
            for record in data:
                # Выводим каждую запись в формате с отступами
                print(json.dumps(record, indent=4))
        except:
            # Обработка ошибок при чтении файла
            print("Ошибка при чтении файла.")

    elif choice == '2':  # Если выбрано '2'
        # Вывод записи по id
        search_id_input = input("Введите id записи: ")  # Запрашиваем id для поиска
        if not search_id_input.isdigit():  # Проверка, что ввод — число
            print("Некорректный ввод.")  # Сообщение об ошибке
            continue  # Возврат к началу меню
        search_id = int(search_id_input)  # Преобразование строки в число
        found = False  # Флаг, найден ли запись
        position = -1  # Позиция записи (не используется, можно убрать)
        try:
            with open(filename, 'r') as f:
                data = json.load(f)  # Загружаем текущие данные
            for idx, record in enumerate(data):  # Перебираем записи с индексами
                if record.get('id') == search_id:  # Если id совпало
                    print(f"Запись найдена на позиции {idx}:")  # Сообщение
                    print(json.dumps(record, indent=4))  # Вывод записи
                    found = True  # Устанавливаем флаг найдено
                    break  # Выходим из цикла
            if not found:  # Если не нашли
                print("Запись с таким id не найдена.")  # Предупреждение
        except:
            print("Ошибка при чтении файла.")  # Обработка ошибок

    elif choice == '3':  # Если выбрано '3' — добавление
        try:
            with open(filename, 'r') as f:  # Читаем текущие данные
                data = json.load(f)
        except:
            data = []  # Если файла нет или ошибка, создаём пустой список

        # Находим максимальный id среди существующих
        max_id = max([record['id'] for record in data], default=0)
        new_id = max_id + 1  # Новый id — на единицу больше максимального

        # Запрашиваем у пользователя поля новой записи
        name = input("Введите название модели: ")
        manufacturer = input("Введите производителя: ")

        # Запрос о типе топлива
        is_petrol_input = input("Заправляется ли машина бензином? (да/нет): ").lower()
        is_petrol = True if is_petrol_input == 'да' else False  # Булево значение

        tank_volume_input = input("Введите объем бака (литры): ")
        if not tank_volume_input.isdigit():  # Проверка, что введено число
            print("Некорректный объем бака.")
            continue  # Переходим к следующему циклу
        tank_volume = int(tank_volume_input)

        # Создаём новую запись как словарь
        new_record = {
            "id": new_id,  # Новый уникальный id
            "name": name,
            "manufacturer": manufacturer,
            "is_petrol": is_petrol,
            "tank_volume": tank_volume
        }
        # Добавляем новую запись в список
        data.append(new_record)
        # Записываем обновлённые данные обратно в файл
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print("Запись добавлена.")  # Уведомление
        operation_count += 1  # Увеличиваем счетчик операций

    elif choice == '4':  # Если выбрано '4' — удаление
        search_id_input = input("Введите id записи для удаления: ")
        if not search_id_input.isdigit():
            print("Некорректный ввод.")
            continue
        search_id = int(search_id_input)
        try:
            with open(filename, 'r') as f:  # Читаем текущие данные
                data = json.load(f)
            found_index = -1  # Изначально не нашли
            for idx, record in enumerate(data):  # Перебираем с индексами
                if record.get('id') == search_id:  # Если нашли искомый id
                    found_index = idx  # Запоминаем позицию
                    break
            if found_index == -1:  # Если не нашли
                print("Запись с таким id не найдена.")
            else:
                # Удаляем запись из списка
                del data[found_index]
                # Записываем обновлённые данные
                with open(filename, 'w') as f:
                    json.dump(data, f, indent=4)
                print("Запись удалена.")  # Уведомление
                operation_count +=1  # Увеличиваем счетчик
        except:
            print("Ошибка при чтении файла.")

    elif choice == '5':  # Выйти из программы
        # Перед завершением выводим количество выполненных операций
        print(f"Количество выполненных операций: {operation_count}")
        break  # Выходим из бесконечного цикла → завершение программы

    else:  # Если введено что-то другое
        print("Некорректный выбор. Повторите попытку.")  # Сообщение об ошибке
