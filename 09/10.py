num_list = list()
sum = 0
for _ in range(int(input())):
    num = int(input())
    num_list.append(num)
start = int(input())
end = int(input())
for i in num_list[start - 1:end]:
    sum += i
print(sum)
