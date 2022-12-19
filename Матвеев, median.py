list = ['bug','debug','42']

#Для интереса, я попробовал выполнить сортировку самостоятельно:
def shaker_sort(list):
    """Проходит по массиву, сравнивая текущий элемент со следующим. Если
    следующий элемент меньше, меняет их местами. Пройдя до конца, начинает
    сравнивать текщий элемент с предыдущим. Если предыдущий элемент больше,
    меняет их местами. Когда весь массив отсортирован, заканчивает работу.
    Работает быстрее пузырьковой сортировки за счёт переноса малых чисел
    в начало списка"""

    i = 0
    a = 0
    operating_range = len(list) - 1
    while a <= operating_range:
        for i in range (1,operating_range):
            if list[i - 1] > list[i]:
                list[i - 1], list[i] = list[i], list[i - 1]
        i = 0
        for i in range (operating_range,1, -1):
            if list[i] < list[i - 1]:
                list[i], list[i - 1] = list[i - 1], list[i]
        a = a + 2
        operating_range = operating_range - 1


def calc_median(list):
    """Принимает на вход массив чисел и возвращает медиану
    на основе введённого массива. Массив должен быть отсортирован."""
    if len(list) % 2 == 0:
        a = len(list)
        a = a / 2
        a = int(a)
        median_1 = list[a]
        median_2 = list[a-1]
        res = (median_1 + median_2) / 2
    else:
        a = len(list)
        a = a / 2
        a = int(a)
        res = list[a]
    return res


def main():

    i = int(input("Сколько чисел Вы хотите ввести? "))
    list.clear()
    while i != 0:
        number = float(input("Введите число: "))
        i = i - 1
        list.append(number)

    #list.sort()
    shaker_sort(list)
    print(list)
    calc_median(list)
    print("Медиана для данных чисел равна", end = ' ')
    print(calc_median(list))



if __name__ == '__main__':
    main()
