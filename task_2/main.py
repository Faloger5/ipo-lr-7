import json

list = "C:/l/car.json"
with open(list, 'r', encoding='utf-8') as file:
    data = json.load(file)

menu = data["menu"]
cars = data["cars"]
operations = 0

while True:
    print("Меню:")
    for i in menu:
        for key, value in i.items():
            print(key + ": " + value)

    vvod = input("Выберите нужный пункт меню: ")

    if vvod == "1":
        for car in cars:
            print("ID:", car["id"])
            print("Модель:", car["name"])
            print("Производитель:", car["manufacturer"])
            print("Бензин:", "Да" if car["is_petrol"] else "Нет")
            print("Объём бака:", car["tank_volume"], "литров")
            print("-----------------------------------")
        operations += 1

    elif vvod == "2":
        id = input("Введите id записи: ")
        found = False
        for i in range(len(cars)):
            if str(cars[i]["id"]) == id:
                print(f"Запись в позиции {i}:")
                print(cars[i])
                found = True
                break
        if not found:
            print("Запись не найдена")
        operations += 1

    elif vvod == "3":
        new_id = int(input("Введите id: "))
        new_name = input("Введите название модели: ")
        new_manufacturer = input("Введите производителя: ")
        new_is_petrol = input("Бензиновая? (да/нет): ").lower() == "да"
        new_tank_volume = int(input("Введите объём бака: "))
        new_record = {
            "id": new_id,
            "name": new_name,
            "manufacturer": new_manufacturer,
            "is_petrol": new_is_petrol,
            "tank_volume": new_tank_volume
        }
        cars.append(new_record)
        with open(list, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Запись добавлена")
        operations += 1

    elif vvod == "4":
        id = input("Введите id записи для удаления: ")
        for i in range(len(cars)):
            if str(cars[i]["id"]) == id:
                del cars[i]
                print("Запись удалена")
                with open(list, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                break
        else:
            print("Запись не найдена")
        operations += 1

    elif vvod == "5":
        print(f"Завершение программы. Выполнено операций: {operations}")
        break

    else:
        print("Неверный пункт меню. Попробуйте снова.")
