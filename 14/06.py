def print_average(arr):
    sum = 0
    if arr == []:
        print('0')
    else:
        for num in arr:
            sum += num
            print(sum / len(arr))
