def quarter():
    x = float(input())
    y = float(input())
    if x < 0:
        if y < 0:
            print('3 четверть')
        else:
            print('2 четверть')
    else:
        if y < 0:
            print('4 четверть')
        else:
            print('1 четверть')
quarter()
