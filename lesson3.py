# a = True
# b = False
#
# print(a, b)


# a = 1 > 4 # True
#
# print(a)
# print(1 > 4)
# print(1 < 4)
# print(1 >= 4)
# print(1 <= 4)
# print(4 == 4) # True
# print(1 != 4)

# a = "abc" == "abc" # True
# b = "aBc" == "abc" # False
# c = "cvd" != "aaa"
# d = "Hwq" < "G"
# #
# print(a, b, c, d)


# age = 16
#
# if age >= 18:
#     print("Добро пожаловать!")
#     print("Привет")
# else:
#     print("Доступ запрещен :(")
#
# print("Продолжение программы...")

# age = 15
# is_admin = True
#
# if age >= 18:
#     print("Добро пожаловать!")
#     print("Привет")
# elif is_admin == True:
#     is_admin = False
#     print("Привет, админ!")
# else:
#     print("Доступ запрещен :(")
# #
# print(is_admin)
# print("Продолжение программы...")

# age = 21
# is_citizen = True
# is_citizen = False
# is_admin = True
#
# if age >= 18 and is_citizen == True and is_admin:
#     print("Вы можете голосовать!")
# else:
#     print("Вы не можете голосовать!")
#
# print("Продлолжение...")
#
#
# is_student = False
# is_senior = True

# is_student = False
# is_senior = True
#
# if is_student or is_senior:
#     print("Вам положена скидка!")
# else:
#     print("Скидки не будет")
# #
# age = 12
# is_admin = True
#
# if age >= 18 and is_admin:
#     print("...")

# is_admin = True
#
# if is_admin:
#     print("Привет, админ!")

# # Проверяем, что ввод — это число
# try:
#     age = int(input("Введите ваш возраст: "))
# except ValueError:
#     print("Ошибка: введите число!")
#     exit()  # Завершаем программу, если ввод некорректный
#
# # Если возраст меньше 18, сразу запрещаем доступ
# if age < 18:
#     print("Доступ запрещён! Вам нет 18 лет.")
#     exit()
#
# # Если возраст 18 или больше, запрашиваем пароль
# password = input("Введите пароль (если вы админ): ")
# is_admin = password == "123"  # Проверяем, правильный ли пароль
#
# # Проверяем доступ
# if is_admin:
#     print("Доступ разрешён! Вы вошли как администратор.")
# else:
#     print("Доступ разрешён! Вы прошли по возрасту.")




# age = int(input()) # 12
#
# if age >= 18:
#     print("Вы взрослый!")
# else:
#     print("Вы не взрослый")

# 1, -1, "abc", True, 3.14, ...
# 0, None, False, "", ...

# if True:               # 1, -1, "abc", True, 3.14, ... - будет True
#                        # 0, None, False, "", ... - будет False
#     print("Привет!")


count = 0

# if count:
#     print(f"У меня есть деньги! {count}$")
# else:
#     print("У меня нет денег :(")

# string1 = "Hello"
# string2 = "hello"
#
# print(string1.lower() == string2.lower())

# print("abca" in "123123abc")

# string = "Hello"
# num = len(string)
#
# print(num)

# string = "Hello"
#
# print(len(string) < 10)

# range(5) # (0, 1, 2, 3, 4)

# for i in range(5): # (0, 1, 2, 3, 4)
#     print(i)
#
# for i in range(5):  # (0, 1, 2, 3, 4)
#     print(i)

# for c in "Hello":
#     print(c)
#     print("---")

# for i in range(12):
#     print(i)

# string = "Hello"
# n = 5
#
# for _ in range(n):
#     print(string)

# i, j, k
# for i in range(10):
#     print(i)
#
# # char
# for c in "Hello":
#     print(c)

string = "Hello world!"
n = 3

for c in string:
    print(f"Проверяю букву {c}")
    if c == "l":
        print("Есть!")
        n += 1
    else:
        print("Это не буква l")

print(n)
#
# n = 0
#
# for i in range(5): # 0, 1, 2, 3, 4
#     n += i
#
# print(n)

# password = "klsdkdfnk*fd"
#
# for c in password:
#     if c == "*":
#         print("* - под запретом!")
#         break
#     print(c)
#
# print("Продолжение программы...")

# password = "klsdkdfnk*fd"
#
# for c in password:
#     if c == "*":
#         continue
#     print(c)

# password = "*ls*dkdfnkfddgdfgfg3434"
# is_correct = True
#
# for c in password:
#     if c == "*":
#         is_correct = False
#         break
#     print(c)

# if is_correct:
#     print("Пароль хороший!")
# else:
#     print("Недопустимый пароль!")
#
# print("Продолжение программы...")

# string = ""
#
# while string != "exit":
#     string = input()
#     print(string, "!!!!")












