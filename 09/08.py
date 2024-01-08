soup_list = ['щи', 'борщ', 'щавелевый суп','овсяный суп', 'суп по-чабански']
for i in range(int(input())):
    if i >= 4:
        print(soup_list[i - 5])
    else:
        print(soup_list[i])
