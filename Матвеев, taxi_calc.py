def taxi_calc(distance, pay = 0.25, pay_line=140, base = 4):
    #Базовая стоимость - 4 у.е. distance - в километрах.
    distance = distance * 1000 #Перевод в метры
    total_pay_line = distance / pay_line
    total_pay_line = round(total_pay_line,0)
    res = total_pay_line * pay
    res = res + base
    return res


def main():
    distance = float(input("Введите пройденную такси дистанцию в КМ >> "))
    print(taxi_calc(distance))



if __name__ == '__main__':
    main()
