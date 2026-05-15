import json

def load_books():
    try:
        with open('books.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def save_books(books):
    with open('books.json', 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

def show_books():
    books = load_books()
    for i, b in enumerate(books):
        print(f"{i}. {b['author']} - {b['title']}")

def delete_book():
    books = load_books()
    show_books()
    try:
        idx = int(input("Индекс для удаления: "))
        books.pop(idx)
        save_books(books)
        print("Удалено")
    except:
        print("Ошибка")

def main():
    while True:
        print("\n1. Добавить 2. Список 3. Средняя 4. Статистика 5. Удалить 6. Выход")
        c = input("> ")
        if c == '5': delete_book()
        elif c == '6': break

if __name__ == "__main__":
    main()