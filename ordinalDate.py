days = {1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30,
        10:31, 11:30, 12:31}

def february(year):
    #Возвращает кол-во дней в феврале
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                res = 29
            else:
                res = 28
        else:
            res = 29
    else:
        res = 28

    return res


def ordinalDate(day,month,year):
    #Возвращает порядковый номер дня в этом году
    month_calc = 1
    day_number = 0
    while month_calc < month:
        if month_calc != 2:
            day_number += days[month_calc]
        else:
            day_number += february(year)
        month_calc += 1

    day_number += day
    return day_number


def main():
    day = int(input("Введите дату(день): "))
    month = int(input("Введите дату(месяц): "))
    year = int(input("Введите дату(год): "))
    print ("Порядковый номер дня: ", ordinalDate(day,month,year))



if __name__ == '__main__':
    test = 353
    test_x = ordinalDate(19,12,2022)
    if test == test_x:
        print("Первый тест пройден.")
    else:
        print("Возникла ошибка, необхдимо исправлять код...")

    test = 157
    test_x = ordinalDate(5,6,1964)
    if test == test_x:
        print("Второй тест пройден.")
    else:
        print("Возникла ошибка, необхдимо исправлять код...")

else:
    main()
