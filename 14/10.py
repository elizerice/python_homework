def golden_ratio(i):
    fibonacci = [1, 1]
    for i in range(2, i + 1):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
        print(fibonacci)
    print(fibonacci[i] / fibonacci[i - 1])
