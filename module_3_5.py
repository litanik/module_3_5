# 1. Создаем функцию get_multiplied_digits и параметр number в ней.
def get_multiplied_digits(number):

    # 2. Создаем переменную str_number и записываем строковое
    # представление (str) числа number в нее.
    str_number = str(number)

    # 3. Отделение первой цифры в числе: создаем переменную first и записываем
    # в нее первый символ из str_number в числовом представлении(int).
    first = int(str_number[0])

    # 4. Если длина str_number > 1, то возвращается значение first * get_multiplied_digits(int(str_number[1:])).
    # Таким образом умножаем первую цифру числа на результат работы этой же функции с числом,
    # но уже без первой цифры.
    # 4 пункт можно выполнить только тогда, когда длина str_number > 1, т.к.
    # в противном случае не получиться взять срез str_number[1:]

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    # 6. Если же длина str_number не больше 1, тогда возвращаем оставшуюся цифру first
    else:
        return first


result1 = get_multiplied_digits(int('40203'))
print(result1)
result2 = get_multiplied_digits(int('00123'))
print(result2)
