import json, uuid

import pandas as pd

class Contact:
    def __init__(self, id, name, phone, email):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    def __dict__(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
        }

class ContactsManagement:
    def __init__(self, contacts_file):
        self.contacts_file = contacts_file

    def load_contacts(self):
        try:
            with open(self.contacts_file) as f:
                json_loaded =  json.load(f)
                return [Contact(**contact) for contact in json_loaded]
        except FileNotFoundError:
            return []

    def save_contacts(self, contacts):
        dict_contacts = [contact.__dict__() for contact in contacts]
        with open(self.contacts_file, 'w') as file:
            json.dump(dict_contacts, file)

    def create_contact(self):
        contacts = self.load_contacts()

        contact_id = str(uuid.uuid4())
        name = input("Введите имя контакта: ")
        phone = input("Введите номер контакта: ")
        email = input("Введите почту контакта: ")

        contact = Contact(contact_id, name, phone, email)
        contacts.append(contact)

        self.save_contacts(contacts)
        print("контакт успешно создан.")

    def find_contact(self):
        contacts = self.load_contacts()
        print('выберите тип поиска: 1 - по номеру, 2 - по имени')
        choice = int(input())
        if choice == 1:
            print('введите номер')
            phone_search = input()
            for contact in contacts:
                if contact.phone == phone_search:
                    print(f'имя: {contact.name} номер: {contact.phone}, почта: {contact.email}, id: {contact.id}')
                    print('изменено')
                    return
            print('не найдено')
        elif choice == 2:
            print('введите имя')
            name_search = input()
            for contact in contacts:
                if contact.name == name_search:
                    print(f'имя: {contact.name} номер: {contact.phone}, почта: {contact.email}, id: {contact.id}')
                    print('изменено')
                    return
            print('не найдено')
        else:
            print('нет такой опции')

    def edit_contact(self, contact_id):
        contacts = self.load_contacts()

        for contact in contacts:
            if contact.id == contact_id:
                print("Введите новый имя контакта, оставьте пустым, чтобы оставить прежний: ")
                name = input()
                print("Введите новое номер контакта, оставьте пустым, чтобы оставить прежнее: ")
                phone = input()
                print("Введите новый почту контакта, оставьте пустым, чтобы оставить прежний: ")
                email = input()

                contact.name = name if name else contact.name
                contact.phone = phone if phone else contact.phone
                contact.email = email if email else contact.email

                self.save_contacts(contacts)
                print("контакт успешно изменена.")
                return

        print('Не найдена Контакт с таким ID!')

    def delete_contact(self, contact_id):
        contacts = self.load_contacts()

        for contact in contacts:
            if contact.id == contact_id:
                contacts.remove(contact)

                self.save_contacts(contacts)
                print("Контакт успешно удалена.")
                return

        print('Не найдена Контакт с таким ID!')

    def export_csv(self):
        try:
            contacts_df = pd.read_json(self.contacts_file)
            contacts_df.to_csv('contacts.csv', index=False)
            print("контакты экспортированы в contacts.csv.")
        except FileNotFoundError:
            print(f"Файл {self.contacts_file} не найден, сначала сздайте хотя бы одну контакт...")

    def import_csv(self):
        try:
            contacts_df = pd.read_csv('contacts.csv')
            contacts_df.to_json(self.contacts_file, orient='records')
            print("контакты импортированы из contacts.csv.")
        except FileNotFoundError:
            print("Файл contacts.csv не найден.")

    def manage_contacts(self):
        while True:
            print("""Управление контактами:
    1. Создать новый контакт
    2. Поиск контакта по номеру телефона или имени
    3. Редактировать контакт
    4. Удалить контакт
    5. Экспорт контактов в CSV
    6. Импорт контактов из CSV
    7. Назад""")
            choice = int(input())
            if choice == 1:
                self.create_contact()
            elif choice == 2:
                self.find_contact()
            elif choice == 3:
                print('введите ID контакты')
                contact_id = input()
                self.edit_contact(contact_id)
            elif choice == 4:
                print('введите ID контакты')
                contact_id = input()
                self.delete_contact(contact_id)
            elif choice == 5:
                self.export_csv()
            elif choice == 6:
                self.import_csv()
            elif choice == 7:
                print('выход из программы')
                break
            else:
                print('некорректный выбор')