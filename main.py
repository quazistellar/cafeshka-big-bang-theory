import sqlite3 as sqlka
from user_auth import UserAuth

#для бдшки
conn = sqlka.connect("caf3shka.db")
cursor = conn.cursor()
auth = UserAuth("caf3shka.db")
chs = ["новенький", "смешарик"]

# интерфейс))))
print()
print("                >>> ИНФОРМАЦИОННАЯ СИСТЕМА <<<                   ")
print("-----------------------------------------------------------------")
print("_________ > то самое кафе из теории большого взрыва < ___________")
print("-----------------------------------------------------------------")
print()
print("> Ты уже смешарик или новенький?  p.s (введи: смешарик/новенький)")

while True:
    choice = input("- ").lower()

    if choice == "смешарик":
        while True:
            print(">> Авторизация")
            while True:
                username = input("Введите логин (имя пользователя системы): ")
                password = input("Введите пароль: ")
                query = "SELECT * FROM Users WHERE username = ? AND password = ?"
                cursor.execute(query, (username, password))
                user = cursor.fetchone()
                if user:
                    auth.login(username, password)
                    break
                else:
                    print("Неверный пароль или логин, попробуйте ещё раз!")
                    continue
            break
        break

    if choice == "новенький":
        while True:
            print(">> Регистрация")
            username = input("Придумайте себе логин (имя пользователя системы): ")
            password = input("Придумайте себе пароль: ")
            role = input("Введите свою роль (администратор/сотрудник/клиент): ").lower()
            roles = {"администратор", "сотрудник", "клиент"}
            if role not in roles:
                print("Такой роли нет!")
                continue
            else:
                auth.register(username, password, role)
                auth.login(username, password)
                break
        break

auth.close_connection()