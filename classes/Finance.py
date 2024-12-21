import json, uuid
import pandas as pd

class Finance:
    def __init__(self, id, amount, category, date, description):
        self.id = id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def __dict__(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description,
        }

class FinancesManagement:
    def __init__(self, finances_file):
        self.finances_file = finances_file

    def load_finances(self):
        try:
            with open(self.finances_file) as f:
                json_loaded =  json.load(f)
                return [Finance(**finance) for finance in json_loaded]
        except FileNotFoundError:
            return []

    def save_finances(self, finances):
        dict_finances = [finance.__dict__() for finance in finances]
        with open(self.finances_file, 'w') as file:
            json.dump(dict_finances, file)

    def create_finance(self):
        finances = self.load_finances()

        finance_id = str(uuid.uuid4())
        amount = input("Введите сумму операции: ")
        category = input("Введите категорию операции: ")
        date = input("Введите дату операции в формате'ДД-ММ-ГГГГ': ")
        description = input("Введите описание операции: ")

        finance = Finance(finance_id, amount, category, date, description)
        finances.append(finance)

        self.save_finances(finances)
        print("Операциz  успешно создана.")

    def view_finances(self):
        finances = self.load_finances()

        if finances:
            print('выберите тип фильтрации: 1 - по дате, 2 - по категории, нет выбора - без филтрации')
            choice = int(input())
            if choice == 1:
                print('введите день в формате "ДД-ММ-ГГГГ"')
                search_date = input()
                for finance in finances:
                    if finance.date ==  search_date:
                        print(
                            f'сумма операции: {finance.amount}, категория операции: {finance.category}, дата операции: {finance.date}, описание операции: {finance.description},  ID: {finance.id}')
            
            if choice == 2:
                print('введите категорию для поиска')
                search_category = input()
                for finance in finances:
                    if finance.category == search_category:
                        print(
                            f'сумма операции: {finance.amount}, категория операции: {finance.category}, дата операции: {finance.date}, описание операции: {finance.description},  ID: {finance.id}')

            else:
                for finance in finances:
                    print(f'сумма операции: {finance.amount}, категория операции: {finance.category}, дата операции: {finance.date}, описание операции: {finance.description},  ID: {finance.id}')
        else:
            print('Нет операций!')

    def generate_summary(self):
        finances = self.load_finances()

        for finance in finances:
            if finance.id == 0:
                finance.done = True
                self.save_finances(finances)
                print("операция успешно изменена.")
                return
        print('Я не понял какой функционал от меня требуется. ТЗ - во! круто!')
    
    def export_csv(self):
        try:
            finances_df = pd.read_json(self.finances_file)
            finances_df.to_csv('finances.csv', index=False)
            print("задачи экспортированы в finances.csv.")
        except FileNotFoundError:
            print(f"Файл {self.finances_file} не найден, сначала сздайте хотя бы одну таску...")

    def import_csv(self):
        try:
            finances_df = pd.read_csv('finances.csv')
            finances_df.to_json(self.finances_file, orient='records')
            print("задачи импортированы из finances.csv.")
        except FileNotFoundError:
            print("Файл finances.csv не найден.")

    def manage_finances(self):
        while True:
            print("""Управление Задачами:
           1. Добавление новой финансовой записи
           2. Просмотр всех записей с возможностью фильтрации по дате или категории.
           3. Генерация отчётов о финансовой активности за определённый период.
           4. Импорт финансовых записей в формате CSV.
           5. Экспорт финансовых записей в формате CSV.
           6. Назад""")

            choice = int(input())
            if choice == 1:
                self.create_finance()
            elif choice == 2:
                self.view_finances()
            elif choice == 3:
                self.generate_summary()
            elif choice == 4:
                self.import_csv()
            elif choice == 5:
                self.export_csv()
            elif choice == 6:
                print('выход из программы')
                break
            else:
                print('некорректный выбор')