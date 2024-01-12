def print_statistics(arr):
    sum = 0
    if arr == []:
        print('0')
    else:
        for num in arr:
            sum += num
        print(len(arr))
        print(sum / len(arr))
        print(min(arr))
        print(max(arr))
        mediana(arr)

def mediana(arr):
    arr_sorted = sorted(arr)
    if len(arr) % 2 != 0:
        print(arr_sorted[len(arr_sorted) // 2])
    else:
        print(((arr_sorted[len(arr_sorted) // 2 - 1] + arr_sorted[len(arr_sorted) // 2]) / 2))
