from admin_rules import User

class Employee(User):
    def __init__(self, user_id, db):
        super().__init__(user_id)
        self.db = db

    def add_product(self, name, price, count):
        #добавление нового товара в бдшку
        query = "INSERT INTO Products (name, price, count) VALUES (?, ?, ?)"
        self.db.execute_query(query, (name, float(price), float(count)))

    def update_product(self, product_id, new_name=None, new_price=None, new_count=None):
        #обновление названия или цены товара/количества в бдшке
        if new_name:
            query = "UPDATE Products SET name = ? WHERE id = ?"
            self.db.execute_query(query, (new_name, product_id))
        if new_price:
            query = "UPDATE Products SET price = ? WHERE id = ?"
            self.db.execute_query(query, (float(new_price), product_id))
        if new_count:
            query = "UPDATE Products SET count = ? WHERE id = ?"
            self.db.execute_query(query, (float(new_count), product_id))

    def list_products(self):
        #вывод списка всех товаров с их названиями и ценами и кол-вом
        query = "SELECT id, name, price, count FROM Products"
        result = self.db.execute_query(query)
        for row in result:
            id, name, price, count = row
            print(f"ID: {id}, Название: {name}, Цена: {price}, Количество: {count}")

    def delete_product(self, product_id):
        #удаление выбранного товара из бдшки
        query = "DELETE FROM Products WHERE id = ?"
        self.db.execute_query(query, (product_id,))

    def filter_product(self, product_id):
        #показ выбранного товара из бдшки (фильтрация)
        query = "SELECT * FROM Products WHERE id = ?"
        print(self.db.execute_query(query, (product_id,)))

