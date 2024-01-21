import datetime as dt
days_before = int(input())
today = dt.datetime.now()
birthday = dt.timedelta(days=days_before) + today
print(birthday.day, birthday.month)
