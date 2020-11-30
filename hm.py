# 1)Дан лист:
l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
while True:
    print('1. найти min число в листе')
    print('2. удалить все одинаковые значения')
    print('3. заменить каждое четвертое значение на "Х"')
    print('4. вывести элемент листа, значение которого ближе всего к среднему арифметическому всех елементов в листе')
    print('5. выход')
    ch = input('Сделайте свой выбор: ')

    if ch == '1':  # - найти min число в листе
        print("min value element : ", min(l))
        print(min(l))

    elif ch == '2':  # - удалить все одинаковые значения
        print(set(l))

    elif ch == '3':  # - заменить каждое четвертое значение на "Х"
        l1 = ['X' if i % 4 == 0 else l[i - 1] for i in range(1, len(l) + 1)]
        print(l1)

    elif ch == '4':
        avg = sum(l) / len(l)
        print(avg)
        min = l[0]

        for i in l:
           d = abs(i - avg)
           k = abs(min - avg)
        if d < k:
            min = i
        print(min)

    elif ch == '5':
        print('END')
    break

# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
######################################
i = 0
size = 7
for i in range(size):
    if i == 0 or i == size - 1:
        sq = ('*' + ' ') * size
    else:
        sq = '* ' + '  ' * (size - 2) + '*'
    print(sq)

# 4) вывести табличку умножения с помощью цикла while
size = 5
for row in range(1, size + 1):
    for column in range(1, size + 1):
        print(row * column, end='\t')
    print()
