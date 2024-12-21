import datetime, json, uuid
import pandas as pd

class Note:
    def __init__(self, id, title, content, timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")):
        self.id = id
        self.title = title
        self.content = content
        self.timestamp = timestamp

    def __dict__(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "timestamp": self.timestamp,
        }

class NotesManagement:
    def __init__(self, notes_file):
        self.notes_file = notes_file

    def load_notes(self):
        try:
            with open(self.notes_file) as f:
                json_loaded =  json.load(f)
                return [Note(**note) for note in json_loaded]
        except FileNotFoundError:
            return []

    def save_notes(self, notes):
        dict_notes = [note.__dict__() for note in notes]
        with open(self.notes_file, 'w') as file:
            json.dump(dict_notes, file)

    def create_note(self):
        notes = self.load_notes()

        title = input("Введите заголовок заметки: ")
        content = input("Введите содержимое заметки: ")
        note_id = str(uuid.uuid4())
        note = Note(note_id, title, content)
        notes.append(note)

        self.save_notes(notes)
        print("Заметка успешно создана.")

    def view_notes(self):
        notes = self.load_notes()

        if notes:
            for note in notes:
                print(f'Название: {note.title}, Дата: {note.timestamp}, ID: {note.id}')
        else:
            print('Нет заметок!')

    def view_content(self, note_id):
        notes = self.load_notes()

        for note in notes:
            if note.id == note_id:
                print(f'Название: {note.title}, Дата: {note.timestamp}, ID: {note.id}')
                print(note.content)
                return
        print('Не найдена заметка с таким ID!')

    def edit_note(self, note_id):
        notes = self.load_notes()

        for note in notes:
            if note.id == note_id:
                print("Введите новый заголовок заметки, оставьте пустым, чтобы оставить прежнее: ")
                title = input()
                print("Введите содержимое заметки, оставьте пустым, чтобы оставить прежнее: ")
                content = input()
                note.title = title if title else note.title
                note.content = content if content else note.content
                note.timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

                self.save_notes(notes)
                print("Заметка успешно изменена.")
                return

        print('Не найдена заметка с таким ID!')


    def delete_note(self, note_id):
        notes = self.load_notes()

        for note in notes:
            if note.id == note_id:
                notes.remove(note)

                self.save_notes(notes)
                print("Заметка успешно удалена.")
                return
        print('Не найдена заметка с таким ID!')

    def export_csv(self):
        try:
            notes_df = pd.read_json(self.notes_file)
            notes_df.to_csv('notes.csv', index=False)
            print("Заметки экспортированы в notes.csv.")
        except FileNotFoundError:
            print(f"Файл {self.notes_file} не найден, сначала сздайте хотя бы одну заметку...")


    def import_csv(self):
        try:
            notes_df = pd.read_csv('notes.csv')
            notes_df.to_json(self.notes_file, orient='records')
            print("Заметки импортированы из notes.csv.")
        except FileNotFoundError:
            print("Файл notes.csv не найден.")

    def manage_notes(self):
        while True:
            print("""Управление заметками:
    1. Создать новую заметку
    2. Просмотреть список заметок
    3. Просмотреть подробности заметки
    4. Редактировать заметку
    5. Удалить заметку
    6. Экспорт заметок в CSV
    7. Импорт заметок из CSV
    8. Назад""")
            choice = input()
            if choice == '1':
                self.create_note()
            elif choice == '2':
                self.view_notes()
            elif choice == '3':
                print('введите ID заметки')
                note_id = input()
                self.view_content(note_id)
            elif choice == '4':
                print('введите ID заметки')
                note_id = input()
                self.edit_note(note_id)
            elif choice == '5':
                print('введите ID заметки')
                note_id = input()
                self.delete_note(note_id)
            elif choice == '6':
                self.export_csv()
            elif choice == '7':
                self.import_csv()
            elif choice == '8':
                print('выход из программы')
                break
            else:
                print('некорректный выбор')
