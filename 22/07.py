import datetime
import math

birthday = input().split('.')
birthday_date = datetime.date(int(birthday[2]), int(birthday[1]), int(birthday[0]))

biorytm = input().split('.')
biorytm_date = datetime.date(int(biorytm[2]), int(biorytm[1]), int(biorytm[0]))

pi = math.pi
T = (biorytm_date- birthday_date).days
physical = round(math.sin((2 * pi * T)/23) * 100, 2)
emotional = round(math.sin((2 * pi * T)/28) * 100, 2)
intellectual = round(math.sin((2 * pi * T)/33) * 100, 2)
print(physical)
print(emotional)
print(intellectual)
