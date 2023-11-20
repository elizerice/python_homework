num = int(input())
city_list = set()
for i in range(num):
    city = input()
    if city in city_list:
        repetition = True
    else:
        repetition = False
    city_list.add(city)
if repetition == True:
    print('TRY ANOTHER')
else:
    print('OK')
