import sys
code_list = list()
for line in sys.stdin:
    code_list.append(line.strip())
print(sum(map(lambda x: x[0]=='#', code_list)))
