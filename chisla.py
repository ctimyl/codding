def is_valid(n):
    if n.isalpha() or n == "" or n == " ":
        return False
    elif int(n) in range(1, 101):
        return True


def games():
    import random
    num = random.randint(1, 100)
    print('Добро пожаловать в числовую угадайку')
    count = 1
    print(num)
    n = input('Введите число от 1 до 100: ')

    if is_valid(n) == True:
        while int(n) != num:
            if int(n) < num:
                n = input('Ваше число меньше загаданного, попробуйте еще разок: ')
            else:
                n = input('Ваше число больше загаданного, попробуйте еще разок: ')
            count += 1
        print(f'Вы угадали, поздравляем! И потратили на это {count} попыток')
    else:
        print('А может быть все-таки введем целое число от 1 до 100?: ')


games()
game = input("Сыграем еще раз? ")
if game == "да".lower():
    games()
else:
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
