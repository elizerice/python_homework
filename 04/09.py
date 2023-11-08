num = int(input())
void_sum = 0
sum = 1
for i in range(num):
    void = ' ' * (num - void_sum)
    print(void, '*' * sum)
    void_sum += 1
    sum += 2
