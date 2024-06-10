import json
import os
from datetime import datetime

NOTES_FILE = 'notes.json'

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as file:
            return json.load(file)
    return []

def save_notes(notes):
    with open(NOTES_FILE, 'w') as file:
        json.dump(notes, file, indent=4)

def create_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    note_id = len(load_notes()) + 1
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": note_id,
        "title": title,
        "body": body,
        "created_at": created_at,
        "updated_at": created_at
    }
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    print("Заметка создана.")

def list_notes():
    notes = load_notes()
    if not notes:
        print("Нет заметок.")
    else:
        for note in notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата создания: {note['created_at']}, Дата обновления: {note['updated_at']}")

def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            note['title'] = input("Введите новый заголовок заметки: ")
            note['body'] = input("Введите новое тело заметки: ")
            note['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка обновлена.")
            return
    print("Заметка не найдена.")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    notes = load_notes()
    notes = [note for note in notes if note['id'] != note_id]
    save_notes(notes)
    print("Заметка удалена.")

def main():
    while True:
        print("\n1. Создать заметку")
        print("2. Просмотреть все заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            create_note()
        elif choice == '2':
            list_notes()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
