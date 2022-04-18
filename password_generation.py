"""
Генератор паролей
"""
import random


def good_password_generation(length):
    alphabet = (
        '0123456789'
        'abcdefghijklmnopqrstuvwxyz'
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        '!@#$%^&*()+-'
    )

    result = ''
    for i in range(length):
       symbol = random.choice(alphabet)
       result += symbol
    return result

result = good_password_generation(10)  # Количество символов в пароле
print(result)
