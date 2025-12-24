
lst_months = [[1, 31], [2,28], [3,31], [4,30], [5,31], [6,30], [7,31], [8,31], [9,30], [10,31], [11,30], [12,31]]
lst_in = ['24', '03', '2001', '22:33:44']
#lst_in = input().split()
integer = input()

def date_in_future(integer):

    all_days = 0
    for i in range(int(lst_in[1])):
        if i != int(lst_in[1]) - 1:
            all_days += lst_months[i][1]
        else:
            all_days += int(lst_in[0])

    year = int(lst_in[2])
    month = 1
    all_days += integer

    while True:
        if month == 1 and all_days <= lst_months[0][1]:
            return formating([all_days, month, year, lst_in[3]])
        else:
            all_days -= lst_months[0][1]
            month += 1
        if month == 2 and all_days <= lst_months[1][1]:
            return formating([all_days, month, year, lst_in[3]])
        else:
            all_days -= lst_months[1][1]
            month += 1
        if month == 3 and all_days <= lst_months[2][1]:
            return formating([all_days, month, year, lst_in[3]])
        else:
            all_days -= lst_months[2][1]
            month += 1
        if month == 4 and all_days <= lst_months[3][1]:
            return formating([all_days, month, year, lst_in[3]])
        else:
            all_days -= lst_months[3][1]
            month += 1
        if month == 5 and all_days <= lst_months[4][1]:
            return formating([all_days, month, year, lst_in[3]])
        else:
            all_days -= lst_months[4][1]
            month += 1
        if month == 6 and all_days <= lst_months[5][1]:
            return formating([all_days, month, year, lst_in[3]])
        else:
            all_days -= lst_months[5][1]
            month += 1
        if month == 7 and all_days <= lst_months[6][1]:
            return formating([all_days, month, year, lst_in[3]])
        else:
            all_days -= lst_months[6][1]
            month += 1
        if month == 8 and all_days <= lst_months[7][1]:
            return formating([all_days, month, year, lst_in[3]])
        else:
            all_days -= lst_months[7][1]
            month += 1
        if month == 9 and all_days <= lst_months[8][1]:
            return formating([all_days, month, year, lst_in[3]])
        else:
            all_days -= lst_months[8][1]
            month += 1
        if month == 10 and all_days <= lst_months[9][1]:
            return formating([all_days, month, year, lst_in[3]])
        else:
            all_days -= lst_months[9][1]
            month += 1
        if month == 11 and all_days <= lst_months[10][1]:
            return formating([all_days, month, year, lst_in[3]])
        else:
            all_days -= lst_months[10][1]
            month += 1
        if month == 12 and all_days <= lst_months[11][1]:
            return formating([all_days, month, year, lst_in[3]])
        else:
            year += 1
            all_days -= lst_months[11][1]
            month = 1


def formating(lst):
    if len(str(lst[0])) == 1:
        lst[0] = '0' + str(lst[0])
    if len(str(lst[1])) == 1:
        lst[1] = '0' + str(lst[1])
    return f'{lst[0]}-{lst[1]}-{lst[2]} {lst[3]}'

if integer.isdigit():
    integer = int(integer)
    print(date_in_future(integer))
else:
    print('Введите корректное число, вывожу входные данные: ', end='')
    print(formating(lst_in))

