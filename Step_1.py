# 1.
# a = input("Введите ваш возраст: ")
# b = input("Введите ваш рост: ")
# c = input("Введите ваше имя: ")
# information = input("Впишите команду ""info"", чтобы проверить введенную информацию: ")
# if information == "info":
#     print("Возраст - " + a + "; Рост - " + b + " Ваше имя - " + c)

# 2.
# Number = int(input("Введите количество секунд: "))
# while Number <= 0:
#     input("Количество отрицательным быть не может!")
#     number = int(input("Введите положительное число: "))
# Seconds = int(Number % 60)
# Minutes = int((Number // 60) % 60)
# Hours = int(Number // 3600)
# print(f'{Hours:02}:{Minutes:02}:{Seconds:02}')

# 3.
# number = int(input("Введите число: "))
# n = number
# if n < 0:
#     symbol = "-"
# else:
#     symbol = ""
# print(int(f'{symbol}{number}') + int(f'{symbol}{number}{number}') + int(f'{symbol}{number}{number}{number}'))

# 4.
# number = int(input("Введите целое положительное число: "))
# fl = number % 1
# while number <= 0 or fl != 0:
#     input("Введено некорректное число!")
#     number = int(input("Введите целое положительное число: "))
# my_list = list(str(number))
# my_max = 0
# i = 0
# while i < len(str(number)):
#     if int(my_list[i]) > my_max:
#         my_max = int(my_list[i])
#     i += 1
# print(my_max)

# 5.6
# import sys
# # sys в данном случае - просто декорация
# rent = False
# a = int(input("Ведите сумму выручки: "))
# if a < 0:
#     print("Отрицательная выручка?")
#     sys.exit()
# b = int(input("Ведите сумму издержек: "))
# if b < 0:
#     print("Отрицательные издержки?")
#     sys.exit()
# c = abs(a - b)
# if a < b:
#     print(f'Издержки больше выручки на {c} рублей')
# else:
#     rent = True
#     print(f'Выручка больше издержек на {c} рублей')
# if rent:
#     rent_number = c / a * 100
#     print(f'Рентабельность выручки составила {rent_number}%')
#     ppl_number = int(input("Введите количество сотрудников: "))
#     print(f'Рентабельность выручки на сотрудника составила {rent_number / ppl_number} процентов')

# 7.
# a = int(input("Сколько км в день пробегает спортсмен? "))
# b = int(input("Сколько он должен пробегать? "))
# day_x = 1
# while a < b:
#     print(f'{day_x}-й день: {a}')
#     a = float("%.2f" % (a + (a * 0.1)))
#     day_x += 1
# print(f'{day_x}-й день: {a}')

