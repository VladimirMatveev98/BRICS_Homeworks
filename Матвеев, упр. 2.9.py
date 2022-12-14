def deposit(sum,per,years):
    if years > 0:
        years -= 1
        sum = sum + (sum * per)
        print("%.2f" % sum)
        deposit(sum,per,years)


if __name__ == '__main__':
    deposit(10000,0.18,5)
    a = print("Нажмите ENTER для продолжения...")
