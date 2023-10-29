days = int()
while True:
    temperature = float(input())
    days += 1
    if temperature >= 22:
        break
print(days // 7)
