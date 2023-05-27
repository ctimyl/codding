from random import *

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
chars = []

quantity_pw = int(input('Укажите количество паролей для генерации: '))
len_pw = int(input('Укажите желаюмую длину пароля: '))
number_pw = input('Включать ли цифры? (y/n) ')
if number_pw == 'y':
    chars += [i for i in digits]
letters_upp_pw = input('Включать ли прописные буквы? (y/n) ')
if letters_upp_pw == 'y':
    chars += [i for i in lowercase_letters]
letter_low_pw = input('Включать ли строчные буквы? (y/n) ')
if letter_low_pw == 'y':
    chars += [i for i in uppercase_letters]
symbols_pw = input('Включать ли спецсимволы? (y/n) ')
if symbols_pw == 'y':
    chars += [i for i in punctuation]
double_pw = input('Исключать ли неоднозначные символы il1Lo0O? (y/n) ')
if double_pw == 'n':
    if "i" in chars:
        chars.remove("i")
    elif "l" in chars:
        chars.remove('l')
    elif "1" in chars:
        chars.remove('1')
    elif "L" in chars:
        chars.remove('L')
    elif "o" in chars:
        chars.remove('o')
    elif "O" in chars:
        chars.remove('0')
    elif "0" in chars:
        chars.remove('O')

def generate_password(length, chars):
    password = []
    for i in range(length):
        password += chars[randrange(0, len(chars))]
    return "".join(password)


for i in range(quantity_pw):
    print(generate_password(len_pw, chars))
