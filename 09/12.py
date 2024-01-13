line = input().split()
error_list = list()
sum = 0
for i in range(int(line[0])):
    reciepe_line = input().split()
    sum_product = int(reciepe_line[1][1:])
    result_product = int(reciepe_line[2][1:])
    sum += result_product
    if int(reciepe_line[0]) * sum_product != result_product:
        error_list.append(i + 1)
print(int(line[1]) - sum)
print(*error_list)
