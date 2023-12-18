n = int(input())
count = 1
result = 0
for i in range(n):
    num = int(input())
    count += 1
    if count % 2 == 0:
        result = result + num
    else:
        result = result - num
print(result)
