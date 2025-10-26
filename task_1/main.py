import json

list = "C:/L/books.json"
with open(list, 'r', encoding='utf-8') as file:
    books = json.load(file)

for i in range(len(books)):
    print(" ---------------------- Книга", i + 1, "-----------------------")
    print(" Название:", books[i]["title"] + ",", "Автор:", books[i]["author"] + ",")
    print(" -------------------------" + str(books[i]["year"]) + "-------------------------\n")
