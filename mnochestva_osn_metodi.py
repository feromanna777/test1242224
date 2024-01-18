Объединение.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

c = a.union(b)

print(c)  # {1, 2, 3, 4, 5, 6}
Метод .union() возвращает новое множество, являющееся объединением множеств a и b.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a.update(b)

print(a)  # {1, 2, 3, 4, 5, 6}
print(b)  # {3, 4, 5, 6}
Метод .update() добавляет в множество a все элементы из множества b.



Пересечение.



a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

c = a.intersection(b)

print(c)  # {3, 4}
Метод .intersection() возвращает новое множество, являющееся пересечением множеств a и b.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a.intersection_update(b)

print(a)  # {3, 4}
print(b)  # {3, 4, 5, 6}
Метод .intersection_update() оставляет в множестве a только те элементы, которые есть в множестве b.


Разность.



a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

c = a.difference(b)

print(c)  # {1, 2}
Метод .difference() возвращает новое множество - элементы входящие в множество a, но не входящие в b.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a.difference_update(b)

print(a)  # {1, 2}
print(b)  # {3, 4, 5, 6}
Метод .difference_update() удаляет из множества a все элементы, входящие в b.



a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

c = a.symmetric_difference(b)

print(c)  # {1, 2, 5, 6}
Метод .symmetric_difference() возвращает новое множество - элементы, входящие в a или в b, но не в оба из них одновременно.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a.symmetric_difference_update(b)

print(a)  # {1, 2, 5, 6}
print(b)  # {3, 4, 5, 6}
Метод .difference_update() записывает в a симметрическую разность множеств a и b.



Для добавления элемента в множество нужно использовать метод .add() (добавлять).

many = set()

many.add(10)
many.add(2.5)
many.add(tuple(range(0, 10)))

print(many)
# {(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 10, 2.5}



Если необходимо добавить в множество несколько значений, то можно использовать метод .update() (обновить).

many = set()

many.update([10, 2.5, "алгоритм"])
many.update("автоматизация")

print(many)
# {2.5, 'т', 'ц', 10, 'алгоритм', 'в', 'я', 'а', 'и', 'з', 'м', 'о'}

'''
Чтобы удалить элемент
из множества нужно использовать
метод .remove()(удалить).'''

many = {10, 2.5, "алгоритм", (10, 20, 30)}

many.remove("алгоритм")

print(many)  # {10, 2.5, (10, 20, 30)}
'''
Если
удаляемый
элемент
отсутствует
в
множестве, то
программа
вернёт
ошибку.Поэтому, перед удалением стоит проверить
наличие элемента в множестве с
помощью оператора in (оператор вхождения).'''

many = {10, 2.5, "алгоритм", (10, 20, 30)}

if "алгоритм" in many:
    many.remove("алгоритм")
else:
    print("Ошибка! Элемента в множестве нет!")

print(many)  # {10, 2.5, (10, 20, 30)}

Ещё
один
способ
удаления
элемента
из
множества
по
значению, это
использование
метода.discard()(выбросить).

many = {10, 2.5, "алгоритм", (10, 20, 30)}

many.discard("алгоритм")
many.discard("алгоритм")

print(many)  # {10, 2.5, (10, 20, 30)}
Если
удаляемый
элемент
отсутствует
в
множестве, то
метод
проигнорирует
удаление
и
ничего
не
произойдёт.

Также
удалять
элементы
из
множества
можно
и
с
помощью
метода.pop().

many = {10, 2.5, "алгоритм", (10, 20, 30)}

temp = many.pop()
print(temp)  # алгоритм

many.pop()

print(many)  # {2.5, (10, 20, 30)}