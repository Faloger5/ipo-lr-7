import json  # импорт библиотеки для работы с JSON

file_path = "S:/students/GR_88/Доброва Анна/ИПО/ipo-lr-7/task_2/college.json"  # путь к файлу

with open(file_path, 'r', encoding='utf-8') as file:  # открыть файл для чтения с правильной кодировкой
    data = json.load(file)  # загрузить содержимое файла в переменную data
qualification_number = input("Введите номер квалификации: ").strip()  # запросить у пользователя номер и убрать лишние пробелы
result = None  # инициализация переменной для хранения найденного объекта
for item in data:  # пройти по всем элементам в списке
    if item.get('model') == 'data.specialty':  # проверить, что модель равна 'data.specialty'
            result = item  # сохранить найденный элемент в переменную result
            break  # выйти из цикла после нахождения
if result:  # если найдена
    title = result.get('fields', {}).get('title')  # получить название или указать по умолчанию
    c_type = result.get('fields', {}).get('c_type', 'Нет типа')  # получить c_type или указать по умолчанию
    print("=============== Найдено ===============")  # вывести строку для обозначения результата
    print(f"{qualification_number} >> Специальность \"{title}\", {c_type}")  # вывести номер и название специальности
else:  # если ничего не найдено
    print("=============== Не найдено ===============")  # вывести строку
