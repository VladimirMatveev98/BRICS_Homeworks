numbers = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six',
            7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten', 11:'Eleven',
            12:'Twelwe'}

def main_task(number):
    try:
        print(numbers[number])
    except:
        return False


def main():
    for i in range (1,13):
        print(numbers[i])



if __name__ == '__main__':
    main()
