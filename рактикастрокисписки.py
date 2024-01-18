"строки"

# letter="А"
#
#
#
#
# def letter_to_number(letter):
#     # Преобразуем букву в верхний регистр, чтобы учитывать и строчные буквы.
#     letter = letter.upper()
#
#     # Получаем ASCII-код буквы и вычитаем код буквы 'A'.
#     # Таким образом, получим номер буквы в алфавите (A -> 1, B -> 2, и т.д.).
#     return ord(letter) - ord('А') + 1
#
#
# def main():
#     input_string = input("Введите строку: ")
#
#     for letter in input_string:
#         if letter.isalpha():  # Проверяем, является ли символ буквой.
#             number = letter_to_number(letter)
#             original_tuple =(letter,number)
#             print(original_tuple)
#             # print(f"Буква '{letter}' имеет номер в алфавите: {number}")
#
#
# main()






# # Должна быть введена любая строчная
# # буква английского алфавита.
# c = input("Letter (a-z): ")
# # Функция ord() возвращает порядковый
# # номер символа в таблице символов.
# c = ord(c)
# print(c)
# # Находим порядковый номер первой
# # буквы алфавита.
# a = ord('а')
# print("а")
# # Поскольку буквы идут по-порядку,
# # то вычитая коды символов, мы находим
# # расстояние между ними.
# n = c - a
# # Так как требуется найти не расстояние,
# # а порядковый номер буквы в алфавите,
# # прибавляем единицу.
# n = n + 1
# print("Its number is", n)


# def letter_to_number(letter):
#     # Преобразуем букву в верхний регистр, чтобы учитывать и строчные буквы.
#     letter = letter.upper()
#
#     # Получаем ASCII-код буквы и вычитаем код буквы 'A'.
#     # Таким образом, получим номер буквы в алфавите (A -> 1, B -> 2, и т.д.).
#     if ord(letter)>1045:
#         answer=ord(letter) - ord('А') + 2
#     elif letter=="Ё":
#         answer=7
#     else:
#         answer=ord(letter) - ord('А') + 1
#     return answer
#
#
# def main():
#     input_string = input("Введите строку: ")
#
#     for letter in input_string:
#         if letter.isalpha():  # Проверяем, является ли символ буквой.
#             number = letter_to_number(letter)
#             print(f"('{letter}', {number})")
#
#
# if __name__ == "__main__":
#     main()

#7
# def main():
#     num_numbers = int(input("Введите количество чисел: "))
#
#     numbers = []
#     for _ in range(num_numbers):
#         num = int(input())
#         numbers.append(num)
#
#     # Вывод чисел в том же порядке
#     print("\n".join(str(num) for num in numbers))
#     print()
#     # Вывод чисел, утраиваемых
#     tripled_numbers = [num * 3 for num in numbers]
#     print("\n".join(str(num) for num in tripled_numbers))
#
# if __name__ == "__main__":
#     main()


#10


# def determine_winner(input_string):
#     # Разделяем строку на название команды и счёт
#     team1, team2, score = input_string.split(" - ")[0], input_string.split(" - ")[1].split()[0], input_string.split(" ")[1]
#
#     # Извлекаем количество голов/очков для каждой команды
#     team1_score, team2_score = map(int, score.split(":"))
#
#     # Определяем победителя или ничью
#     if team1_score > team2_score:
#         return f"{team1} Победитель"
#     elif team1_score < team2_score:
#         return f"{team2} Победитель"
#     else:
#         return "Ничья"
#
# # Примеры ввода/вывода
# # input_string = input()
# # print(determine_winner(input_string))
#
# print(determine_winner("Земляне - Марсиане 3:2"))




def determine_winner(input_string):
    # Разделяем строку на название команды и счёт
    team1 = input_string.split(" - ")[0]
    team2=input_string.split(" - ")[1].split()[0]
    score=input_string.split(" ")[3]
    print( team1, team2, score)

    # Извлекаем количество голов/очков для каждой команды
    team1_score, team2_score = map(int, score.split(":"))

    # Определяем победителя или ничью
    if team1_score > team2_score:
        return f"{team1} Победитель"
    elif team1_score < team2_score:
        return f"{team2} Победитель"
    else:
        return "Ничья"

# Примеры ввода/вывода
sample_input_1 = "Земляне - Марсиане 3:2"
sample_output_1 = determine_winner(sample_input_1)
print(sample_output_1)  # Output: Земляне Победитель





