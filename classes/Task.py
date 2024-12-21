import datetime, json, uuid
import pandas as pd

class Task:
    def __init__(self, task_id, title, description, priority, due_date):
        self.id = task_id
        self.title = title
        self.description = description
        self.done = False
        self.priority = priority
        self.due_date = due_date

class TasksManagement:
    def __init__(self, tasks_file):
        self.tasks_file = tasks_file

    def load_tasks(self):
        try:
            with open(self.tasks_file) as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_tasks(self, tasks):
        with open(self.tasks_file, 'w') as file:
            json.dump(tasks, file)



    def create_task(self):
        tasks = self.load_tasks()

        task_id = uuid.uuid4()
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
                print(f'Название: {task.title}, Статус: {task.done}, Приоритет: {task.priority}, Срок: {task.due_date}') #TODO - сделать стрип
        else:
            print('Нет задач!')

    def complete_task(self, task_id):
        tasks = self.load_tasks()

        for task in tasks:
            if task.id == task_id:
                task.done = True
                self.save_tasks(tasks)
                print("Задача успешно изменена.")
                break

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

                task.title = title if title else 0
                task.description = description if description else 0
                task.priority = priority if priority else 0
                task.due_date = due_date if due_date else 0

                self.save_tasks(tasks)
                print("Задача успешно изменена.")
                break

        print('Не найдена Задача с таким ID!')


    def delete_task(self, task_id):
        tasks = self.load_tasks()

        for task in tasks:
            if task.id == task_id:
                tasks.remove(task)

                self.save_tasks(tasks)
                print("Задача успешно удалена.")
                break

        print('Не найдена Задача с таким ID!')



    def export_csv(self):
        tasks_df = pd.read_json(self.tasks_file)
        tasks_df.to_csv('tasks.csv', index=False) #TODO прочитать че это все значит
        print("задачи экспортированы в tasks.csv.")

    def import_csv(self):
        try:
            tasks_df = pd.read_csv('tasks.csv')
            tasks_df.to_json(self.tasks_file, orient='records', lines=True) #TODO прочитать че это все значит
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
                task_id = int(input())
                self.complete_task(task_id)
            elif choice == 4:
                print('введите ID задачи')
                task_id = int(input())
                self.edit_task(task_id)
            elif choice == 5:
                print('введите ID задачи')
                task_id = int(input())
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