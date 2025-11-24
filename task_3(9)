import json  # Импортируем модуль json для работы с файлом в формате JSON

filename = 'cars.json'  # Имя файла, где будут храниться записи
operation_count = 0  # Счётчик выполненных операций

def load_data():
    """Функция для загрузки данных из файла"""
    try:
        with open(filename, 'r') as f:  # Открываем файл для чтения
            return json.load(f)  # Загружаем данные из файла в формате JSON
    except:
        return []  # Если файл не найден или произошла ошибка, возвращаем пустой список

def save_data(data):
    """Функция для сохранения данных в файл"""
    with open(filename, 'w') as f:  # Открываем файл для записи (перезапись)
        json.dump(data, f, indent=4)  # Записываем данные в формате JSON с красивым форматированием

def show_all_records():
    """Функция для отображения всех записей"""
    data = load_data()  # Загружаем текущие данные
    if not data:  # Если список пуст
        print("Нет записей.")  # Выводим сообщение, что записей нет
    else:
        for record in data:  # Проходим по всем записям
            print(json.dumps(record, indent=4))  # Выводим каждую запись как красиво отформатированный JSON

def find_record_by_id(search_id):
    """Функция для поиска записи по id"""
    data = load_data()  # Загружаем текущие данные
    for idx, record in enumerate(data):  # Перебираем список с индексами
        if record.get('id') == search_id:  # Если id совпадает с искомым
            return record, idx  # Возвращаем найденную запись и её индекс
    return None, -1  # Если не нашли, возвращаем None и -1

def add_record():
    """Функция для добавления новой записи"""
    global operation_count  # Объявляем, что будем изменять глобальную переменную счётчика
    data = load_data()  # Загружаем текущие данные

    max_id = max([record['id'] for record in data], default=0)  # Находим максимальный id в текущих данных
    new_id = max_id + 1  # Устанавливаем новый id как максимум + 1

    name = input("Введите название модели: ").strip()  # Запрос имени модели, удаляя лишние пробелы
    manufacturer = input("Введите производителя: ").strip()  # Запрос производителя

    while True:  # Бесконечный цикл для получения корректного ответа
        is_petrol_input = input("Заправляется ли машина бензином? (да/нет): ").lower()  # Ввод с преобразованием в маленькие буквы
        if is_petrol_input in ('да', 'нет'):  # Проверка корректности ответа
            is_petrol = True if is_petrol_input == 'да' else False  # Установка булева значения
            break  # Выход из цикла при корректном ответ
        else:
            print("Пожалуйста, введите 'да' или 'нет'.")  # Если ответ некорректен, просим повторить

    while True:  # Аналогичный цикл для проверки объема бака
        tank_volume_input = input("Введите объем бака (литры): ").strip()
        if tank_volume_input.isdigit():  # Проверка, что введено число
            tank_volume = int(tank_volume_input)  # Преобразование в целое число
            break  # Выход из цикла
        else:
            print("Некорректный объем бака. Введите число.")  # При ошибке просим повторить

    # Создаём новую запись в виде словаря
    new_record = {
        "id": new_id,  # Уникальный идентификатор
        "name": name,  # Название модели
        "manufacturer": manufacturer,  # Производитель
        "is_petrol": is_petrol,  # Заправляется бензином?
        "tank_volume": tank_volume  # Объем бака
    }
    data.append(new_record)  # Добавляем новую запись в список
    save_data(data)  # Сохраняем обновлённые данные в файл
    print("Запись добавлена.")  # Информируем пользователя
    operation_count += 1  # Увеличиваем счётчик операций

def delete_record():
    """Функция для удаления записи по id"""
    global operation_count  # Объявляем глобальную переменную
    try:
        search_id_input = input("Введите id записи для удаления: ").strip()  # Запрашиваем id для удаления
        if not search_id_input.isdigit():  # Проверка, что ввели число
            print("Некорректный ввод.")  # Если нет, сообщаем
            return  # Выход из функции
        search_id = int(search_id_input)  # Преобразуем ввод в число
        data = load_data()  # Загружаем текущие данные
        for idx, record in enumerate(data):  # Перебираем записи с индексами
            if record.get('id') == search_id:  # Если id совпадает
                del data[idx]  # Удаляем эту запись
                save_data(data)  # Сохраняем изменения
                print("Запись удалена.")  # Сообщаем пользователю
                operation_count += 1  # Увеличиваем счётчик операций
                return  # Выходим из функции
        print("Запись с таким id не найдена.")  # Если не нашли, уведомляем
    except:
        print("Ошибка при чтении файла.")  # При исключении сообщаем об ошибке

def main_menu():
    """Главное меню программы, запускает цикл взаимодействия"""
    global operation_count  # Объявление глобальной переменной
    while True:  # Бесконечный цикл
        # Вывод вариантов меню
        print("\nМеню:")
        print("1. Вывести все записи")
        print("2. Вывести запись по полю")
        print("3. Добавить запись")
        print("4. Удалить запись по полю")
        print("5. Выйти из программы")
        choice = input("Введите номер пункта: ").strip()  # Ввод выбора пользователя

        if choice == '1':  # Если выбран пункт 1
            show_all_records()  # Вызываем функцию отображения всех записей

        elif choice == '2':  # Пункт 2 — вывести запись по id
            try:
                search_id_input = input("Введите id записи: ").strip()  # Запрашиваем id
                if not search_id_input.isdigit():
                    print("Некорректный ввод.")  # Проверка и сообщение
                    continue
                search_id = int(search_id_input)  # Преобразование в число
                record, _ = find_record_by_id(search_id)  # Поиск записи по id
                if record:
                    print(json.dumps(record, indent=4))  # Вывод записи
                else:
                    print("Запись с таким id не найдена.")  # Если не нашли
            except:
                print("Ошибка при чтении файла.")  # Обработка ошибок

        elif choice == '3':  # Пункт 3 — добавление записи
            add_record()  # Вызов функции добавления

        elif choice == '4':  # Пункт 4 — удаление записи
            delete_record()  # Вызов функции удаления

        elif choice == '5':  # Выход из программы
            print(f"Количество выполненных операций: {operation_count}")  # Вывод счётчика
            break  # Выход из цикла и завершение программы

        else:  # Если введена некорректная опция
            print("Некорректный выбор. Повторите попытку.")  # Сообщение пользователю
