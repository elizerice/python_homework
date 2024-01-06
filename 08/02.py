word_1 = str(input())
word_2 = str(input())
cows = int()
bulls = int()
for i in set(word_1):
    if i in set(word_2):
        cows += 1
for i in range(len(word_1)):
    if word_1[i] == word_2[i]:
        bulls += 1
        cows -= 1
print(bulls, cows)
