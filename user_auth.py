import sqlite3 as sqlka
from admin_rules import Administrator, Database
from employee_rules import Employee
from client_rules import Customer


class UserAuth:
    def __init__(self, caf3shka):
        self.conn = sqlka.connect(caf3shka)
        self.cursor = self.conn.cursor()
        self.db = Database(caf3shka)

    def login(self, username, password):
        self.cursor.execute("SELECT * FROM Users WHERE username = ? AND password = ?", (username, password))
        user = self.cursor.fetchone()
        self.cursor.execute("SELECT role FROM Users WHERE username = ? AND password = ?", (username, password))
        role = self.cursor.fetchone()
        if role:
            print("----------------------------------------------------------------------")
            print("Авторизация прошла успешно! Роль пользователя:", user[3])
            if role[0] == "администратор":
                print()
                print(f" > Выполнен вход за администратора, добро пожаловать {username}!")
                print("----------------------------------------------------------------------")
                print("")
                while True:
                    print()
                    print("Что вы хотите сделать?")
                    print("1. Посмотреть всех сотрудников")
                    print("2. Удалить сотрудника")
                    print("3. Добавить нового сотрудника")
                    print("4. Изменить что-то у сотрудника")
                    print("5. Выйти из программы")
                    print("--------------------------------")
                    choice_one = input()
                    match choice_one:
                        case '3':
                            admin = Administrator(user, self.db)
                            name = input("Введите имя сотрудника: ")
                            fam = input("Введите фамилию сотрудника: ")
                            otch = input("Введите отчество сотрудника: ")
                            position = input("Введите должность сотрудника: ")
                            salary = float(input("Введите зарплату сотрудника: "))
                            admin.add_employee(name, fam, otch, position, salary)
                        case '2':
                            admin = Administrator(user, self.db)
                            employee_id = input("Введите ID сотрудника для удаления: ")
                            admin.delete_employee(employee_id)
                        case '1':
                            print(" ★ Все сотрудники: ")
                            admin = Administrator(user, self.db)
                            admin.list_employees()
                        case '4':
                            admin = Administrator(user, self.db)
                            print("Что вы хотите изменить: роль(1), зпшку(2) или ничего не хотите менять(3)?")
                            choice_two = input()
                            if choice_two == '1':
                                employee_id = input("Введите ID сотрудника, роль которого нужно изменить: ")
                                new_role = input("Введите новую роль сотрудника: ")
                        #для обновления роли
                                admin.update_employee(employee_id, new_role=new_role)
                            elif choice_two == '2':
                                employee_id = input("Введите ID сотрудника, зарплату которого нужно изменить: ")
                                new_salary = input("Введите новую зарплату сотрудника: ")
                        #для обновления зарплаты
                                admin.update_employee(employee_id, new_salary=float(new_salary))
                            elif choice_two == '3':
                                print("Как скажете")
                            else:
                                print("Некорректный выбор")
                        case '5':
                            print("★ Вы завершили работу с программой")
                            break

            if role[0]  == "сотрудник":
                print()
                print(f" > Выполнен вход за сотрудника, добро пожаловать {username} !")
                print("----------------------------------------------------------------------")
                print("")
                while True:
                    print()
                    print("Что вы хотите сделать?")
                    print("1. Посмотреть список товаров")
                    print("2. Принять новые товары")
                    print("3. Удалить товары")
                    print("4. Изменить товары")
                    print("5. Посмотреть выбранный товар")
                    print("6. Выйти из программы")
                    print("----------------------")
                    choice_three = input()
                    match choice_three:
                        case '1':
                            print("★ Список товаров: ")
                            employee = Employee(username, self.db)
                            employee.list_products()
                        case '6':
                            print(" ★ Вы завершили работу с программой")
                            return
                        case '2':
                            employee = Employee(username, self.db)
                            name = input("Введите название товара: ")
                            price = input("Введите цену товара: ")
                            count = input("Введите количество товара: ")
                            employee.add_product(name, price, count)
                        case '4':
                            employee = Employee(username, self.db)
                            product_id = input("Введите ID товара, который вы хотите изменить: ")
                            if product_id.isdigit():
                                print("Выберите, что вы хотите изменить: ")
                                print("1. Название товара")
                                print("2. Цену товара")
                                print("3. Количество товара")
                                print("4. Ничего не хочу менять")
                                choice1 = input()
                                if choice1 == '1':
                                    new_name = input("Введите новое название товара: ")
                                    employee.update_product(int(product_id), new_name=new_name)
                                elif choice1 == '2':
                                    new_price = input("Введите новую цену товара: ")
                                    employee.update_product(int(product_id), new_price=new_price)
                                elif choice1 == '3':
                                    new_count = input("Введите новое количество товара: ")
                                    employee.update_product(int(product_id), new_count=new_count)
                                elif choice1 == '4':
                                    print("Как скажете")
                                else:
                                    print("Некорректный выбор")
                            else:
                                print("Некорректный ID товара")

                        case '3':
                            employee = Employee(username, self.db)
                            product_id = input("Введите ID товара для удаления: ")
                            employee.delete_product(product_id)
                        case '5':
                            employee = Employee(username, self.db)
                            product_id = input("Введите ID товара для просмотра: ")
                            employee.filter_product(product_id)

            if role[0] == "клиент":
                print()
                print(f"> Выполнен вход за клиента, добро пожаловать {username} !!")
                print("----------------------------------------------------------------------")
                print("")
                while True:
                    print()
                    print("Что вы хотите сделать?")
                    print("1. Посмотреть список заказов")
                    print("2. Сделать новый заказ")
                    print("3. Удалить заказ")
                    print("4. Изменить заказ")
                    print("5. Выйти из программы")
                    print("----------------------")
                    choice_four = input()
                    match choice_four:
                        case '1':
                            print("★ Список Ваших заказов:")
                            customer = Customer(user[0], self.db)
                            customer.list_orders()
                        case '3':
                            customer = Customer(user[0], self.db)
                            order_id = input("Введите ID заказа для удаления: ")
                            customer.delete_order(order_id)
                        case '2':
                            customer = Customer(user[0], self.db)
                            name_of_order = input("Введите название заказа: ")
                            order_date = input("Введите дату заказа (гггг-мм-дд): ")
                            count_order = int(input("Введите количество товаров: "))
                            customer.add_order(name_of_order, order_date, count_order)
                        case '4':
                            customer = Customer(user[0], self.db)
                            order_id = input("Введите ID заказа, который нужно изменить: ")
                            print("Что вы хотите изменить: название(1), дату(2), количество(3) или ничего (4)?")
                            choice_two2 = input()
                            match choice_two2:
                                case '1':
                                    new_name_of_order = input("Введите новое название заказа: ")
                                    customer.update_order(order_id, name_of_order=new_name_of_order)
                                case '2':
                                    new_order_date = input("Введите новую дату заказа (гггг-мм-дд): ")
                                    customer.update_order(order_id, order_date=new_order_date)
                                case '3':
                                    new_count_order = int(input("Введите новое количество в заказе: "))
                                    customer.update_order(order_id, count_order=new_count_order)
                                case '4':
                                    print("Как скажете")
                                case _:
                                    print("Некорректный выбор")
                        case '5':
                            print("★ Вы завершили работу с программой")
                            break

        else:
            print("Ошибка авторизации! Проверьте свои данные и попробуйте ввести их снова")
            return


    def register(self, username, password, role):
        self.cursor.execute("INSERT INTO Users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
        self.conn.commit()
        print("★ Регистрация прошла успешно!")

    def close_connection(self):
        self.conn.close()