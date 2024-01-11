for _ in range(int(input())):
    line = str(input())
    line_copy = line.split()
    pyramide = list()
    for i in range(1, len(line_copy)):
        pyramide.append(max(line_copy[0], line_copy[-1]))
        line_copy.remove(max(line_copy[0], line_copy[-1]))
    pyramide.append(line_copy[0])
    if pyramide != sorted(pyramide, reverse=True):
        print('НЕТ')
    else:
        print(*pyramide)
