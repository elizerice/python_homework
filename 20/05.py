import sys
print(any('0' in line.split() for line in list(sys.stdin)))
