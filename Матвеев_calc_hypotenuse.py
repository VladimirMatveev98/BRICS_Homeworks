def calc_hypotenuse(a, b):
    #Работает только с прямоугольным треугольником
    c = (a*a) + (b*b)
    c = c ** 0.5
    return c


def main():
    a = int(input("Введите первый катет прямоугольного треугольника: "))
    b = int(input("Введите второй катет прямоугольного треугольника: "))
    print(calc_hypotenuse(a,b))



if __name__ == '__main__':
    main()
