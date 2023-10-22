line = str(input())
kop = len(line) * 40 % 100
rub = len(line) * 40 // 100
print(rub, 'р.', kop, 'коп.')
