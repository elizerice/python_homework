num = 0
sum = int()
count = 0
number = int(1)
while number != 0:
    number = int(input())
    count += 1
    sum += number
    if num == 0:
        if sum >= 10:
            print(count)
            
