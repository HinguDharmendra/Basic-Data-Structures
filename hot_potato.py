import random


def hot_potato(name_list, number):
    q = []
    for name in name_list:
        q.append(name)

    while len(q) > 1:
        for i in range(number):
            q.append(q.pop(0))
        print(q.pop(0), ' is out of game')

    return q.pop(0)


def main():
    name_list = ['Hingu', 'Pingu', 'Tingu', 'Jingu', 'Guddi', 'Mehul', 'Tina', 'Kushu']
    number = random.randint(0, 10)
    print(number)
    print(hot_potato(name_list, number))


if __name__ == '__main__':
    main()
