import json, uuid
import pandas as pd

class Task:
    def __init__(self, id, title, description, priority, due_date, done = False):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.done = done

    def __dict__(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "due_date": self.due_date,
            "done": self.done,
        }

class TasksManagement:
    def __init__(self, tasks_file):
        self.tasks_file = tasks_file

    def load_tasks(self):
        try:
            with open(self.tasks_file) as f:
                json_loaded =  json.load(f)
                return [Task(**task) for task in json_loaded]
        except FileNotFoundError:
            return []

    def save_tasks(self, tasks):
        dict_tasks = [task.__dict__() for task in tasks]
        with open(self.tasks_file, 'w') as file:
            json.dump(dict_tasks, file)

    def create_task(self):
        tasks = self.load_tasks()

        task_id = str(uuid.uuid4())
        title = input("Введите заголовок задачи: ")
        description = input("Введите описание задачи: ")
        priority = input("Введите приоритет - 'Высокий/средний/низкий': ")
        due_date = input("Введите дату окончания в формате 'ДД-ММ-ГГГГ': ")

        task = Task(task_id, title, description, priority, due_date)
        tasks.append(task)

        self.save_tasks(tasks)
        print("Задача успешно создана.")

    def view_tasks(self):
        tasks = self.load_tasks()

        if tasks:
            for task in tasks:
                print(f'Название: {task.title}, Статус: {task.done}, Приоритет: {task.priority}, Срок: {task.due_date},  ID: {task.id}')
        else:
            print('Нет задач!')

    def complete_task(self, task_id):
        tasks = self.load_tasks()

        for task in tasks:
            if task.id == task_id:
                task.done = True
                self.save_tasks(tasks)
                print("Задача успешно изменена.")
                return

        print('Не найдена Задача с таким ID!')


    def edit_task(self, task_id):
        tasks = self.load_tasks()

        for task in tasks:
            if task.id == task_id:
                print("Введите новый заголовок задачи, оставьте пустым, чтобы оставить прежний: ")
                title = input()
                print("Введите новое описание задачи, оставьте пустым, чтобы оставить прежнее: ")
                description = input()
                print("Введите новый приоритет задачи, оставьте пустым, чтобы оставить прежний: ")
                priority = input()
                print("Введите новую дату окончания 'ДД-ММ-ГГГГ' задачи, оставьте пустым, чтобы оставить прежнее: ")
                due_date = input()

                task.title = title if title else task.title
                task.description = description if description else task.description
                task.priority = priority if priority else task.priority
                task.due_date = due_date if due_date else task.due_date

                self.save_tasks(tasks)
                print("Задача успешно изменена.")
                return

        print('Не найдена Задача с таким ID!')


    def delete_task(self, task_id):
        tasks = self.load_tasks()

        for task in tasks:
            if task.id == task_id:
                tasks.remove(task)

                self.save_tasks(tasks)
                print("Задача успешно удалена.")
                return

        print('Не найдена Задача с таким ID!')



    def export_csv(self):
        try:
            tasks_df = pd.read_json(self.tasks_file)
            tasks_df.to_csv('tasks.csv', index=False)
            print("задачи экспортированы в tasks.csv.")
        except FileNotFoundError:
            print(f"Файл {self.tasks_file} не найден, сначала сздайте хотя бы одну таску...")



    def import_csv(self):
        try:
            tasks_df = pd.read_csv('tasks.csv')
            tasks_df.to_json(self.tasks_file, orient='records')
            print("задачи импортированы из tasks.csv.")
        except FileNotFoundError:
            print("Файл tasks.csv не найден.")

    def manage_tasks(self):
        while True:
            print("""Управление Задачами:
    1. Создать новую задачу
    2. Просмотреть список задач
    3. Выполнить задачу
    4. Редактировать задачу
    5. Удалить задачу
    6. Экспорт задач в CSV
    7. Импорт задач из CSV
    8. Назад""")
            choice = int(input())
            if choice == 1:
                self.create_task()
            elif choice == 2:
                self.view_tasks()
            elif choice == 3:
                print('введите ID задачи')
                task_id = input()
                self.complete_task(task_id)
            elif choice == 4:
                print('введите ID задачи')
                task_id = input()
                self.edit_task(task_id)
            elif choice == 5:
                print('введите ID задачи')
                task_id = input()
                self.delete_task(task_id)
            elif choice == 6:
                self.export_csv()
            elif choice == 7:
                self.import_csv()
            elif choice == 8:
                print('выход из программы')
                break
            else:
                print('некорректный выбор')