def partial_sums(*num):
    sum = 0
    nums = list(num)
    nums.insert(0, 0)
    for i in range(len(nums)):
        sum += nums[i]
        nums[i] = sum
    return nums


print(partial_sums(13))
print(partial_sums(1, 0.5, 0.25, 0.125))
