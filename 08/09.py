for i in range(int(input())):
    line = str(input())
    if line[0:2] == '%%':
        print(line[2:])
    elif '##' not in line:
        print(line)
