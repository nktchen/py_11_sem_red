import re
class Calculator:
    def plus(self):
        number1 = input("Enter the first number: ")
        number2 = input("Enter the second number: ")
        number1 = re.findall(r'\d', number1)
        number2 = re.findall(r'\d', number2)
        if number1 != [] and number2 != []:
            number1 = int(number1[0])
            number2 = int(number2[0])
            print(number1 + number2)
        else:
            print("Please enter a valid number")

    def minus(self):
        number1 = input("Enter the first number: ")
        number2 = input("Enter the second number: ")
        number1 = re.findall(r'\d', number1)
        number2 = re.findall(r'\d', number2)
        if number1 != [] and number2 != []:
            number1 = int(number1[0])
            number2 = int(number2[0])
            print(number1 - number2)
        else:
            print("Please enter a valid number")

    def multiply(self):
        number1 = input("Enter the first number: ")
        number2 = input("Enter the second number: ")
        number1 = re.findall(r'\d', number1)
        number2 = re.findall(r'\d', number2)
        if number1 != [] and number2 != []:
            number1 = int(number1[0])
            number2 = int(number2[0])
            print(number1 * number2)
        else:
            print("Please enter a valid number")

    def divide(self):
        number1 = input("Enter the first number: ")
        number2 = input("Enter the second number: ")
        number1 = re.findall(r'\d', number1)
        number2 = re.findall(r'\d', number2)
        if number1 != [] and number2 != []:
            number1 = int(number1[0])
            number2 = int(number2[0])
            if number2 != 0:
                print('cant delit na 0')
                return
            print(number1 / number2)
        else:
            print("Please enter a valid number")

    def main_loop(self):
        while True:
            print("""1. Сложение
            2. Вычитание
            3. Умножение
            4. Деление
            5. Выход""")
            choice = int(input())
            if choice == 1:
                self.plus()
            elif choice == 2:
                self.minus()
            elif choice == 3:
                self.multiply()
            elif choice == 4:
                self.divide()
            elif choice == 5:
                break
            else:
                print("Please enter a valid number")