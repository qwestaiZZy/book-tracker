import json

def load_books():
    try:
        with open('books.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_books(books):
    with open('books.json', 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

def add_book():
    books = load_books()
    author = input("Автор: ")
    title = input("Название: ")
    
    for book in books:
        if book['author'] == author and book['title'] == title:
            print("Ошибка: дубликат")
            return

    try:
        rating = int(input("Оценка (1-5): "))
        if not (1 <= rating <= 5): raise ValueError
    except ValueError:
        print("Ошибка: число от 1 до 5")
        return

    date = input("Дата: ")
    books.append({"author": author, "title": title, "rating": rating, "date": date})
    save_books(books)
    print("Добавлено")

def main():
    while True:
        print("\n1. Добавить\n2. Список\n3. Средняя оценка\n4. Статистика\n5. Удалить\n6. Выход")
        choice = input("> ")
        if choice == '1': add_book()
        elif choice == '6': break

if __name__ == "__main__":
    main()