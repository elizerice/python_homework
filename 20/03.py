import sys
height_list = []
for height in sys.stdin:
    height_list.append(int(height))
print(sum(height_list)/len(height_list))
