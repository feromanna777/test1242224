# num1 = int(input())
# num2 = int(input())
# num3 = int(input())

# num1 = 1
# num2 = 2
# num3 = 3
#
# max_num = max(num1, num2, num3)
# min_num = min(num1, num2, num3)
# middle_num = (num1 + num2 + num3) - (max_num + min_num)
#
# print(max_num, middle_num, min_num, sep="\n")
# print(max_num)
# , middle_num, min_num, sep="/n")

# bacon = 20
#
# bacon+=1
# print(bacon)


# c=round (5.7)
# print(c)
#
# name = 'Мэри'
# password = 'рыба-меч'
# if name == 'Мэри':
#     # print('Привет, Мэри')
#
#     if password == 'рыба-меч':
#         print('Предоставлен доступ.')
#     else:
#         print('Неверный пароль.')

# number = input()

# Получаем отдельные цифры числа
# digit1 = int(number[0])
# digit2 = int(number[1])
# digit3 = int(number[2])
# digit4 = int(number[3])

# Находим минимальную, максимальную и среднюю цифры
# min_digit = min(digit1, digit2, digit3, digit4)
# max_digit = max(digit1, digit2, digit3, digit4)
# min_digit = digit1
# if digit1 <= digit2 and digit1 <= digit3 and digit1<= digit4:
#     min_digit = digit1
#
#
# if digit2 <= digit1 and digit2 <= digit3 and digit2 <= digit4:
#     min_digit = digit2
# if digit3 <= digit1 and digit3 <= digit2 and digit3 <= digit4:
#     min_digit = digit3
# if digit3 <= min_digit:
#     min_digit = digit3
#     print(min_digit)
#     if middle2_digit >= digit3:
#         middle2_digit = digit3
#         middle3_digit = digit1
#         print(min_digit)
# if digit4 <= min_digit:
#     min_digit = digit4
#     print(min_digit)
# print(min_digit)


# number = input()
#
# # Сортируем цифры числа в порядке возрастания
# sorted_number = ''.join(sorted(number))
# print(sorted_number)
#
# # Удаляем ведущие нули
# smallest_number = str(int(sorted_number))
#
# print("Наименьшее возможное четырехзначное число:", smallest_number)

# print("Agb"=="agb")



# number = int(input())
#
# quotient=number//8
# print(quotient)
# while quotient > 8:
#     quotient = quotient // 8
#     print("quotient" ,quotient)
# first_digit=quotient
# print(first_digit)




# number = int(input())
#
# # Переводим число в восьмеричную систему счисления
# octal_number = ""
# quotient = number
#
# while quotient > 0:
#     remainder = quotient % 8
#     octal_number = str(remainder) + octal_number
#     quotient = quotient // 8
#
# # Получаем первую цифру восьмеричного числа
# first_digit = int(octal_number[0])
#
# print( first_digit)


#Функции
# def test():
#     number *= 2
#     return number + 5
#
#
# number = 5
# print(test())

# def outer_function():
#     x = 10  # Variable defined in the outer function
#
#     def inner_function():
#         nonlocal x  # Declare x as a nonlocal variable
#         x += 5  # Modify the value of x
#
#         print("Inner function:", x)
#
#     inner_function()
#     print("Outer function:", x)
#
# outer_function()




# def count_ones(number):
#     answer=number %10
#     return answer
# print(count_ones(int(input())))

# def repeat(number: int, line: str, sep=" "):
#     """
#     number: int - количество повторов
#     line:   str - дублирующая строка
#     sep:    str - символ разделитель
#     """
#     print((line + sep) * number)
#
#
# repeat(5, "Python")         # Python Python Python Python Python
#
# repeat(5, "Python", " | ")  # Python | Python | Python | Python | Python |

# def run_test():
#     questions = {
#         "Вопрос 1": {
#             "вариант1": False,
#             "вариант2": False,
#             "вариант3": True,
#             "вариант4": False
#         },
#         "Вопрос 2": {
#             "вариант1": True,
#             "вариант2": False,
#             "вариант3": False,
#             "вариант4": False
#         },
#         "Вопрос 3": {
#             "вариант1": False,
#             "вариант2": False,
#             "вариант3": False,
#             "вариант4": True
#         },
#         "Вопрос 4": {
#             "вариант1": False,
#             "вариант2": True,
#             "вариант3": False,
#             "вариант4": False
#         },
#         "Вопрос 5": {
#             "вариант1": True,
#             "вариант2": False,
#             "вариант3": False,
#             "вариант4": False
#         }
#     }
#
#     score = 0
#
#     for question, answers in questions.items():
#         print(question)
#         for option, is_correct in answers.items():
#             print(option)
#
#         user_choice = input("Выберите вариант ответа (введите номер): ")
#
#         if user_choice in answers and answers[user_choice]:
#             score += 1
#
#     print("Результат:")
#     print("Правильных ответов:", score)
#     print("Неправильных ответов:", len(questions) - score)
#
#     if score < len(questions) / 2:
#         retry = input("Результат неудовлетворительный. Хотите пройти тест еще раз? (да/нет): ")
#         if retry.lower() == "да":
#             run_test()
#
#
# run_test()
import random

def test(
    question: str,        # вопрос
    right_answer: str,    # правильный ответ
    wrong_answer_1: str,  # неправильный ответ
    wrong_answer_2: str,  # неправильный ответ
    wrong_answer_3: str,  # неправильный ответ
):
    score = 0
    spisok=[right_answer,wrong_answer_1, wrong_answer_2,wrong_answer_3]
    random.shuffle(spisok)

    print(question)
    for i in spisok:
        print(i,end=" ")

    user_choice = input("Выберите вариант ответа")


    if user_choice == right_answer:

        score += 1
    return score



while True:

    score1=test("2 + 2 = ?", "4", "3", "5", "2")
    score2=test("2 + 3 = ?", "5", "3", "5", "2")
    score3=test("2 + 1 = ?", "3", "3", "5", "2")
    score4=test("2 + 4 = ?", "6", "3", "5", "2")
    score5=test("4 + 4 = ?", "8", "3", "5", "2")
    right_anwers=score1+score2+score3+score4+score5
    print("Правильных ответов:",right_anwers)

    if right_anwers < 5 / 2:
           try_again = input("Результат неудовлетворительный. Хотите пройти тест еще раз? (да/нет): ")
           if try_again =="да":
               continue
    break