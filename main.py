import re
reg_name = re.compile(r'^[A-Za-zA-Яа-яЁё]+$')



user_name = input("Введите Имя пользователя: ")

if reg_name.match(user_name):
    print(f"Имя {user_name} принято!")
else:
    print("Ввод некорректен повторите! Повторите ввод данных!\n")