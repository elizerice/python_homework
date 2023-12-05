https://disk.yandex.ru/d/dCRdQi0UaZ8P7Q
#1незак
lines = list()
import sys
for line in sys.stdin:
    lines.append((line.strip('\n')).split('-=-'))
line_filter = []

for line in lines:
        line_filter.append("&".join(filter(lambda x: len(str(line)) % 2 == 0, line)).split())
for n in line_filter:
    print(*n)
