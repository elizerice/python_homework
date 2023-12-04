line = input().split()
sum_list = []
num_1, num_2 = [int(i) for i in input().split()]
for i in range(num_1, num_2 + 1):
    sum_list.append(int(line[i]) ** 2)
print(sum(sum_list))
