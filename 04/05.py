result = 1
for i in range(6):
    num = int(input())
    if num == 0:
        num = 1
    result = result * num
print(result)
