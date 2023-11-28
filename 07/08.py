number = int(input())
symbol = int(str(number)[0])
while number < 1000000000 and symbol != 1:
    symbol = int(str(number)[0])
    number = number * symbol
print(number)
