# number = 50
# guess = int(input('Введите целое число : '))
# if guess == number:
#     print('Поздравляю, вы угадали,')
# elif guess < number:
#     print('Нет, загаданное число немного больше этого.')
# else:
#     print('Нет, загаданное число немного меньше этого.')

def func():
    number = 50 
    game = True
    while game:
        guess = int(input('Введите целое число : '))
        if guess == number:
            print('Поздравляю, вы угадали.')
            game = False
        elif guess < number:
            print('Нет, загаданное число немного больше этого.')
        else:
            print('Нет, загаданное число немного меньше этого.')
    else:
        print('ИГРА законченА')
func()