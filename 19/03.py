nums = filter(lambda x: x % 9 == 0, range(10, 100))
sum_num_sqr = sum(map(lambda x: x ** 2, nums))
print(sum_num_sqr)
