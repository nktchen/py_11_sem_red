from classes.Calculator import Calculator
from classes.Finance import FinancesManagement
from classes.Note import NotesManagement
from classes.Task import TasksManagement
from classes.Contact import ContactsManagement

Notes = NotesManagement("notes.json")
Tasks = TasksManagement("tasks.json")
Contacts = ContactsManagement('contacts.json')
Finances = FinancesManagement('finances.json')
Calculators = Calculator()

def manage_contacts():
    return

def manage_finances():
    return

def calculator():
    return

while True:
    print("""Добро пожаловать в Персональный помощник!
    Выберите действие:
    1. Управление заметками
    2. Управление задачами
    3. Управление контактами
    4. Управление финансовыми записями
    5. Калькулятор
    6. Выход""")
    choice = input()
    if choice == '1':
        Notes.manage_notes()
    elif choice == '2':
        Tasks.manage_tasks()
    elif choice == '3':
        Contacts.manage_contacts()
    elif choice == '4':
        Finances.manage_finances()
    elif choice == '5':
        Calculators.main_loop()
    elif choice == '6':
        print('выход из программы')
        break
    else:
        print('некорректный выбор')





