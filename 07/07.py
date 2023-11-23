phrase = input()
line = ""
for elem in range(len(phrase)):
    line += (str(ord(phrase[elem])))
    line += ','
print(line[:-1])

