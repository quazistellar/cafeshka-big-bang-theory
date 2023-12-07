from admin_rules import User

class Customer(User):
    #наследование, инкапсуляция
    def __init__(self, user_id, db):
        super().__init__(user_id)
        self.__db = db

    def add_order(self, name_of_order, order_date, count_order):
        #сделать заказ
        query = "INSERT INTO Orders (user_id, name_of_order, order_date, count_order) VALUES (?, ?, ?, ?)"
        self.__db.execute_query(query, (self.user_id, name_of_order, order_date, count_order))

    def update_order(self, order_id, name_of_order=None, order_date=None,  count_order=None):
        #обновить/изменить что-то в заказе
        if name_of_order:
            query = "UPDATE Orders SET name_of_order = ? WHERE id = ? AND user_id = ?"
            self.__db.execute_query(query, (name_of_order, order_id, self.user_id))
        if order_date:
            query = "UPDATE Orders SET order_date = ? WHERE id = ? AND user_id = ?"
            self.__db.execute_query(query, (order_date, order_id, self.user_id))
        if count_order:
            query = "UPDATE Orders SET count_order = ? WHERE id = ? AND user_id = ?"
            self.__db.execute_query(query, (count_order, order_id, self.user_id))

    def list_orders(self):
        #показать список заказов только на ВЫБРАННОМ пользователе
        query = "SELECT id, name_of_order, order_date, count_order FROM Orders WHERE user_id = ?"
        result = self.__db.execute_query(query, (self.user_id,))
        for row in result:
            id, name_of_order, order_date, count_order = row
            print(f"ID: {id}, Наименование заказа: {name_of_order}, Дата заказа: {order_date}, Количество: {count_order}")

    def delete_order(self, order_id):
        #удалить заказ
        query = "DELETE FROM Orders WHERE id = ? AND user_id = ?"
        self.__db.execute_query(query, (order_id, self.user_id))

