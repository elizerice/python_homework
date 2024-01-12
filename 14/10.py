def golden_ratio(i):
    fibonacci = [1, 1]
    for j in range(2, i + 1):
        fibonacci.append(fibonacci[j - 1] + fibonacci[j - 2])
        print(fibonacci)
    print(fibonacci[i] / fibonacci[i - 1])
