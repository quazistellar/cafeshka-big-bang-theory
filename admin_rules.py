import sqlite3 as sqlka

# коннект с бдшкой
class Database:
    def __init__(self, cafeshka1):
        self.conn = sqlka.connect(cafeshka1)

    #для запросов из бд
    def execute_query(self, query, params=None):
        cursor = self.conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        self.conn.commit()
        return cursor.fetchall()
    def __del__(self):
        self.conn.close()

# базовый класс для пользователей
class User:
    def __init__(self, user_id):
        self.user_id = user_id

class Administrator(User):
    def __init__(self, user_id, db):
        super().__init__(user_id)
        self.db = db

    def add_employee(self, name, fam, otch, position, salary):
        #добавление нового сотрудника в бдшку
        query = "INSERT INTO Employees (name, fam, otch, positionRole, salary) VALUES (?, ?, ?, ?, ?)"
        self.db.execute_query(query, (name, fam, otch, position, float(salary)))

    def update_employee(self, employee_id, new_role=None, new_salary=None):
        #обновление роли или зарплаты сотрудника в бдшке
        if new_role:
            query = "UPDATE Employees SET positionRole = ? WHERE id = ?"
            self.db.execute_query(query, (new_role, employee_id))
        if new_salary:
            query = "UPDATE Employees SET salary = ? WHERE id = ?"
            self.db.execute_query(query, (new_salary, employee_id))

    def list_employees(self):
        #вывод списка всех сотрудников c их должностями и зпшками
        query = "SELECT id, name, fam, positionRole, salary FROM Employees"
        result = self.db.execute_query(query)
        for row in result:
            employee_id, name, fam, position, salary = row
            print(f"ID: {employee_id}, Имя: {name} {fam} , Должность: {position}, Зарплата: {salary}")

    def delete_employee(self, employee_id):
        #удаление выбранного сотрудника из бдшки
        query = "DELETE FROM Employees WHERE id = ?"
        self.db.execute_query(query, (employee_id,))

