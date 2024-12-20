import datetime, json, uuid
import pandas as pd

class Note:
    def __init__(self, note_id, title, content):
        self.id = note_id
        self.title = title
        self.content = content
        self.timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

class NotesManagement:
    def __init__(self, notes_file):
        self.notes_file = notes_file

    def load_notes(self):
        try:
            with open(self.notes_file) as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def create_note(self):
        notes = self.load_notes()

        title = input("Введите заголовок заметки: ")
        content = input("Введите содержимое заметки: ")
        note_id = uuid.uuid4()
        note = Note( note_id, title, content)
        notes.append(note)

        with open(self.notes_file, 'w') as file:
            json.dump(notes, file)

        print("Заметка успешно создана.")

    def view_notes(self):
        notes = self.load_notes()

        if notes:
            for note in notes:
                print(f'Название: {note.title}, Дата: {note.timestamp}') #TODO - сделать стрип
        else:
            print('Нет заметок!')

    def view_content(self, note_id):
        notes = self.load_notes()

        for note in notes:
            if note.id == note_id:
                print(f'Название: {note.title}, Дата: {note.timestamp}')  # TODO - сделать стрип
                print(note.content)
                break
        print('Не найдена заметка с таким ID!')

    def edit_note(self, note_id):
        notes = self.load_notes()

        for note in notes:
            if note.id == note_id:
                print("Введите новый заголовок заметки, оставьте пустым, чтобы оставить прежнее: ")
                title = input()
                print("Введите содержимое заметки, оставьте пустым, чтобы оставить прежнее: ")
                content = input()
                note.title = title if title else 0
                note.content = content if content else 0
                note.timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

                with open(self.notes_file, 'w') as file:
                    json.dump(notes, file)

                print("Заметка успешно изменена.")
                break

        print('Не найдена заметка с таким ID!')


    def delete_note(self, note_id):
        notes = self.load_notes()

        for note in notes:
            if note.id == note_id:
                notes.remove(note)

                with open(self.notes_file, 'w') as file:
                    json.dump(notes, file)

                print("Заметка успешно удалена.")
                break
        print('Не найдена заметка с таким ID!')



    def export_csv(self):
        notes_df = pd.read_json(self.notes_file)
        notes_df.to_csv('notes.csv', index=False) #TODO прочитать че это все значит
        print("Заметки экспортированы в notes.csv.")

    def import_csv(self):
        try:
            notes_df = pd.read_csv('notes.csv')
            notes_df.to_json(self.notes_file, orient='records', lines=True) #TODO прочитать че это все значит
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
            choice = int(input())
            if choice == 1:
                self.create_note()
            elif choice == 2:
                self.view_notes()
            elif choice == 3:
                print('введите ID заметки')
                note_id = int(input())
                self.view_content(note_id)
            elif choice == 4:
                print('введите ID заметки')
                note_id = int(input())
                self.edit_note(note_id)
            elif choice == 5:
                print('введите ID заметки')
                note_id = int(input())
                self.delete_note(note_id)
            elif choice == 6:
                self.export_csv()
            elif choice == 7:
                self.import_csv()
            elif choice == 8:
                print('выход из программы')
                break
            else:
                print('некорректный выбор')
