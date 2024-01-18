# def count_word_occurrences(text):
#     word_dict = {}  # Словарь для хранения порядковых номеров слов
#     words = text.split()  # Разбиваем текст на слова
#
#     for word in words:
#
#         if word in word_dict:
#             word_dict[word] += 1
#
#
#         else:
#             word_dict[word] = 1
#
#         print(word_dict[word], end=" ")
#
#     return word_dict
#
#
# text = input()
# word_dict = count_word_occurrences(text)

#шифрование

# def transliterate_char(char):
#     translit_dict = {
#         'А': 'A', 'а': 'a',
#         'Б': 'B', 'б': 'b',
#         'В': 'V', 'в': 'v',
#         'Г': 'G', 'г': 'g',
#         'Д': 'D', 'д': 'd',
#         'Е': 'E', 'е': 'e',
#         'Ё': 'E', 'ё': 'e',
#         'Ж': 'Zh', 'ж': 'zh',
#         'З': 'Z', 'з': 'z',
#         'И': 'I', 'и': 'i',
#         'Й': 'I', 'й': 'i',
#         'К': 'K', 'к': 'k',
#         'Л': 'L', 'л': 'l',
#         'М': 'M', 'м': 'm',
#         'Н': 'N', 'н': 'n',
#         'О': 'O', 'о': 'o',
#         'П': 'P', 'п': 'p',
#         'Р': 'R', 'р': 'r',
#         'С': 'S', 'с': 's',
#         'Т': 'T', 'т': 't',
#         'У': 'U', 'у': 'u',
#         'Ф': 'F', 'ф': 'f',
#         'Х': 'Kh', 'х': 'kh',
#         'Ц': 'Ts', 'ц': 'ts',
#         'Ч': 'Ch', 'ч': 'ch',
#         'Ш': 'Sh', 'ш': 'sh',
#         'Щ': 'Shch', 'щ': 'shch',
#         'Ъ': 'Ie', 'ъ': 'ie',
#         'Ы': 'Y', 'ы': 'y',
#         'Э': 'Eh', 'э': 'eh',
#         'Ю': 'Iu', 'ю': 'iu',
#         'Я': 'Ia', 'я': 'ia',
#         'Ь': '', 'ь': '',
#     }
#
#     return translit_dict.get(char, char)
#
# def transliterate(text):
#     result = ''
#     for char in text:
#         result += transliterate_char(char)
#     return result
#
#
# text = input()
# transliterated_text = transliterate(text)
# print(transliterated_text)
#шифрованиеend

# dct = 'А (а) → A (a), Б (б) → B (b), В (в) → V (v), Г (г) → G (g), Д (д) → D (d), Е (е) → E (e), Ё (ё) → E (e), Ж (ж) → Zh (zh), З (з) → Z (z), И (и) → I (i), Й (й) → I (i), К (к) → K (k), Л (л) → L (l), М (м) → M (m), Н (н) → N (n), О (о) → O (o), П (п) → P (p), Р (р) → R (r), С (с) → S (s), Т (т) → T (t), У (у) → U (u), Ф (ф) → F (f), Х (х) → Kh (kh), Ц (ц) → Ts (ts), Ч (ч) → Ch (ch), Ш (ш) → Sh (sh), Щ (щ) → Shch (shch), Ы (ы) → Y (y), Ъ (ъ) → Ie (ie), Э (э) → Eh (e), Ю (ю) → Iu (iu), Я (я) → Ia (ia)'.split(', ')
# dct = dict([(s.split(' → ')[0].split()[0], s.split(' → ')[1].split()[0]) for s in dct] + [('Ь', '')])
#
# mystr='''
# (А, а -> (A), (a)
# Б, б -> (B), (b)
# В, в -> (V), (v)
# Г, г -> (G), (g)
# Д, д -> (D), (d)
# Е, е -> (E), (e)
# Ё, ё -> (E), (e)
# Ж, ж -> (Zh), (zh)
# З, з -> (Z), (z)
# И, и -> (I), (i)
# Й, й -> (I), (i)
# К, к -> (K), (k)
# Л, л -> (L), (l)
# М, м -> (M), (m)
# Н, н -> (N), (n)
# О, о -> (O), (o)
# П, п -> (P), (p)
# Р, р -> (R), (r)
# С, с -> (S), (s)
# Т, т -> (T), (t)
# У, у -> (U), (u)
# Ф, ф -> (F), (f)
# Х, х -> (Kh), (kh)
# Ц, ц -> (Ts), (ts)
# Ч, ч -> (Ch), (ch)
# Ш, ш -> (Sh), (sh)
# Щ, щ -> (Shch), (shch)
# Ъ, ъ -> (Ie), (ie)
# Ы, ы -> (Y), (y)
# Э, э -> (Eh), (eh)
# Ю, ю -> (Iu), (iu)
# Я, я -> (Ia), (ia) '''
#
# mystr2=mystr.split('\n')
# # print(mystr2)
# l= {}
# for i in mystr2:
#     i.split("->")
#
#     print(i)
#
#
#     # l[i[1]]=i[7]
#     print(l)

# mystr3=mystr.split(',')
# print(mystr2)
# mystr4=mystr3.replace("->", ":")



#3 упереводим строку в словарь
mystr = '''
А, а -> (A), (a)
Б, б -> (B), (b)
В, в -> (V), (v)
Г, г -> (G), (g)
Д, д -> (D), (d)
Е, е -> (E), (e)
Ё, ё -> (E), (e)
Ж, ж -> (Zh), (zh)
З, з -> (Z), (z)
И, и -> (I), (i)
Й, й -> (I), (i)
К, к -> (K), (k)
Л, л -> (L), (l)
М, м -> (M), (m)
Н, н -> (N), (n)
О, о -> (O), (o)
П, п -> (P), (p)
Р, р -> (R), (r)
С, с -> (S), (s)
Т, т -> (T), (t)
У, у -> (U), (u)
Ф, ф -> (F), (f)
Х, х -> (Kh), (kh)
Ц, ц -> (Ts), (ts)
Ч, ч -> (Ch), (ch)
Ш, ш -> (Sh), (sh)
Щ, щ -> (Shch), (shch)
Ъ, ъ -> (Ie), (ie)
Ы, ы -> (Y), (y)
Э, э -> (Eh), (eh)
Ю, ю -> (Iu), (iu)
Я, я -> (Ia), (ia) '''

# translit_dict = {}
#
# # Splitting the input string by lines
# mystr=mystr.strip()
# lines = mystr.split('\n')
# # print(lines)
#
# # Processing each line to extract the mappings and populate the translit_dict
# for line in lines:
#     parts = line.strip().split(' -> ')
#     # print("parts",parts)
#     cyrillic_chars = parts[0].split(', ')
#     # print(cyrillic_chars, "cyrillic_chars,")
#     latin_chars = parts[1].replace("(", "").replace(")", "").split(', ')
#
#     for i in range(len(cyrillic_chars)):
#         translit_dict[cyrillic_chars[i]] = latin_chars[i]
#
# # Adding Ь and ь as empty strings
# translit_dict['Ь'] = ''
# translit_dict['ь'] = ''
#
# print(translit_dict)


# n = int(input())
# dict = {}
# for i in range(n):
#     line = input()
#     line = line.split()
#     if line[2] not in dict:
#         dict[line[2]] = line[0]
#     else:
#         dict[line[2]] =  line[0]+" "+dict[line[2]]
#
# month = int(input())
# for i in range(month):
#     month2 = input()
#     # print()
#     print(dict.get(month2, ""))


# a=input().split()
#
# spisok=[]
#
# for i in a:
#     dict = {}
#     two=bin(int(i))
#     print(two)
#     print(len(two))
#     dict["len"]=(len(two)-2)
#     dict[0]=two.count("0")-1
#     dict[1]=two.count("1")
#     spisok.append(dict)
#
# print(spisok)


# def check_city_existence(city_list, new_city):
#     city_set = set(city_list)
#     if new_city in city_set:
#         return "Было"
#     else:
#         return "Ок"
#
# # Пример использования
# num_cities = int(input())
# cities = []
#
# for i in range(num_cities):
#     city_name = input()
#     cities.append(city_name)
#
# new_city_name = input()
# result = check_city_existence(cities, new_city_name)
# print(result)


# def check_city_existence(city_list, new_city):
#     city_set = set(city_list)
#     if new_city in city_set:
#         return "Было"
#     else:
#         return "Ок"
#
# # Пример использования
# num_cities = int(input())
# cities = []
#
# for i in range(num_cities):
#     city_name = input()
#     cities.append(city_name)
#
# new_city_name = input()
# result = check_city_existence(cities, new_city_name)
# print(result)


# a = set(map(int, iter(input, ''))) & set(map(int, iter(input, '')))
# if a :
#     print(*sorted(a))
# else:
#     print("Пусто")


# put your python code here

"fhefe"
# listki = int(input())
#
#
#
#
# seto = []
# for i in range(listki):
#
#     setfamilii = set()
#     print(setfamilii,"setfamilii")
#     stroki = int(input())
#     for e in range(stroki):
#         familii=input()
#         setfamilii.add(familii)
#         print(setfamilii,"setfamilii")
#     seto.append(setfamilii)
#     print(seto)
#
#
# print(seto)
# a=0
# many=seto[a].intersection(seto[a+1])
# for a in range(len(seto)-1):
#     many=many.intersection(seto[a+1])
# print(many)

# Примеры
#
# spam = {
#     1: 100,
#     2: 2.5,
#     "алгоритм": "algorithm",
#     (0, 1, 2, 3, 4, 5, 6, 7, 8, 9): "numbers"
#
#
# }
# print(spam.keys())
# a=2
# for i in spam.keys():
#     if a == i or a in i:
#         print("yes")

#
# student_grades = {
#     ("Иванов", "Математика"): 85,
#     ("Иванов", "Физика"): 92,
#     ("Петров", "Математика"): 78,
#     ("Петров", "Физика"): 88,
# }
#
# last_name = "Иванов"
# grades_for_ivanov = {}
#
# for key in student_grades:
#     print(key)
#     if key[0] == last_name:
#         grades_for_ivanov[key[1]] = student_grades[key]
#
# print("Оценки Иванова:", grades_for_ivanov)


# Создание списка учеников
# students_list = ["Иванов", "Петров", "Сидоров", "Козлов"]
#
# # Преобразование списка в словарь с номерами учеников в качестве ключей
# students_dict = {}
# for i, student in enumerate(students_list):
#     print(student)
#     students_dict[i+1] = student
#
# # Вывод полученного словаря
# print(students_dict)



# Пример словаря с кортежами в качестве ключей
# student_grades = {
#     ("Иванов", "Математика"): 85,
#     ("Иванов", "Физика"): 92,
#     ("Петров", "Математика"): 78,
#     ("Петров", "Физика"): 88,
# }
#
# # Пример обращения к словарю с использованием кортежа в качестве ключа
# grade_math_ivanov = student_grades[("Иванов", "Математика")]
# print("Оценка Иванова по математике:", grade_math_ivanov)  # Вывод: Оценка Иванова по математике: 85
#
# grade_physics_petrov = student_grades[("Петров", "Физика")]
# print("Оценка Петрова по физике:", grade_physics_petrov)  # Вывод: Оценка Петрова по физике: 88



spam = {
    1: 100,
    2: 2.5,
    "алгоритм": "algorithm",
    "numbers": (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
}
spam[7]=6
print(spam)

if "algorithm" in spam:
    print(spam["алгоритм"])