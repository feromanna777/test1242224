def caesar_cipher(message, shift):
    result = ''
    for char in message:
        if char.isalpha():  # Проверяем, является ли символ буквой
            base = ord('А') if char.isupper() else ord('а')  # Определяем базовый код для 'А' или 'а'
            shifted_char_code = (ord(char) - base + shift) % 32 + base  # Вычисляем сдвинутый код символа
            print("ord(char)",ord(char))

            result += chr(shifted_char_code)
        else:
            result += char  # Если символ не является буквой, добавляем его как есть
    return result

# Пример использования функции:
shift = int(input())  # Вводим шаг шифрования
message = input()  # Вводим сообщение для шифрования
encrypted_message = caesar_cipher(message, shift)
print(encrypted_message)