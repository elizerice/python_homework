step = int(input())
phrase = str(input())
answer = str()
for i in range(len(phrase)):
    symbol = phrase[i]
    if symbol != ' ':
        if ord(symbol) >= 1072 and ord(symbol) <= 1103:
            char = ord(symbol) + step
            if char > 1103:
                char = char - 32
            symbol = chr(char)
        elif ord(symbol) >= 1040 and ord(symbol) <= 1071:
            char = ord(symbol) + step
            if char > 1071:
                char = char - 32
            symbol = chr(char)
    else:
        symbol = ' '
    answer += symbol
print(answer)
