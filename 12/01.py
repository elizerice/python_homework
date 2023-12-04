for i in range(int(input())):
    line = str(input())
    if line.find('кот') != -1:
        print(i + 1, line.find('кот') + 1)
