import sys
code_dict = dict()
count = 0
for line in sys.stdin:
    count += 1
    if line[0]=="#":
        code_dict[count] = line[1:].strip()
[print(f"Line {i}: {code_dict[i]}") for i in code_dict]
