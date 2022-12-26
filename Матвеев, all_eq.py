def all_eq(lst):
    lst_res = []
    a = len(max(lst))
    for str in lst:
        while len(str) < a:
            str = str + '_'
        lst_res.append(str)

    return lst_res


if __name__ == '__main__':
    list = ['Первая строка', 'Сааааамая длииинная строкаааа', 'Вторая строка']
    lst_res = all_eq(list)
    for str in lst_res:
        print(str)
