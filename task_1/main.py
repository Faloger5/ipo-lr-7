import json  #импортируем json

list = "S:/students/GR_88/Доброва Анна/ИПО/ipo-1r-7/task_1/books.json"  #определяем где находится файл

with open(list, 'r', encoding='utf-8') as file:  #открываем файл для чтения
    books = json.load(file)  #чтение данных

for i in range(len(books)):  #цикл, повторяемый стол только, гов в файле json
    print("Книга", i + 1, "-")  #заголовок
    print("Название: ", books[i]["title"] + ",", "Автор:", books[i]["author"] + ",")  #названиет
    print(str(books[i]["year"]) + " - -------------\n")  #год
