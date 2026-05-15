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
    author, title = input("Автор: "), input("Название: ")
    if any(b['author'] == author and b['title'] == title for b in books):
        print("Ошибка: дубликат"); return
    try:
        rating = int(input("Оценка (1-5): "))
        if not (1 <= rating <= 5): raise ValueError
    except: print("Ошибка: число 1-5"); return
    books.append({"author": author, "title": title, "rating": rating, "date": input("Дата: ")})
    save_books(books); print("Добавлено")

def show_books():
    books = load_books()
    for i, b in enumerate(books):
        print(f"{i}. {b['author']} - {b['title']} ({b['rating']})")

def show_stats():
    books = load_books()
    if not books: return
    print(f"Средняя оценка: {sum(b['rating'] for b in books)/len(books):.2f}")
    authors = {}
    for b in books: authors[b['author']] = authors.get(b['author'], 0) + 1
    for a, c in authors.items(): print(f"{a}: {c} книг")

def main():
    while True:
        print("\n1. Добавить 2. Список 3. Средняя 4. Статистика 5. Удалить 6. Выход")
        c = input("> ")
        if c == '1': add_book()
        elif c == '2': show_books()
        elif c in ('3', '4'): show_stats()
        elif c == '6': break

if __name__ == "__main__":
    main()