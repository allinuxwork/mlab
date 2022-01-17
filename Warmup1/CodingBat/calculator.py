def calculate():
    operation = input('''
    Пожалуйста, введите математическую операцию, которую вы хотели бы выполнить:
    + сложение
    - вычитание
    * умножение
    / деление
    ''')
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
    else:
        print('Вы не ввели допустимый оператор, пожалуйста, запустите программу еще раз.')
        again()

def again():
    calc_again = input('''
    Вы хотите снова посчитать?
    Пожалуйста, введите Y для ДА или N для НЕТ.
    ''')
    if calc_again == 'Y':
        calculate()
    elif calc_again == 'N':
        print('До свидания.')
    else:
        again()

calculate()